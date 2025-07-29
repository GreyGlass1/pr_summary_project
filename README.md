# 🧠 PR Summary Project

Automatically summarises GitHub pull requests and generates release notes, using OpenAI and context from your codebase (via Retrieval Augmented Generation).

---

## 🚀 Features

- Summarises merged PRs with a specific release label (e.g. `release-1.2.3`)
- Embeds and queries codebase using LLM-powered semantic search
- Generates clean, context-aware release notes in Markdown
- Local vector DB storage with Chroma
- Built with Python 3.13+

---

## 📁 Folder Structure
pr-summary-project/
├── codebase/                  # Codebase to embed
├── index/                     # Chroma vector DB index (auto-generated)
├── venv/                      # Python virtual environment
├── .env                       # API keys (not tracked)
├── context_embed.py           # Embeds and retrieves codebase context
├── generate_release_notes.py  # Main script
└── README.md

py -3.13 -m venv venv
venv\Scripts\activate.bat
python --version
pip install -r requirements.txt