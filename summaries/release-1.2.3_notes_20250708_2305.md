# 📝 Release Notes for release-1.2.3

### PR #1 - update repo
The pull request titled "update repo" is about a change in the repository name within the file `generate_release_notes.py`. The previous name "GreyGlass1/test_repo" is replaced with the new name "GreyGlass1/pr_summary_project". The change is made by the user `teaton12`.

---

### PR #2 - Embed codebase context for RAG
Title: Embed codebase context for RAG

Summary: This pull request introduces a new script, `context_embed.py`, that uses the LlamaIndex library to embed the project's source code into a Chroma vector store. The purpose of this is to allow for semantic retrieval of the code. The script gathers all .py files from the project root, excluding specific directories, then writes the matching .py files into a temporary folder. The vector index is then created from these documents and saved.

---

### PR #3 - no context (test)
Pull Request Title: no context (test)

This pull request involves updates to the 'generate_release_notes.py' script. It includes loading the index from disk and querying this index using the diff text to gather relevant context. This context is then included in the prompt along with the Pull Request title, body, and diff text. This information is used to call OpenAI for summarization using the GPT-4 model with specific message roles and parameters. Other changes include minor updates such as the correction of a typo.

---

