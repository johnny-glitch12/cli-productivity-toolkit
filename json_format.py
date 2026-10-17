#!/usr/bin/env python3
"""Pretty-print and validate JSON files."""
import sys
import json

def format_json(path):
    try:
        with open(path) as f:
            data = json.load(f)
        print(json.dumps(data, indent=2))
    except json.JSONDecodeError as e:
        print(f"Invalid JSON: {e}")
        sys.exit(1)
    except FileNotFoundError:
        print(f"File not found: {path}")
        sys.exit(1)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python json_format.py <file.json>")
        sys.exit(1)
    format_json(sys.argv[1])
