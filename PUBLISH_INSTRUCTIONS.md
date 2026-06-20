# 📖 AI AGENT GITHUB PUBLISHING PROTOCOL

> [!IMPORTANT]
> **INSTRUCTIONS FOR THE AI AGENT:**
> Read and execute this document step-by-step whenever you are tasked with publishing this project to GitHub. This is a global, portable guide designed for all **noybiss (OA)** projects to ensure brand consistency, clean version control, and proper credentials handling.

---

## 🔑 1. Credentials & Token Setup

To authenticate requests to GitHub, follow this hierarchy to obtain the Personal Access Token (PAT):

1. **In-File Placeholder (Portable Method)**: Check the token defined below. If you copy this file to a new project, write your active token here so the agent can access it instantly:
   ```env
   # Replace the placeholder below with your GitHub PAT (Personal Access Token)
   GITHUB_PAT="ghp_YOUR_ACTUAL_PERSONAL_ACCESS_TOKEN_HERE"
   ```
2. **Environment Variable**: Check if `GITHUB_TOKEN` or `GITHUB_PAT` is defined in the system environment.
3. **Local Environment File**: Check if a `.env` file exists in the project root containing `GITHUB_TOKEN=ghp_...` or `GITHUB_PAT=ghp_...`.
4. **Keychain Fallback**: If no token is found, rely on the system's Git credential helper (e.g., macOS Keychain).

### Configuration Details
- **GitHub Username / Organization**: `noybiss`
- **Developer Email**: `noybiss@users.noreply.github.com`
- **Default Branch**: `main`

---

## 🎨 2. The "Noybiss" Project Style Guide

To maintain a consistent style across all projects, you **MUST** apply the following rules:

### A. Repository Naming
- Use strictly **lowercase kebab-case** (e.g., `lake-simulation-timeseries`, `image-classifier-ui`).
- Do not use spaces, uppercase characters, or underscores in the repository name.

### B. Standard README.md Signature
Every project's `README.md` must start and end with the Noybiss signature:
1. **Header**: Starts with a descriptive emoji followed by the name in Title Case (e.g., `# 🌊 OmniSim AI — Lake Simulation TimeSeries v1.0`).
2. **Shield Badges**: Right below the title, include shields representing key technologies and version numbers:
   ```markdown
   [![Python Version](https://img.shields.io/badge/Python-3.9+-blue.svg?style=flat&logo=python&logoColor=white)](https://www.python.org/)
   [![Developer](https://img.shields.io/badge/Made%20by-OA-lightgrey.svg?style=flat)](https://github.com/noybiss)
   ```
3. **Key Features**: A bulleted list using descriptive emojis.
4. **Project Directory Structure**: A clean tree-like directory structure wrapped in a ````text```` block.
5. **Attribution Footer**: The very last line must contain the developer signature:
   ```markdown
   **Developed & Maintained by [OA](https://github.com/noybiss)**  
   *Universal Environmental Intelligence Engine.* (or custom short project tagline in italics)
   ```

### C. Commit Message Style (Conventional Commits + Emojis)
All commit messages must follow the pattern: `<emoji> <type>(<scope>): <short description>`.
Use the following emojis and types:
- ✨ `feat`: New feature addition.
- 🐛 `fix`: Bug resolution.
- 📝 `docs`: Documentation updates.
- 🎨 `style`: Formatting, UI/UX design, or layout tweaks.
- ♻️ `refactor`: Structural code changes without adding features/fixes.
- ⚡️ `perf`: Code optimizations for speed or efficiency.
- 🚀 `release`: Finalizing a release or version bump.

---

## 🚀 3. Step-by-Step Publishing Workflow

Follow these steps in sequence when executing the publish command:

### Step 1: Pre-Publish Clean Up
- Ensure standard local configurations are applied to prevent system-specific files from being uploaded.
- Ensure the project has a `.gitignore` containing at least:
  ```text
  .DS_Store
  __pycache__/
  *.pyc
  .venv/
  venv/
  env/
  .env
  ```
- Double-check that no heavy database files, raw datasets (`.xls`, `.xlsx`, `.csv`), or credentials are being staged.

### Step 2: Initialize Git (If needed)
If the project is not a git repository yet, initialize it:
```bash
git init
```

### Step 3: Configure Git Local User
Ensure the commit author matches the user profile exactly:
```bash
git config --local user.name "noybiss"
git config --local user.email "noybiss@users.noreply.github.com"
```

### Step 4: Configure Remote Repository
1. **Locate Remote**: Run `git remote -v` to check if `origin` is set.
2. **If Remote Does Not Exist**:
   - Check if GitHub CLI (`gh`) is available to create it:
     ```bash
     gh repo create noybiss/<repo-name> --public --source=. --remote=origin
     ```
   - If `gh` is not installed, use GitHub REST API via `curl` with the token:
     ```bash
     curl -H "Authorization: token <token>" https://api.github.com/user/repos -d '{"name":"<repo-name>", "private":false}'
     ```
     Then add the authenticated remote:
     ```bash
     git remote add origin https://noybiss:<token>@github.com/noybiss/<repo-name>.git
     ```
3. **If Remote Exists**:
   - Update the URL to inject the token for authentication if running headlessly:
     ```bash
     git remote set-url origin https://noybiss:<token>@github.com/noybiss/<repo-name>.git
     ```

### Step 5: Stage and Commit
1. Stage all eligible files:
   ```bash
   git add .
   ```
2. Commit with the stylized Noybiss commit message (e.g. initial setup):
   ```bash
   git commit -m "🚀 release: initial commit setup for <repo-name>"
   ```

### Step 6: Push to GitHub
1. Rename the primary branch to `main` (if it isn't already):
   ```bash
   git branch -M main
   ```
2. Push local changes:
   ```bash
   git push -u origin main
   ```

### Step 7: Verification
Verify that the push was successful by checking the output. Report the repository link `https://github.com/noybiss/<repo-name>` to the user.
