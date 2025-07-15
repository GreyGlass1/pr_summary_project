# 📝 Release Notes for release-1.2.3

### PR #1 - update repo
**Score** 100%
**Reason** High-quality PR with good metadata

Pull Request Title: update repo

Summary: This pull request updates the repository name in the `generate_release_notes.py` file. Specifically, the name changes from "GreyGlass1/test_repo" to "GreyGlass1/pr_summary_project".

---

### PR #2 - Embed codebase context for RAG
**Score** 100%
**Reason** High-quality PR with good metadata

Title: Embed codebase context for RAG

This pull request introduces a new script that embeds the project's source code into a Chroma vector store for semantic retrieval, using the LlamaIndex library. The script loads the OpenAI API Key from the .env file, collects Python files from the project's root directory (excluding certain specified directories), writes them into a temporary folder, and saves the index in the index folder. The intent is to use this for Retrieval Augmented Generation (RAG). The changes involve 37 new lines of code added to a new file named `context_embed.py`.

---

### PR #3 - no context (test)
**Score** 100%
**Reason** High-quality PR with good metadata

The pull request titled "no context (test)" introduces significant updates to the `generate_release_notes.py` script. The changes allow for loading an index from disk, querying this index with the diff text, constructing a prompt using the code context and PR info, and calling OpenAI to generate a summary of the pull request. It switches from using the "gpt-3.5-turbo" to the "gpt-4" model for OpenAI, with specific parameters for completion. A typo in the output message has also been corrected.

---

### PR #4 - PR introduces configuration and output enhancements to the PR summarisation tool
**Score** 100%
**Reason** High-quality PR with good metadata

This pull request introduces enhanced configuration and output features to a tool that generates summaries for GitHub pull requests. The updates include:

1. `config.py` - a file for centralized environment and configuration variable management for easier maintainability.
2. `generate_release_notes.py` - a script that now generates detailed release notes for each tagged PR, which are stored under a 'summaries/' directory with timestamped filenames.
3. `generate_combined_summary.py` - a new script that creates a single, context-aware summary across all included PRs using both embedded codebase context and OpenAI.

The modifications also improve the tool's traceability of outputs and allow for more streamlined summary generation. Furthermore, they support release-specific context.

The changes to `generate_release_notes.py` include:
- Improved error handling for the case when the 'diff' for a pull request is too large.
- The script now loads an index from disk and uses it to query the 'diff' to provide relevant code context.
- The prompt for the OpenAI model is now constructed using the code context and PR info.
- The OpenAI model used has been upgraded from 'gpt-3.5-turbo' to 'gpt-4'.
- The 'max_tokens' parameter for the OpenAI model call has been set to 500, and the 'temperature' parameter has been updated from 0.2 to 0.7.

The new `config.py` file sets up the OpenAI client with the API key from the environment variables.

In the second patch, the `generate_release_notes.py` script is further updated to use the 'REPO_NAME' from the environment variables and to make a directory for storing summaries. It also includes changes to the 'main' function to write individual and combined summaries for each tagged PR.

Overall, these updates aim to enhance the functionality of the PR summarization tool.

---

### PR #5 - enhancements
**Score** 100%
**Reason** High-quality PR with good metadata

This pull request, titled "enhancements", primarily focuses on reorganising the codebase and introducing new functionalities. Major changes include:

1. The extraction of configurations into a separate `config.py` file.
2. The movement of all Python scripts into a new `scripts` folder. This includes the `config.py`, `context_embed.py`, and `generate_release_notes.py` files.
3. The extension of Chroma vector store for the entire repository.

In terms of code changes, a total of 91 insertions and 64 deletions were made across 6 files. The old `config.py` and `context_embed.py` files were deleted, and new versions were created in the `scripts` directory. The `generate_release_notes.py` script was also renamed and moved to the `scripts` directory. Modifications were made to the scripts for added functionalities and updates.

---

