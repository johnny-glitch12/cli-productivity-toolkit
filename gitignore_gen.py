#!/usr/bin/env python3
"""Generate common .gitignore templates."""
import sys

TEMPLATES = {
    "python": """__pycache__/
*.py[cod]
*$py.class
*.so
.Python
build/
develop-eggs/
dist/
downloads/
eggs/
.eggs/
lib/
lib64/
parts/
sdist/
var/
wheels/
*.egg-info/
.installed.cfg
*.egg
MANIFEST
.env
.venv
env/
venv/
ENV/
.idea/
.vscode/
""",
    "node": """node_modules/
npm-debug.log*
yarn-debug.log*
yarn-error.log*
.pnpm-debug.log*
.DS_Store
.env
.env.local
.env.*.local
dist/
build/
""",
    "general": """.DS_Store
Thumbs.db
*.log
.env
.idea/
.vscode/
"""
}

def generate(template_name):
    template = TEMPLATES.get(template_name.lower())
    if not template:
        print(f"Unknown template. Available: {', '.join(TEMPLATES.keys())}")
        return
    with open(".gitignore", "w") as f:
        f.write(template)
    print(f"Created .gitignore for {template_name}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python gitignore_gen.py <python|node|general>")
        sys.exit(1)
    generate(sys.argv[1])
