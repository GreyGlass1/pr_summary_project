import shutil
from pathlib import Path
from llama_index.core import VectorStoreIndex, SimpleDirectoryReader
from config import PROJECT_ROOT, INDEX_DIR
from rich import print
from external_module_tracker import find_external_modules

VALID_EXTS = {".py", ".tf", ".md", ".txt", ".json", ".yaml", ".yml"}
EXCLUDE_DIRS = {".git", ".github", "__pycache__"}


def main():
    print("📁 Reading files and generating index...")

    # Ensure the index dir is fresh
    if INDEX_DIR.exists():
        print(f"🧹 Removing old index at: {INDEX_DIR}")
        shutil.rmtree(INDEX_DIR)

    # Build list of paths to index
    repo_paths = [PROJECT_ROOT]
    print(f"🔍 Scanning {PROJECT_ROOT} for external modules...")
    external_paths = find_external_modules(PROJECT_ROOT)
    print(f"🧩 Found {len(external_paths)} external module paths.")
    for mod_path in external_paths:
        print(f"🔗 Will index external module: {mod_path}")
    repo_paths.extend(Path(p) for p in external_paths)

    # Read all valid files
    documents = []
    for path in repo_paths:
        print(f"📄 Indexing: {path}")

        input_files = []
        for file in path.rglob("*"):
            if (
                file.is_file()
                and file.suffix in VALID_EXTS
                and not any(excl in file.parts for excl in EXCLUDE_DIRS)
            ):
                input_files.append(str(file))

        if not input_files:
            print(f"⚠️ No valid files found in {path}, skipping.")
            continue

        reader = SimpleDirectoryReader(input_files=input_files)
        docs = reader.load_data()
        documents.extend(docs)

    # Create new index
    index = VectorStoreIndex.from_documents(documents)
    print(f"📄 Indexing: {path}")
    index.storage_context.persist(persist_dir=INDEX_DIR)

    print("✅ Embedded entire repo and saved index.")


if __name__ == "__main__":
    main()
