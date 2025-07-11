import shutil
import os
from llama_index.core import VectorStoreIndex, SimpleDirectoryReader
from config import PROJECT_ROOT, INDEX_DIR
from rich import print

def main():
    print("🗂️  Reading files and generating index...")

    # Ensure the index dir is fresh
    if INDEX_DIR.exists():
        print(f"🧹 Removing old index at: {INDEX_DIR}")
        shutil.rmtree(INDEX_DIR)

    # Read entire project (excluding EXCLUDED_DIRS if needed)
    documents = SimpleDirectoryReader(input_dir=str(PROJECT_ROOT)).load_data()

    # Create new index
    index = VectorStoreIndex.from_documents(documents)
    index.storage_context.persist(persist_dir=INDEX_DIR)

    print("✅ Embedded entire repo and saved index.")

if __name__ == "__main__":
    main()