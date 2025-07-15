# 🚀 Combined Release Summary for release-1.2.3

# Release Notes for Version 1.2.3

## Repository Update
The repository name in the `generate_release_notes.py` file has been updated. The new name is "GreyGlass1/pr_summary_project" (PR #1).

## Enhanced Codebase Context for RAG Model
A new script, `context_embed.py`, has been added to the codebase. This script uses LlamaIndex to embed the entire project's source code into a Chroma vector store for semantic retrieval. This enhancement provides a better context for the Retrieval-Augmented Generation (RAG) model (PR #2).

## Improved Release Notes Generation
Several enhancements have been made to the `generate_release_notes.py` script. The script now loads an index from disk, queries this index with the diff text, and constructs a prompt using the relevant code context and PR information. This prompt is then used in an OpenAI completion call to summarise the Pull Request. The model used in the OpenAI completion call has been updated from "gpt-3.5-turbo" to "gpt-4". The temperature parameter in the completion call has also been adjusted from 0.2 to 0.7, and max tokens set to 500 (PR #3).

## Potential Risks
The changes to the `generate_release_notes.py` script include an update to the model used in the OpenAI completion call. This update from "gpt-3.5-turbo" to "gpt-4" may impact the output of the script. Additionally, the adjustment of the temperature parameter in the completion call from 0.2 to 0.7 could result in more random output.