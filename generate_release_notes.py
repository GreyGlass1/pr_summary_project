import os
import re
from github import Github
from openai import OpenAI
import requests
from dotenv import load_dotenv

load_dotenv()

GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")
print("Loaded GitHub token:", GITHUB_TOKEN)
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
REPO_NAME = "GreyGlass1/pr_summary_project"
RELEASE_TAG = "release-1.2.3"

gh = Github(GITHUB_TOKEN)
user = gh.get_user()
print(f"Authenticated as: {user.login}")
repo = gh.get_repo(REPO_NAME)
print(f"Connected to repo: {repo.full_name}")
client = OpenAI(
  api_key=os.environ['OPENAI_API_KEY'],  # this is also the default, it can be omitted
)

def fetch_prs(tag):
    prs = repo.get_pulls(state="closed", sort="updated")
    #return [pr for pr in prs if pr.merged and tag in [l.name for l in pr.labels]]
    matching_prs = []

    for pr in prs: 
        labels = [l.name for l in pr.labels]
        print(f"\nChecking PR #{pr.number}: {pr.title}")
        print(f" Labels: {labels}")
        print(f" Marged: {pr.merged}")
        print(f" State: {pr.state}")
        print(f" Patch URL: {pr.patch_url}")
        print(f"")

        if pr.merged and tag in labels:
            matching_prs.append(pr)

    return matching_prs

def summarise_pr(pr):
    # Fetch raw patch from GitHub
    # Extract owner and repo from REPO_NAME 
    owner, repo_name = REPO_NAME.split('/') 
    
    # Build API URL manually 
    patch_url = f"https://api.github.com/repos/{owner}/{repo_name}/pulls/{pr.number}" 
    
    headers = { 
        "Authorization": f"token {os.getenv('GITHUB_TOKEN')}", 
        "Accept": "application/vnd.github.v3.patch" 
        } 
    
    response = requests.get(patch_url, headers=headers) 
    
    if response.status_code != 200: 
        print(f"⚠️ Failed to fetch patch for PR #{pr.number}, Status: {response.status_code}") 
        print(f"Response body:\n{response.text[:300]}") 
        diff_text = "Could not retrieve diff." 
    else: 
        diff_text = response.text[:6000]

    prompt = f"""
    Summarise this Pull Request clearly and concisely.
    Title: {pr.title}
    Body: {pr.body}
    Diff:
    {diff_text}
    """

    completion = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.2,
    )

    return completion.choices[0].message.content.strip()


def main():
    print ("Starting script...")
    prs = fetch_prs(RELEASE_TAG)
    print(f"Found {len(prs)} PRs with tag {RELEASE_TAG}")
    output_file = f"release_notes_{RELEASE_TAG}.md"
    with open(output_file, "w", encoding="utf-8") as f:
        f.write(f"# Release Notes for {RELEASE_TAG}\n\n")
        for pr in prs:
            summary = summarise_pr(pr)
            f.write(f"### PR #{pr.number} – {pr.title}\n")
            f.write(f"{summary}\n\n---\n\n")
    print(f"Release notes saved to {output_file}")

if __name__ == "__main__":
    main()