#!/usr/bin/env python3
"""Organize files in a directory by their extension."""
import os
import sys
import shutil
from pathlib import Path

def organize(directory):
    directory = Path(directory)
    if not directory.is_dir():
        print(f"Error: {directory} is not a directory")
        return

    for item in directory.iterdir():
        if item.is_file():
            ext = item.suffix.lower() or "no_extension"
            target_dir = directory / ext.lstrip(".")
            target_dir.mkdir(exist_ok=True)
            shutil.move(str(item), str(target_dir / item.name))
            print(f"Moved {item.name} → {target_dir.name}/")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python organize.py <directory>")
        sys.exit(1)
    organize(sys.argv[1])
