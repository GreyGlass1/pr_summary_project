# 📝 Release Notes for release-1.2.3

### PR #1 - update repo
**Score** 100%
**Reason** High-quality PR with good metadata

Pull Request Title: Update Repo

Summary: The pull request involves a change in the repository name within the `generate_release_notes.py` file. The repository name has been updated from "GreyGlass1/test_repo" to "GreyGlass1/pr_summary_project".

---

### PR #2 - Embed codebase context for RAG
**Score** 100%
**Reason** High-quality PR with good metadata

Pull Request Title: Embed codebase context for RAG

Summary: 
This pull request adds a script (`context_embed.py`) that uses LlamaIndex to semantically embed the project's source code into a Chroma vector store for Retrieval Augmented Generation (RAG). The script loads the OpenAI API key from the `.env` file, gathers Python files from the project root, excluding certain directories, writes them into a temporary folder, and then saves the index. The patch includes 37 new lines of code, all within the new script file.

---

### PR #3 - no context (test)
**Score** 100%
**Reason** High-quality PR with good metadata

The pull request titled "no context (test)" involves updates to the script `generate_release_notes.py`. The changes include:

1. Code for loading an index from disk.
2. Querying the index with the diff text.
3. Constructing a prompt using the code context and PR information.
4. Calling OpenAI to generate a summary of the pull request.

The changes also involve a minor correction of print statement from "Marged" to "Merged". The OpenAI model used is changed from "gpt-3.5-turbo" to "gpt-4". Improvements have also been made to how prompts are constructed and presented. The pull request overall enhances the script's ability to generate more precise summaries of pull requests.

---

### PR #4 - PR introduces configuration and output enhancements to the PR summarisation tool
**Score** 100%
**Reason** High-quality PR with good metadata

This pull request, titled "PR introduces configuration and output enhancements to the PR summarisation tool", brings several enhancements to the PR summarisation tool. 

The changes include:
1. A new `config.py` which centralises environment/config variable handling for better maintainability.
2. An update to `generate_release_notes.py` to generate detailed release notes for each tagged PR. These notes are stored under the `summaries/` directory with timestamped filenames.
3. The addition of `generate_combined_summary.py`, a script that produces a single, context-aware summary across all included PRs using the embedded codebase context and OpenAI.

The pull request also modifies the existing scripts to streamline summary generation, support release-specific context, and improve traceability of outputs.

The changes in the code include:
1. Loading an index from the disk and querying it with the diff to get the relevant context.
2. Creating a prompt using code context and PR info.
3. Changing the parameters for the call to OpenAI.
4. Creating a new `config.py` file.
5. Modifying `generate_release_notes.py` to include timestamps and file paths for the notes and summaries.
6. Creating a new `summariser.py` file. 

These changes will significantly improve the functionality and usability of the PR summarisation tool.

---

### PR #5 - enhancements
**Score** 100%
**Reason** High-quality PR with good metadata

This Pull Request, titled "enhancements", includes changes to the structure and functionality of the project. The configuration was extracted into a separate `config.py` file, and the python scripts were moved into a new `scripts` folder. A new functionality was added to the `context_embed.py` script, which can now read files and generate an index for the entire repository. The `config.py` and `context_embed.py` scripts in the root directory were deleted, and new versions were created within the `scripts` directory. The `generate_release_notes.py` script was also moved to the `scripts` directory. Consequently, 91 lines of code were added, and 64 lines were removed in this Pull Request.

---

### PR #6 - new score functionality
**Score** 80%
**Reason** PR description is missing or too short

Pull Request Title: new score functionality

This pull request introduces a new functionality that calculates a score out of 100 for each pull request based on specific characteristics of the PR such as whether it has been merged, the length and content of the PR body, the presence of labels, and the title of the PR. The score and a reason string explaining the scoring are displayed. The changes involve 44 insertions and 4 deletions across two files: `scripts/generate_release_notes.py` and `scripts/summariser.py`.

---

