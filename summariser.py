from config import client

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