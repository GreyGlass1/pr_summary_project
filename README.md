# 🧠 Context-Aware GitHub PR Summarisation Tool

This project automates the generation of high-quality release notes by semantically summarising merged pull requests based on a release tag. It enriches summaries with contextual understanding from your codebase and external dependencies, making them insightful, actionable, and easy to review.

---

## 🚀 Key Features

- **Release-Tag Based Summarisation**: Summarises only merged PRs with a given release label (e.g., `release-1.2.3`).
- **AI-Powered Summarisation with Semantic Context**: Uses OpenAI GPT-4 and LlamaIndex to summarise PRs with deep context awareness, including what changed, why it matters, and potential risks.
- **Codebase Indexing with Vector Search**: Automatically embeds your repo and any external Terraform module dependencies into a vector index for fast semantic retrieval.
- **External Module Tracking**: Scans `.tf` files for external Git module references and automatically clones & indexes the latest tag.
- **Scoring for PRs (Experimental)**: Each PR is rated with a quality score (out of 100%) and includes a reasoning explanation.
- **Summarised Output**: Generates both individual PR summaries and a combined executive release summary in Markdown format.

---

## 🔍 How the Tool Uses AI-Powered Semantic Search

This tool uses [LlamaIndex](https://www.llamaindex.ai/) to convert your codebase into embeddings stored in a vector index. When evaluating a PR, it uses the PR's code diff to semantically search this index and retrieve relevant context from your actual code. This context is included in a carefully structured prompt sent to OpenAI’s GPT-4 to produce high-quality summaries with understanding beyond simple diffs.

By combining vector search + AI reasoning, it can answer:
- Why a change was made
- What modules it impacts
- Potential side effects or risks
- How it fits into the overall architecture

---

## 🛠️ Setup

### Requirements
- Python 3.10+
- A GitHub access token
- OpenAI API key
- Your codebase cloned locally

### Installation
```bash
pip install -r requirements.txt
cp .env.example .env