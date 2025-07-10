import os
from datetime import datetime
import re
from github import Github
from openai import OpenAI
import requests
from llama_index.core import VectorStoreIndex, StorageContext, load_index_from_storage
from summariser import generate_combined_release_summary
from dotenv import load_dotenv

load_dotenv()

# === CONFIG ===
GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
REPO_NAME = os.getenv("REPO_NAME")
RELEASE_TAG = "release-1.2.3"
SUMMARY_DIR = "summaries"
os.makedirs(SUMMARY_DIR, exist_ok=True)

# === INIT ===
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
    summaries = []

    for pr in prs:
        summary = summarise_pr(pr)
        labels = [l.name for l in pr.labels]
        print(f"\nChecking PR #{pr.number}: {pr.title}")
        print(f" Labels: {labels}")
        print(f" Merged: {pr.merged}")
        print(f" State: {pr.state}")
        print(f" Patch URL: {pr.patch_url}")
        print(f"")

        summaries.append({
            "number": pr.number,
            "title": pr.title,
            "labels": labels,
            "summary": summary
        })

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

    # ✅ Load index from disk
    storage_context = StorageContext.from_defaults(persist_dir="index")
    index = load_index_from_storage(storage_context)

    # ✅ Query the index with the diff
    query_engine = index.as_query_engine()
    relevant_context = query_engine.query(diff_text)

    # 🧠 Construct a prompt using code context + PR info
    prompt = f"""
Summarise this Pull Request clearly and concisely.

🔍 Relevant Code Context:
{relevant_context}

📌 Title: {pr.title}

📝 Body: {pr.body}

🧾 Diff:
{diff_text}
"""
    # 🧠 Call OpenAI
    completion = client.chat.completions.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "You are a helpful assistant that summarises GitHub pull requests."},
            {"role": "user", "content": prompt}
        ],
        max_tokens=500,
        temperature=0.7,
    )

    return completion.choices[0].message.content.strip()


def main():
    print("🔍 Starting script...")

    prs = fetch_prs(RELEASE_TAG)
    print(f"✅ Found {len(prs)} PRs with tag {RELEASE_TAG}")

    # Timestamp
    now = datetime.now().strftime("%Y%m%d_%H%M")

    # File paths
    notes_filename = f"{RELEASE_TAG}_notes_{now}.md"
    summary_filename = f"{RELEASE_TAG}_summary_{now}.md"
    notes_path = os.path.join(SUMMARY_DIR, notes_filename)
    summary_path = os.path.join(SUMMARY_DIR, summary_filename)

    individual_summaries = []

    with open(notes_path, "w", encoding="utf-8") as f:
        f.write(f"# 📝 Release Notes for {RELEASE_TAG}\n\n")
        for pr in prs:
            title = pr.title
            summary = summarise_pr(pr)
            
            individual_summaries.append({
                "number": pr.number,
                "title": pr.title,
                "labels": [label.name for label in pr.labels],
                "summary": summary
            })
        for pr_summary in individual_summaries:
            f.write(f"### PR #{pr_summary['number']} - {pr_summary['title']}\n")
            f.write(f"{pr_summary['summary']}\n\n---\n\n")

    if individual_summaries:
        combined_summary = generate_combined_release_summary(individual_summaries)
        with open(summary_path, "w", encoding="utf-8") as f:
            f.write(f"# 🚀 Combined Release Summary for {RELEASE_TAG}\n\n")
            f.write(combined_summary)

    print(f"✅ Release notes saved to {notes_path}")
    print(f"✅ Combined summary saved to {summary_path}")


if __name__ == "__main__":
    main()