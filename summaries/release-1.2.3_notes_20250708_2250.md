# 📝 Release Notes for release-1.2.3

### PR #3 - no context (test)
Pull Request Title: Update repo

This pull request updates the repository name in the `generate_release_notes.py` file. The name has been changed from "GreyGlass1/test_repo" to "GreyGlass1/pr_summary_project".

---

### PR #3 - no context (test)
Title: Embed codebase context for RAG

Summary: This pull request adds a new script `context_embed.py` which uses LlamaIndex to embed the entire project's source code into a Chroma vector store for semantic retrieval. The script works by gathering all Python files from the project root (excluding specified directories), and then writes these into a temporary folder. The embedded codebase and index are then saved. This enhancement aims to provide a better context for the RAG (Retrieval-Augmented Generation) model.

---

### PR #3 - no context (test)
Title: no context (test)

The pull request introduces several enhancements to the `generate_release_notes.py` script. The main changes include loading an index from disk, querying this index with the diff text, and constructing a prompt using the relevant code context and PR information. This prompt is then used in an OpenAI completion call to summarise the Pull Request. In addition, there are corrections to typos and the model used in the OpenAI completion call has been updated from "gpt-3.5-turbo" to "gpt-4". The temperature parameter in the completion call has also been adjusted from 0.2 to 0.7, and max tokens set to 500.

---

