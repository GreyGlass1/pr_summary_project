import os
from llama_index.core import SimpleDirectoryReader, VectorStoreIndex
from dotenv import load_dotenv

#Load .env for OpenAI API Key
load_dotenv()

# Get the absolute path of the project root (one folder up from this script)
PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))

# Exclude folders you don't want indexed
EXCLUDED_DIRS = {"venv", "index", ".git", ".vscode"}

# Gather all .py files from the project root, excluding specified dirs
def get_python_files(root_dir):
    python_files = []
    for root, dirs, files in os.walk(root_dir):
        # Skip excluded folders
        dirs[:] = [d for d in dirs if d not in EXCLUDED_DIRS]

        for file in files:
            if file.endswith(".py"):
                python_files.append(os.path.join(root, file))
    return python_files

# Write matching .py files into a temporary folder
TEMP_INPUT_DIR = os.path.join(PROJECT_ROOT, "codebase")
os.makedirs(TEMP_INPUT_DIR, exist_ok=True)

# Symlink or copy (optional, to use with SimpleDirectoryReader)
# But LlamaIndex also supports reading from raw paths
documents = SimpleDirectoryReader(input_files=get_python_files(PROJECT_ROOT)).load_data()

index = VectorStoreIndex.from_documents(documents)
index.storage_context.persist(persist_dir=os.path.join(PROJECT_ROOT, "index"))

print("✅ Embedded codebase and saved index.")