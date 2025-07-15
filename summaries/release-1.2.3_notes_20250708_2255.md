# 📝 Release Notes for release-1.2.3

### PR #3 - no context (test)
The pull request titled "update repo" is a minor update to the `generate_release_notes.py` file. The repository name has been updated from "GreyGlass1/test_repo" to "GreyGlass1/pr_summary_project". This change impacts one line of code in the file.

---

### PR #3 - no context (test)
Title: Embed codebase context for RAG

Summary: The pull request adds a new Python script (`context_embed.py`) to the project. This script uses the LlamaIndex to embed the project's source code into a Chroma vector store for semantic retrieval. The script scans the project root for Python files, excluding certain directories (`venv`, `index`, `.git`, `.vscode`), and writes these files into a temporary folder. It then creates a VectorStoreIndex from these documents and persists it in the 'index' subdirectory of the project root.

---

### PR #3 - no context (test)
The pull request titled "no context (test)" by teaton12 is a substantial update to the script 'generate_release_notes.py'. It involves 31 insertions and 10 deletions. It primarily focuses on enhancing the process of summarising pull requests. Key changes include loading the index from disk, querying the index with the diff text, and constructing prompts using relevant code context and PR information. The OpenAI model used for generating PR summaries has been switched to "gpt-4" and parameters for the completion process have been adjusted. A typo has also been corrected from 'marged' to 'merged'.

---

