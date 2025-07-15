# 🚀 Combined Release Summary for release-1.2.3

# Release Notes for Release-1.2.3

## Repository Update
The repository name in the `generate_release_notes.py` file has been updated from "GreyGlass1/test_repo" to "GreyGlass1/pr_summary_project".

## Embed Codebase Context for RAG
A script has been added to embed the project's source code into a Chroma vector store for semantic retrieval, which will be used for Retrieval Augmented Generation (RAG). The script collects all Python files from the project root excluding specific directories, writes them into a temporary folder and persists the resulting index for future use.

## No Context (Test)
Several changes have been made to the `generate_release_notes.py` script. These include loading an index from disk, querying the index with relevant context, constructing a prompt using code context and PR information, and calling OpenAI to generate a summary of the Pull Request. The OpenAI model used has been updated to `gpt-4`, and the temperature setting has been adjusted.

## PR Summarisation Tool Enhancements
The PR summarisation tool has been enhanced with centralized environment and config variable handling, detailed release notes generation for each tagged PR, and a single, context-aware summary across all included PRs using embedded codebase context and OpenAI. The tool now supports release-specific context and improved traceability of outputs. The Github token is now loaded from an environment variable, and the repository name is also configurable.

## Codebase Enhancements
Several structural modifications and improvements have been made to the codebase. The configuration has been extracted into a separate `config.py` file for better organization. All Python script files have been moved into a new `scripts` folder to enhance the project structure. The Chroma vector store has been extended to encompass the entire repository which improves the reach of the vector store.

## Potential Risks
The changes in this release involve significant modifications to the codebase structure and the PR summarisation tool. These changes may introduce unforeseen issues in the PR summarisation process or other parts of the codebase. The use of a new OpenAI model (`gpt-4`) and adjusted temperature setting may also affect the output of the PR summarisation tool.