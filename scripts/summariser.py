from openai import OpenAI
from config import OPENAI_API_KEY

# --- INIT ---
client = OpenAI(api_key=OPENAI_API_KEY)

def generate_combined_release_summary(summaries):
    prompt = """
You are a technical release manager. Write professional, concise release notes
for the following pull requests. Group them by related projects where possible
(e.g. based on labels or summary content).

Focus on describing changes at a feature or architectural level — avoid restating every PR line-by-line.
Conclude with a "Potential Risks" section if any PRs mention breaking changes or dependencies.
"""

    for s in summaries:
        prompt += f"- {s}\n"

    completion = client.chat.completions.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}],
        max_tokens=1000,
        temperature=0.4,
    )

    return completion.choices[0].message.content.strip()

def score_pr(pr):
    """
    Returns a score out of 100 and a reason string based on PR characteristics.
    """
    score = 100
    reasons = []

    if not pr.merged:
        score -= 50
        reasons.append("PR is not merged")

    if not pr.body or len(pr.body.strip()) < 20:
        score -= 20
        reasons.append("PR description is missing or too short")

    if not pr.labels:
        score -= 10
        reasons.append("No labels provided")

    if pr.title.strip().lower() in ["update", "test", "fix"]:
        score -= 10
        reasons.append("Title is too generic")

    if score >= 90:
        reasons.append("High-quality PR with good metadata")

    score = max(score, 0)
    reason_text = ", ".join(reasons) or "No issues found"

    return score, reason_text
