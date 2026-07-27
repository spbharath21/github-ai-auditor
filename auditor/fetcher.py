#Fetches file contents from a GitHub repository via the GitHub API.

import os
from collections import deque
from dataclasses import dataclass
from pathlib import Path

from github import Github, Auth
from dotenv import load_dotenv

load_dotenv()

ALLOWED_EXTENSIONS = {
    ".py", ".js", ".ts", ".jsx", ".tsx",
    ".java", ".go", ".cpp", ".c", ".cs",
    ".php", ".rb", ".yaml", ".yml", ".env",
}

SKIP_DIRS = {"node_modules", ".git", "venv", "__pycache__", "dist", "build", ".next"}
MAX_FILE_SIZE_BYTES = 1_000_000


@dataclass
class RepoFile:
    path: str
    content: str
    size_bytes: int = 0


def is_code_file(path: str) -> bool:
    return Path(path).suffix.lower() in ALLOWED_EXTENSIONS


def get_file_content(file) -> str | None:
    try:
        return file.decoded_content.decode("utf-8", errors="ignore")
    except Exception:
        return None


def collect_repository_files(repo_name: str, max_files: int = 0) -> list[RepoFile]:
    token = os.getenv("GITHUB_TOKEN")
    if not token:
        raise RuntimeError("GITHUB_TOKEN not set. Check your .env file.")

    if repo_name.startswith("http"):
        repo_name = repo_name.rstrip("/").rstrip(".git")
        repo_name = "/".join(repo_name.split("/")[-2:])

    g = Github(auth=Auth.Token(token))
    repo = g.get_repo(repo_name)

    repository_files: list[RepoFile] = []
    queue = deque(repo.get_contents(""))

    while queue:
        item = queue.pop()

        if item.type == "dir":
            if item.name not in SKIP_DIRS:
                queue.extend(repo.get_contents(item.path))
            continue

        if not is_code_file(item.path):
            continue

        if item.size > MAX_FILE_SIZE_BYTES:
            continue

        content = get_file_content(item)
        if content is None:
            continue

        if max_files and len(repository_files) >= max_files:
            break

        repository_files.append(
            RepoFile(path=item.path, content=content, size_bytes=item.size)
        )

    return repository_files