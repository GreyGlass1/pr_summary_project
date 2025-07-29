import os
from openai import OpenAI
from dotenv import load_dotenv
from pathlib import Path

# Load variables from .env
load_dotenv()

# --- Tokens and API keys ---
GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
REPO_NAME = os.getenv("REPO_NAME")  # e.g., 'your-org/your-repo'

# --- Project Paths ---
SCRIPT_DIR = Path(__file__).resolve().parent         # path/to/pr_summary_project/scripts
PROJECT_ROOT = SCRIPT_DIR.parent                     # path/to/pr_summary_project
SUMMARY_DIR = PROJECT_ROOT / "summaries"
INDEX_DIR = PROJECT_ROOT / "index"                   # llama_index will persist here
TEMP_CODE_DIR = PROJECT_ROOT / "codebase"            # optional: used if copying files temporarily
CONTEXT_DIR = PROJECT_ROOT / "context_logs"      # path/to/pr_summary_project/context_logs
# --- Confluence (for future use) ---
CONFLUENCE_BASE_URL = os.getenv("CONFLUENCE_BASE_URL", "")
CONFLUENCE_API_TOKEN = os.getenv("CONFLUENCE_API_TOKEN", "")
CONFLUENCE_USERNAME = os.getenv("CONFLUENCE_USERNAME", "")

# --- Release Tag (optional default) ---
DEFAULT_RELEASE_TAG = os.getenv("DEFAULT_RELEASE_TAG", "release-1.2.3")

# --- Create folders if needed ---
os.makedirs(SUMMARY_DIR, exist_ok=True)
os.makedirs(INDEX_DIR, exist_ok=True)
os.makedirs(CONTEXT_DIR, exist_ok=True)

# --- Directories to skip during indexing ---
EXCLUDED_DIRS = [".git", ".venv", "node_modules", "__pycache__", "index", "codebase"]

# --- Relevant Context Paths ---
