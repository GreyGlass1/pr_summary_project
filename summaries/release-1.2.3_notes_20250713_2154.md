# 📝 Release Notes for release-1.2.3

### PR #1 - update repo
**Score** 100%
**Reason** High-quality PR with good metadata

The pull request titled "update repo" involves a change in the repository name within the `generate_release_notes.py` file. The repository name was updated from "GreyGlass1/test_repo" to "GreyGlass1/pr_summary_project". This change affects only one line of code.

---

### PR #2 - Embed codebase context for RAG
**Score** 100%
**Reason** High-quality PR with good metadata

Title: Embed codebase context for RAG

Summary: This pull request introduces a script that uses the LlamaIndex library to embed the project's source code into a Chroma vector store for semantic retrieval, specifically for Retrieval Augmented Generation (RAG). The script gathers all Python files from the project root, excluding certain directories, and writes them into a temporary folder. The OpenAI API Key is loaded from the .env file. The Chroma vector index is then saved.

---

### PR #3 - no context (test)
**Score** 100%
**Reason** High-quality PR with good metadata

Title: no context (test)

This pull request involves updates to the `generate_release_notes.py` script. The changes include loading an index from disk, querying the index with the diff text, constructing a prompt using code context and PR info, and calling OpenAI to generate a summary of the Pull Request. It also corrects a typo from 'marged' to 'merged'. The PR does not provide context or test for AI generator, hence the title 'no context (test)'.

---

### PR #4 - PR introduces configuration and output enhancements to the PR summarisation tool
**Score** 100%
**Reason** High-quality PR with good metadata

This pull request, titled "PR introduces configuration and output enhancements to the PR summarisation tool", implements several enhancements to a tool used for summarising Github pull requests. It introduces a centralised environment/config variable handling for improved maintainability in a new file named `config.py`, generates detailed release notes for each tagged PR stored under `summaries/` with timestamped filenames in `generate_release_notes.py`, and produces a single, context-aware summary across all included PRs using embedded codebase context and OpenAI in `generate_combined_summary.py`.

The changes made in `generate_release_notes.py` include introducing VectorStoreIndex and StorageContext from `llama_index.core`, querying the index with the diff, constructing a prompt using code context and PR info, and making a call to OpenAI for summarisation.

Additionally, a new file `config.py` has been added to handle environment/config variables and a new `summariser.py` file has been added but the detailed changes have not been shown in the provided diff.

These modifications aim to streamline the summary generation process, support release-specific context, and improve the traceability of outputs.

---

### PR #5 - enhancements
**Score** 100%
**Reason** High-quality PR with good metadata

Pull Request Title: enhancements

Summary: This pull request involves a restructuring of the project files. The existing `config.py` and `context_embed.py` scripts were deleted and recreated in a new `scripts` directory. The `generate_release_notes.py` and `summariser.py` scripts were also moved to this directory and renamed accordingly. Changes to the scripts include modifications to file paths and content. Additionally, the Chroma vector store has been extended to cover the entire repository.

---

### PR #6 - new score functionality
**Score** 80%
**Reason** PR description is missing or too short

This pull request, titled 'new score functionality', introduces a scoring system for pull requests in the `generate_release_notes.py` script. A new function `score_pr` has been added which scores a pull request out of 100 based on certain criteria such as whether the pull request has been merged, the length of its description, whether it has labels, and the nature of its title. The score, along with the reason for the score, is now displayed in the generated release notes for each pull request.

---

