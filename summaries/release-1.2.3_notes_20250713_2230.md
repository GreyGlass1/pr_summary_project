# 📝 Release Notes for release-1.2.3

### PR #1 - update repo
**Score** 100%
**Reason** High-quality PR with good metadata

Pull Request Title: Update Repo

In this pull request, the repository name in the `generate_release_notes.py` file was updated. The previous repository name "GreyGlass1/test_repo" was changed to the new name "GreyGlass1/pr_summary_project".

---

### PR #2 - Embed codebase context for RAG
**Score** 100%
**Reason** High-quality PR with good metadata

Pull Request Title: Embed codebase context for RAG

Summary: This pull request involves the addition of a new Python script, `context_embed.py`, to embed the codebase into the Chroma vector index for Retrieval Augmented Generation (RAG). The script uses the LlamaIndex library to create a vector index from project Python files, excluding specified directories. The OpenAI API key is loaded from the .env file. The resulting vector index is saved for future use. This script will enhance semantic retrieval of the project source code.

---

### PR #3 - no context (test)
**Score** 100%
**Reason** High-quality PR with good metadata

The pull request titled "no context (test)" introduces significant updates to the `generate_release_notes.py` script. The updates include code for loading an index from disk, querying the index with the diff text, constructing a prompt using code context and PR info, and calling OpenAI to generate a summary of the pull request. The OpenAI model in use has been switched from "gpt-3.5-turbo" to "gpt-4". Additionally, the code has been adjusted to correct the spelling of "Marged" to "Merged". The changes result in 31 insertions and 10 deletions in the file.

---

### PR #4 - PR introduces configuration and output enhancements to the PR summarisation tool
**Score** 100%
**Reason** High-quality PR with good metadata

This Pull Request (PR) introduces configuration and output enhancements to a script that generates PR summaries for GitHub. 

The main changes include:

1. Centralized environment/config variable handling has been added for improved maintainability via `config.py`.
2. Detailed release notes for each tagged PR are now generated and stored under `summaries/` with timestamped filenames via `generate_release_notes.py`.
3. A single, context-aware summary across all included PRs is created using embedded codebase context and OpenAI via `generate_combined_summary.py`.

The changes made to `generate_release_notes.py` include the addition of indexing, querying, and prompt construction using code context and PR info. It also includes a change in the OpenAI model and the way messages are sent to the model. 

A new file, `config.py`, has been created to handle environment variables, and another new file, `summariser.py`, has been added, though its functionality is not described in the PR. 

The improvements aim to streamline summary generation, support release-specific context, and improve the traceability of outputs.

---

### PR #5 - enhancements
**Score** 100%
**Reason** High-quality PR with good metadata

Title: Enhancements

Summary:
The pull request involves refactoring and reorganising code files. The configuration was extracted into a separate `config.py` file, and all Python scripts were moved into a new `scripts` folder. This resulted in changes to file paths and the restructuring of the scripts. Additionally, the Chroma vector store was extended for the entire repository. The changes impacted six files, resulting in 91 insertions and 64 deletions.

---

### PR #6 - new score functionality
**Score** 80%
**Reason** PR description is missing or too short

Title: New Score Functionality

This pull request introduces a new functionality to score pull requests out of 100. The scoring is based on various PR attributes like merge status, description length, labels, and title. The score is accompanied by a reason string explaining the score.

Changes are made to the following files:

1. `scripts/generate_release_notes.py`: The code has been updated to fetch the score and reason of each PR. These details are added to the PR summary and printed on the console. 

2. `scripts/summariser.py`: A new function `score_pr(pr)` has been added. This function calculates the score and generates a reason string based on PR characteristics.

There are 44 insertions and 4 deletions across these two files.

---

