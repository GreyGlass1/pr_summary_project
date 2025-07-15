# 📝 Release Notes for release-1.2.3

### PR #1 - update repo
Pull Request Title: update repo

Pull Request Summary: The pull request involves a change in the `generate_release_notes.py` file where the repository name was updated. The previous repository name "GreyGlass1/test_repo" was replaced with the new repository name "GreyGlass1/pr_summary_project".

---

### PR #2 - Embed codebase context for RAG
Title: Embed codebase context for RAG

Summary: A new script was added to the project that uses LlamaIndex to embed the project's source code into a Chroma vector store for semantic retrieval. This is done as part of the Retrieval Augmented Generation (RAG) process. The script identifies all Python files in the project, excluding specified directories, and stores this data into a temporary folder. This data is then embedded into the Chroma vector index and saved.

---

### PR #3 - no context (test)
Pull Request Title: no context (test)

The pull request includes updates to the `generate_release_notes.py` script. The changes involve loading an index from disk, querying the index with relevant context, constructing a prompt using code context and PR information, and calling OpenAI to generate a summary of the pull request. 

The key modifications in the pull request include:

1. The addition of `load_index_from_storage` from `llama_index.core` to load an index from disk.
2. The creation of a `StorageContext` to define the storage directory for the index.
3. The use of a query engine to query the index with the diff text.
4. The construction of a prompt using the relevant code context and PR info.
5. The call to OpenAI's GPT-4 model to generate a summary of the pull request.

Other minor changes include the correction of a typo ('Marged' to 'Merged') and the adjustment of parameters in the call to the OpenAI model.

---

### PR #4 - PR introduces configuration and output enhancements to the PR summarisation tool
The pull request titled "PR introduces configuration and output enhancements to the PR summarisation tool" includes updates to the script that generates release notes for GitHub pull requests. 

The enhancements include:

1. A new `config.py` file for centralised environment/config variable handling to improve maintainability.
2. Updates to `generate_release_notes.py` to generate detailed release notes for each tagged PR, stored under `summaries/` with timestamped filenames.
3. The introduction of `generate_combined_summary.py` that produces a single, context-aware summary across all included PRs using embedded codebase context and OpenAI.

The changes made in the code include:
- The introduction of `VectorStoreIndex` and `StorageContext` from `llama_index.core` in the `generate_release_notes.py` to load the index from disk and query the index with the diff text.
- The prompt used for OpenAI completions was updated to include the relevant code context along with the PR information. 
- The OpenAI model used for completion was updated from `gpt-3.5-turbo` to `gpt-4`, and the max tokens was increased from an unspecified number to 500.
- A new file `config.py` was created, which loads environment variables and initializes the OpenAI client.
- Several changes were made to `generate_release_notes.py`, including the use of the `datetime` module for timestamps, use of environment variables, creation of a directory for summaries, and calling the `summarise_pr()` function for each PR to create individual summaries.
- The `generate_combined_release_summary` function from `summariser.py` was also introduced.

These changes improve the summary generation process, provide release-specific context, and enhance the traceability of outputs.

---

