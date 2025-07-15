# 🚀 Combined Release Summary for release-1.2.3

# Release Notes for Version 1.2.3

## Changes

### Repository Update
- The repository name was updated from "GreyGlass1/test_repo" to "GreyGlass1/pr_summary_project" in the `generate_release_notes.py` script.

### Embed Codebase Context for RAG
- A new script was introduced to embed the project's source code into a Chroma vector store for semantic retrieval, specifically for Retrieval Augmented Generation (RAG). This script uses the LlamaIndex library and gathers all Python files from the project root, excluding certain directories.

### PR Summarisation Tool Enhancements
- The `generate_release_notes.py` script has been updated to include a new scoring system for pull requests. The score is based on certain criteria such as whether the pull request has been merged, the length of its description, whether it has labels, and the nature of its title.
- A new `config.py` file has been introduced to handle environment/config variables. This centralises environment/config variable handling for improved maintainability.
- The `generate_release_notes.py` script now generates detailed release notes for each tagged PR stored under `summaries/` with timestamped filenames. It also produces a single, context-aware summary across all included PRs using embedded codebase context and OpenAI.
- A new `summariser.py` file has been added.

### Project Restructuring
- The project files have been restructured. The existing `config.py` and `context_embed.py` scripts were deleted and recreated in a new `scripts` directory. The `generate_release_notes.py` and `summariser.py` scripts were also moved to this directory and renamed accordingly.
- The Chroma vector store has been extended to cover the entire repository.

## Potential Risks
- The restructuring of the project files and the renaming of the repository may cause issues with existing references or dependencies. Please update any references accordingly.
- The new scoring system for pull requests may not accurately reflect the importance or quality of a pull request based on the chosen criteria. This scoring system should be reviewed and adjusted as necessary.