# 🚀 Combined Release Summary for release-1.2.3

# Release Notes for Version 1.2.3

## Repository Update
- The repository name has been updated in the `generate_release_notes.py` file. The old name "GreyGlass1/test_repo" has been changed to "GreyGlass1/pr_summary_project".

## Codebase Context Embedding for RAG
- A new script has been introduced that uses LlamaIndex to embed the project's source code into a Chroma vector store for semantic retrieval. This script gathers all Python files in the project, writes them into a temporary folder, and saves the index.

## PR Summarisation Tool Enhancements
- The `generate_release_notes.py` script has been updated to import additional modules, load an index from the disk, and query the index with the diff from the pull request. The construction of the prompt has been improved with the addition of a role "system" and adjustments to the max tokens and temperature parameters. The model used for the OpenAI call has been updated to "gpt-4".
- A typo in the print statement in the `fetch_prs` function has been fixed.
- The `config.py` file now handles environment/config variables, improving maintainability.
- The `generate_release_notes.py` file now generates detailed release notes for each tagged pull request. These notes are stored under 'summaries/' with timestamped filenames.
- A new feature has been added to produce a single, context-aware summary across all included PRs using embedded codebase context and OpenAI.

## Codebase Restructuring and Enhancements
- The scripts `config.py`, `context_embed.py`, `generate_release_notes.py`, and `summariser.py` have been moved into a new `scripts` directory.
- A separate `config.py` file has been created to handle the project's configuration.
- The Chroma vector store has been extended for the entire repository.

## New Scoring Functionality
- A new scoring functionality has been introduced for pull requests in the `generate_release_notes.py` script. A new function `score_pr` calculates a score out of 100 and provides a reason string based on specific PR characteristics. The score and reason are then displayed in the generated release notes.

## Potential Risks
- The introduction of new scripts and restructuring of the codebase may lead to unforeseen issues in the code execution.
- The new scoring functionality may not accurately reflect the quality of PRs, as it is based on specific characteristics that may not cover all aspects of a PR's quality.