# 🚀 Auto-Updater for Python (GitHub-Based)

[![PyPI version](https://badge.fury.io/py/Auto-Updater.svg)](https://badge.fury.io/py/Auto-Updater)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.6+](https://img.shields.io/badge/python-3.6+-blue.svg)](https://www.python.org/downloads/)

A lightweight, drop-in module that allows your Python applications to **update themselves** automatically by fetching the latest source code from a public GitHub repository.

It handles **version checking**, **zipping/downloading**, **extraction**, and **overwriting** recursively, making it perfect for complex projects with multiple folders.

---

## ✨ Features

* **Zero-Config Defaults:** Works out of the box with minimal setup.
* **Directory Support:** Updates entire directory structures, not just single files.
* **Smart Extraction:** Automatically strips GitHub's root folder (e.g., `Repo-main/`) to ensure files land in the correct place.
* **CLI & Importable:** Run it from the terminal or import it into your Python code.
* **Cross-Platform:** Tested on Windows, macOS, and Linux.

---

## 📦 Installation

Install via pip:

```bash
pip install Auto-Updater
```

---

## 🛠️ Usage

### Method 1: Python Code (Recommended)

Integrate the updater directly into your application's startup sequence.

```python
from Auto-Updater import AutoUpdater

# Initialize with your GitHub repository details
updater = AutoUpdater(
    owner="YourGithubUsername",
    repo="YourRepoName",
    branch="main",          # Optional, defaults to main
    target_dir="."          # Optional, defaults to current directory
)

# Check for updates
update_available, local_ver, remote_ver = updater.check_for_updates()

if update_available:
    print(f"New version available: {remote_ver} (Current: {local_ver})")
    choice = input("Update now? [y/N]: ")
    
    if choice.lower() == 'y':
        success = updater.do_update()
        if success:
            print("Update successful! Please restart the application.")
            exit()
```

### Method 2: Command Line Interface (CLI)

You can use the module as a standalone tool to fix broken installations or force updates.

```bash
# Check if an update is available
python -m your_package_name --check

# Perform the update immediately
python -m your_package_name --update

# Force re-download (useful if local files are corrupted)
python -m your_package_name --force
```

---

## ⚙️ Repository Setup

For the updater to work, your GitHub repository must have a `version.json` file in the root directory.

**File:** `version.json`

```json
{
    "version": "1.0.5"
}
```

**Workflow:**

1. Make changes to your code locally.
2. Bump the version number in `version.json`.
3. Push changes to GitHub.
4. Clients will detect the version mismatch and download the new code.

---

## ⚠️ Requirements

* Python 3.6+
* `requests` library (automatically installed)
* A **Public** GitHub repository (Private repos require Personal Access Token logic, not included in this base version).

---

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details
