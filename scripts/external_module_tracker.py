import os
import re
import json
import subprocess
from pathlib import Path
from urllib.parse import urlparse
from typing import List, Tuple
from config import PROJECT_ROOT

# === CONFIG ===
EXTERNAL_MODULES_DIR = PROJECT_ROOT / ".external_modules"
MODULE_TAG_CACHE_FILE = EXTERNAL_MODULES_DIR / "module_tags.json"

# Ensure the external modules directory exists
EXTERNAL_MODULES_DIR.mkdir(exist_ok=True, parents=True)

# === TAG CACHE ===
def load_module_tag_cache():
    if MODULE_TAG_CACHE_FILE.exists():
        with open(MODULE_TAG_CACHE_FILE, "r") as f:
            return json.load(f)
    return {}

def save_module_tag_cache(cache):
    with open(MODULE_TAG_CACHE_FILE, "w") as f:
        json.dump(cache, f, indent=2)

# === TF PARSING ===
def parse_tf_for_modules(tf_dir: Path) -> List[Tuple[str, str]]:
    module_sources = []

    # Improved regex: supports single/double quotes, spaces, optional `.git`
    pattern = re.compile(r'source\s*=\s*[\'"]git::(.*?)\?ref=([^\'"]+)[\'"]')

    print(f"🔍 Scanning for .tf files in: {tf_dir}")
    for tf_file in tf_dir.rglob("*.tf"):
        print(f"📁 Checking: {tf_file}")
        try:
            with open(tf_file, "r", encoding="utf-8") as f:
                content = f.read()
                matches = pattern.findall(content)
                for repo_url, ref in matches:
                    print(f"🔗 Matched: {repo_url} @ {ref}")
                    module_sources.append((repo_url, ref))
        except Exception as e:
            print(f"⚠️ Failed to read {tf_file}: {e}")

    return module_sources

# === SLUGIFY PATH ===
def slugify_repo_tag(repo_url: str, tag: str) -> str:
    parsed = urlparse(repo_url)
    path = parsed.path.strip("/").replace("/", "_").replace(".git", "")
    return f"{path}_{tag}"

# === GIT CLONE ===
def clone_module(repo_url: str, tag: str, target_dir: Path):
    print(f"\n📦 Cloning {repo_url}@{tag} to {target_dir}...")
    subprocess.run([
        "git", "clone", "--depth", "1", "--branch", tag, repo_url, str(target_dir)
    ], check=True)

# === MAIN ENTRY ===
def find_external_modules(codebase_dir: Path) -> List[Path]:
    embedded_paths = []
    tag_cache = load_module_tag_cache()

    modules = parse_tf_for_modules(codebase_dir)
    print(f"📄 Found {len(modules)} external module reference(s).")

    for repo_url, tag in modules:
        slug = slugify_repo_tag(repo_url, tag)
        local_path = EXTERNAL_MODULES_DIR / slug
        previous_tag = tag_cache.get(repo_url)

        if previous_tag != tag or not local_path.exists():
            if local_path.exists():
                print(f"🧹 Removing outdated module: {local_path}")
                subprocess.run(["rm", "-rf", str(local_path)])

            try:
                clone_module(repo_url, tag, local_path)
                tag_cache[repo_url] = tag
            except subprocess.CalledProcessError as e:
                print(f"❌ Failed to clone {repo_url}@{tag}: {e}")
                continue
        else:
            print(f"✅ Module already present: {repo_url}@{tag}")

        embedded_paths.append(local_path)

    save_module_tag_cache(tag_cache)
    return embedded_paths

# === TEST ENTRY ===
if __name__ == "__main__":
    print("🧪 Running external module tracker directly...\n")
    paths = find_external_modules(PROJECT_ROOT)
    print(f"\n✅ Discovered {len(paths)} module(s) to embed:")
    for p in paths:
        print(f"  - {p}")
