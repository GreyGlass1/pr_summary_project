# 📝 Release Notes for release-1.2.3

### PR #1 - update repo
Pull Request Title: Update repo

Summary: This pull request is about updating the repository name in the `generate_release_notes.py` file. The old repository name "GreyGlass1/test_repo" has been replaced with the new one "GreyGlass1/pr_summary_project".

---

### PR #2 - Embed codebase context for RAG
Title: Embed codebase context for RAG

Summary:
A script has been added that uses LlamaIndex to embed the project's source code into a Chroma vector store for semantic retrieval, which will be used for Retrieval Augmented Generation (RAG). The script collects all Python files from the project root excluding specific directories, writes them into a temporary folder and persists the resulting index for future use. This change includes 37 new lines of code in the 'context_embed.py' file.

---

### PR #3 - no context (test)
This pull request, titled "no context (test)", introduces several changes to the `generate_release_notes.py` script. The updates include loading an index from disk, querying the index with relevant context, constructing a prompt using code context and PR information, and calling OpenAI to generate a summary of the Pull Request. 

Noteworthy changes in the diff include:
1. A new import from `llama_index.core` for `VectorStoreIndex`, `StorageContext`, and `load_index_from_storage`.
2. The introduction of a `StorageContext` and `load_index_from_storage` to load an index from disk.
3. A new query engine to query the index with the diff.
4. A restructured prompt format that includes the relevant code context along with the PR information.
5. Changes in the OpenAI call parameters, including using a different model ("gpt-4" instead of "gpt-3.5-turbo") and changing the temperature setting.

This pull request seems to be a part of the developer's efforts to improve the automated PR summarisation process.

---

### PR #4 - PR introduces configuration and output enhancements to the PR summarisation tool
This pull request introduces several enhancements to the PR summarisation tool. It centralises environment and config variable handling in `config.py` for improved maintainability, modifies `generate_release_notes.py` to generate detailed release notes for each tagged PR, and introduces `generate_combined_summary.py` to produce a single, context-aware summary across all included PRs using embedded codebase context and OpenAI. The changes also streamline summary generation, support release-specific context, and improve traceability of outputs.

In the code, the script now fetches and summarises pull requests, and then includes the relevant code context in the prompt used to call OpenAI. The script has been improved to load an index from disk, query the index with the diff, and use this context in the prompt. The OpenAI model used has been updated to `gpt-4`, and the temperature has been adjusted from 0.2 to 0.7 for more varied output. 

Other improvements include better handling of configuration through environment variables, the creation of a new `summariser.py` file, and the generation of individual and combined summaries of pull requests with a specific release tag. These summaries are saved to a specified directory with timestamped filenames for improved traceability. The Github token is now loaded from an environment variable, and the repository name is also configurable. 

The pull request includes two patches: one that introduces and tests the context-aware summarisation, and another that further enhances the script with the configuration and summary output improvements.

---

### PR #5 - enhancements
This pull request, titled "enhancements", contains several structural modifications and improvements to the codebase. First, the configuration was extracted into a separate `config.py` file for better organization. 

In addition, all Python script files were moved into a new `scripts` folder to enhance the project structure. The files affected by this change include `config.py`, `context_embed.py`, `generate_release_notes.py`, and `summariser.py`.

The Chroma vector store was extended to encompass the entire repository which improves the reach of the vector store.

In terms of file changes, there were 91 insertions and 64 deletions across 6 files. The `config.py` and `context_embed.py` scripts were deleted from the root directory and new versions were created in the `scripts` directory. The `generate_release_notes.py` and `summariser.py` scripts were moved to the `scripts` directory and renamed accordingly.

---

