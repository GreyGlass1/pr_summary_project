# 📝 Release Notes for release-1.2.3

### PR #1 - update repo
**Score** 100%
**Reason** High-quality PR with good metadata

Pull Request Title: Update Repo

This pull request changes the repository name in the `generate_release_notes.py` file. The old repo name was "GreyGlass1/test_repo", and it has been updated to "GreyGlass1/pr_summary_project".

---

### PR #2 - Embed codebase context for RAG
**Score** 100%
**Reason** High-quality PR with good metadata

Pull Request Title: Embed codebase context for RAG

This pull request introduces a new script that uses LlamaIndex to embed the project's source code into a Chroma vector store for semantic retrieval. The script first loads the OpenAI API Key from the .env file, then gathers all Python files in the project, excluding specific directories. The gathered files are written into a temporary folder. Finally, the script saves the index. The PR includes the addition of 37 lines of code in a new file called 'context_embed.py'.

---

### PR #3 - no context (test)
**Score** 100%
**Reason** High-quality PR with good metadata

The pull request titled "no context (test)" involves modifications to the `generate_release_notes.py` script. The changes include the importation of additional modules, loading an index from the disk, querying the index with the diff from the pull request, constructing a prompt using the code context and pull request information, and calling OpenAI to generate a summary of the pull request. The model used for the OpenAI call has been updated to "gpt-4". The update also includes changes in the construction of the prompt, with the addition of a role "system", and adjustments to the max tokens and temperature parameters. A typo in the print statement in the `fetch_prs` function that previously printed "Marged" has been fixed to "Merged". The changes resulted in 31 insertions and 10 deletions.

---

### PR #4 - PR introduces configuration and output enhancements to the PR summarisation tool
**Score** 100%
**Reason** High-quality PR with good metadata

This pull request, titled "PR introduces configuration and output enhancements to the PR summarisation tool," introduces various enhancements to a script that generates release notes for GitHub pull requests. 

Key changes include:

1. Configuration centralisation: The `config.py` file now handles environment/config variables, improving maintainability.
2. Detailed release notes: The `generate_release_notes.py` file has been updated to generate detailed release notes for each tagged pull request. These notes are stored under 'summaries/' with timestamped filenames.
3. Combined summary generation: A new feature has been added by `generate_combined_summary.py` to produce a single, context-aware summary across all included PRs using embedded codebase context and OpenAI.

Moreover, the script now includes an indexing feature to fetch relevant code context for each PR. This ensures that the summaries are context-aware. The script also uses OpenAI's GPT-4 model for generating summaries. 

The overall changes are expected to streamline summary generation, support release-specific context, and improve the traceability of outputs.

---

### PR #5 - enhancements
**Score** 100%
**Reason** High-quality PR with good metadata

Title: Enhancements

Summary: This pull request involves restructuring of the codebase and enhancements. The scripts `config.py`, `context_embed.py`, `generate_release_notes.py` and `summariser.py` were moved into a new `scripts` directory. A separate `config.py` file was created to handle the project's configuration. The Chroma vector store has also been extended for the entire repository. The changes resulted in 91 insertions and 64 deletions.

---

### PR #6 - new score functionality
**Score** 80%
**Reason** PR description is missing or too short

Title: new score functionality

This pull request introduces a new scoring functionality for pull requests in the `generate_release_notes.py` script. A new function `score_pr` calculates a score out of 100 and provides a reason string based on specific PR characteristics. The score and reason are then displayed in the generated release notes. The `score_pr` function deducts points for various factors such as the PR not being merged, having a missing or short description, lacking labels, or having a too generic title. If a PR scores 90 or above, it's considered high-quality. The changes involve 44 insertions and 4 deletions across two files: `generate_release_notes.py` and `summariser.py`.

---

