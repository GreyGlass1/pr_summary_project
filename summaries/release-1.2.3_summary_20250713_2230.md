# 🚀 Combined Release Summary for release-1.2.3

# Release Notes for Release-1.2.3

## Update Repo
The repository name in the `generate_release_notes.py` file has been updated from "GreyGlass1/test_repo" to "GreyGlass1/pr_summary_project".

## Embed Codebase Context for RAG
A new Python script, `context_embed.py`, has been added to embed the codebase into the Chroma vector index for Retrieval Augmented Generation (RAG). The script uses the LlamaIndex library to create a vector index from project Python files, excluding specified directories. The OpenAI API key is loaded from the .env file. The resulting vector index is saved for future use.

## No Context (Test)
Significant updates have been made to the `generate_release_notes.py` script. These updates include loading an index from disk, querying the index with the diff text, constructing a prompt using code context and PR info, and calling OpenAI to generate a summary of the pull request. The OpenAI model has been switched from "gpt-3.5-turbo" to "gpt-4". 

## PR Summarisation Tool Enhancements
Configuration and output enhancements have been introduced to the PR summarisation tool. This includes centralized environment/config variable handling via `config.py`, detailed release notes for each tagged PR stored under `summaries/` with timestamped filenames, and a single, context-aware summary across all included PRs created using embedded codebase context and OpenAI. 

## Codebase Enhancements
The codebase has been refactored and reorganised. The configuration was extracted into a separate `config.py` file, and all Python scripts were moved into a new `scripts` folder. Additionally, the Chroma vector store was extended for the entire repository.

## New Score Functionality
A new functionality to score pull requests out of 100 has been introduced. The scoring is based on various PR attributes like merge status, description length, labels, and title. The score and the reason for the score are fetched and added to the PR summary.

## Potential Risks
The switch from "gpt-3.5-turbo" to "gpt-4" in the `generate_release_notes.py` script may have an impact on the performance or output of the script. The refactoring and reorganisation of the codebase may also affect the functioning of the scripts if the file paths are not updated correctly. The new score functionality introduces changes to the `scripts/generate_release_notes.py` and `scripts/summariser.py` files, which could potentially introduce bugs if not implemented correctly.