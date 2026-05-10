#!/usr/bin/env python3
"""
build_release_zip.py — Đóng gói skill thành zip ready-to-upload cho claude.ai / Claude Desktop.

Loại trừ dev/CI junk (.git, plans/, examples/, .github/, uv.lock, ...) để zip nhỏ và sạch.
Folder gốc trong zip phải tên `ces-second-brain` để khớp `name` trong SKILL.md.

Output: dist/ces-second-brain.zip

Cách chạy:
    python scripts/build_release_zip.py
"""

from __future__ import annotations
from pathlib import Path
import zipfile
import sys

SKILL_NAME = "ces-second-brain"

# Patterns to exclude (relative to repo root, glob-style — checked via Path.match)
EXCLUDE_DIRS = {
    ".git",
    ".github",
    ".venv",
    "__pycache__",
    "node_modules",
    "plans",
    "dist",
    "scripts",  # build_release_zip.py is dev-only, no need in distributed skill
}

EXCLUDE_FILES = {
    ".gitignore",
    ".gitattributes",
    "uv.lock",
    "CONTRIBUTING.md",
    "CODE_OF_CONDUCT.md",
    "SECURITY.md",
    "CHANGELOG.md",
    ".env.example",
    "build_release_zip.py",  # script itself, no need in skill bundle
}

EXCLUDE_SUFFIXES = {".pyc", ".pyo", ".log", ".local", ".DS_Store"}


def should_skip(path: Path, repo_root: Path) -> bool:
    """Return True if path should NOT go into the zip."""
    rel = path.relative_to(repo_root)
    # Top-level dir filter
    if rel.parts and rel.parts[0] in EXCLUDE_DIRS:
        return True
    # Any segment matches an exclude dir
    if any(part in EXCLUDE_DIRS for part in rel.parts):
        return True
    if path.is_file():
        if path.name in EXCLUDE_FILES:
            return True
        if path.suffix in EXCLUDE_SUFFIXES:
            return True
    return False


def main() -> int:
    repo_root = Path(__file__).resolve().parent.parent

    skill_md = repo_root / "SKILL.md"
    if not skill_md.exists():
        print(f"ERROR: SKILL.md not found at {skill_md}", file=sys.stderr)
        return 1

    dist_dir = repo_root / "dist"
    dist_dir.mkdir(exist_ok=True)
    zip_path = dist_dir / f"{SKILL_NAME}.zip"

    if zip_path.exists():
        zip_path.unlink()

    print(f"Building {zip_path}...")

    file_count = 0
    total_bytes = 0

    with zipfile.ZipFile(zip_path, "w", zipfile.ZIP_DEFLATED, compresslevel=6) as zf:
        for path in sorted(repo_root.rglob("*")):
            if not path.is_file():
                continue
            if should_skip(path, repo_root):
                continue
            rel = path.relative_to(repo_root)
            # Prefix with skill folder name so unzipped folder matches SKILL.md `name`
            arcname = Path(SKILL_NAME) / rel
            zf.write(path, arcname=arcname)
            file_count += 1
            total_bytes += path.stat().st_size

    size_mb = zip_path.stat().st_size / (1024 * 1024)
    print(f"  Files included:     {file_count}")
    print(f"  Total uncompressed: {total_bytes / (1024 * 1024):.2f} MB")
    print(f"  Zip size:           {size_mb:.2f} MB")
    print()
    print(f"Done: {zip_path}")
    print()
    print("Cách dùng:")
    print(f"  1. Mở Claude Desktop / claude.ai")
    print(f"  2. Settings -> Capabilities -> Skills -> Upload skill")
    print(f"  3. Chọn file: {zip_path}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
