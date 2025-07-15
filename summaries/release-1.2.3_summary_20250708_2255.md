# 🚀 Combined Release Summary for release-1.2.3

# Release Notes for Version 1.2.3

## Update Repo
The repository name has been updated in the `generate_release_notes.py` file. The new repository name is "GreyGlass1/pr_summary_project".

## Embed Codebase Context for RAG
A new Python script, `context_embed.py`, has been added to the project. This script uses the LlamaIndex to embed the project's source code into a Chroma vector store for semantic retrieval. The script scans the project root for Python files, excluding certain directories (`venv`, `index`, `.git`, `.vscode`), and writes these files into a temporary folder. A VectorStoreIndex is then created from these documents and persisted in the 'index' subdirectory of the project root.

## No Context (Test)
The `generate_release_notes.py` script has been significantly updated to enhance the process of summarizing pull requests. Key changes include loading the index from disk, querying the index with the diff text, and constructing prompts using relevant code context and PR information. The OpenAI model used for generating PR summaries has been switched to "gpt-4" and parameters for the completion process have been adjusted. A typo has been corrected from 'marged' to 'merged'.

# Potential Risks
The change in the OpenAI model used for generating PR summaries to "gpt-4" may lead to differences in the output. The adjustment of parameters for the completion process may also affect the results. Users are advised to review the new summaries carefully.