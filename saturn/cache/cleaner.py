from pathlib import Path
import shutil


def clear_cache() -> tuple[int, int]:
    root = Path.cwd()

    deleted_dirs = 0
    deleted_files = 0

    for path in root.rglob("__pycache__"):
        if path.is_dir():
            shutil.rmtree(path)
            deleted_dirs += 1

    for path in root.rglob("*.pyc"):
        if path.is_file():
            path.unlink()
            deleted_files += 1

    return deleted_dirs, deleted_files