# 🕷️ Dynamic Web Scraper

> A powerful Python-based web scraper using **Playwright** with stealth mode that automatically extracts data from websites and saves it neatly into an **Excel file**.

---

## 📋 Table of Contents

- [Features](#-features)
- [Project Files](#-project-files)
- [System Requirements](#-system-requirements)
- [Installation Guide](#-installation-guide)
- [Configuration](#-configuration)
- [How to Run](#-how-to-run)
- [Expected Output](#-expected-output)
- [Common Errors & Fixes](#-common-errors--fixes)
- [Dependencies](#-dependencies)

---

## ✨ Features

- ✅ Stealth mode — bypasses bot detection
- ✅ Human scroll simulation — behaves like a real user
- ✅ Multi-page scraping support
- ✅ Auto pagination — automatically finds and navigates to the next page
- ✅ Data saved directly into an Excel file
- ✅ Detailed logging — records every step of the process

---

## 📁 Project Files

```
📦 Scraper/
├── 📄 dynamic_scraper.py     ← Main scraper code
├── 📄 config.json            ← Scraper settings
├── 📄 requirements.txt       ← List of required packages
└── 📄 README.md              ← This guide
```

---

## 💻 System Requirements

Before getting started, make sure you have the following installed on your PC:

| Tool | Version | Download |
|------|---------|----------|
| Python | **3.11.15** | [Download Here](https://www.python.org/downloads/release/python-31115/) |
| VS Code | Latest | [Download Here](https://code.visualstudio.com/) |
| VS Code Python Extension | Latest | Search `Python` by Microsoft inside VS Code Extensions |

> ⚠️ **Important:** When installing Python 3.11.15, **do NOT check** the **"Add Python to PATH"** option ❌

---

## 🚀 Installation Guide

### Step 1 — Install Python 3.11.15

1. Open [this link](https://www.python.org/downloads/release/python-31115/)
2. Scroll down and download **"Windows installer (64-bit)"**
3. Run the installer — but **do NOT check "Add Python to PATH"** ❌

---

### Step 2 — Download the Project

1. Click the green **"Code"** button on GitHub
2. Select **"Download ZIP"**
3. Extract the ZIP file
4. Place the folder anywhere on your PC — e.g. `C:\Scraper`

---

### Step 3 — Open the Project in VS Code

```
File → Open Folder → Select your Scraper folder → Click Select Folder
```

---

### Step 4 — Open the Terminal

```
Terminal → New Terminal
```

You should see something like this at the bottom:
```
PS C:\Scraper>
```

---

### Step 5 — Verify Python Installation

Type this in the terminal and press Enter:

```bash
py -3.11 --version
```

✅ You should see: `Python 3.11.15`

---

### Step 6 — Create a Virtual Environment

```bash
py -3.11 -m venv venv
```

> A virtual environment is an isolated space just for this project — your system Python will not be affected

---

### Step 7 — Activate the Virtual Environment

```bash
venv\Scripts\activate
```

✅ Success indicator — you will see `(venv)` at the start of your terminal:
```
(venv) PS C:\Scraper>
```

> ❗ If you see this error: `running scripts is disabled on this system` — run this command first:
> ```bash
> Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
> ```
> If it asks `Y/N` — press `Y` and then try activating again

---

### Step 8 — Install Required Packages

```bash
pip install -r requirements.txt
```

> ☕ This may take a moment — let it finish

---

### Step 9 — Install the Correct Version of Playwright Stealth

```bash
pip install playwright-stealth==1.0.6
```

> ⚠️ This step is required — without it the code will crash

---

### Step 10 — Install the Playwright Browser

```bash
playwright install chromium
```

> ☕ This will download the Chromium browser — it is a large file, let it finish

---

## ⚙️ Configuration

Open the `config.json` file and adjust the settings as needed:

```json
{
    "target_url": "http://quotes.toscrape.com",
    "extraction_limit_pages": 3,
    "excel_output_filename": "dynamic_scraped_records.xlsx",
    "headless_mode_enabled": false
}
```

| Setting | Description | Example |
|---------|-------------|---------|
| `target_url` | The website you want to scrape | `"http://quotes.toscrape.com"` |
| `extraction_limit_pages` | Number of pages to scrape | `3` |
| `excel_output_filename` | Name of the output Excel file | `"my_data.xlsx"` |
| `headless_mode_enabled` | Show or hide the browser window | `false` = visible, `true` = hidden |

---

## ▶️ How to Run

Once everything is installed, run this command:

```bash
python dynamic_scraper.py
```

> ⚠️ **Important:** Every time you open a new terminal, activate the virtual environment first:
> ```bash
> venv\Scripts\activate
> ```

---

## ✅ Expected Output

### Terminal will show:
```
[INFO] Scraper is starting...
[INFO] Processing Page 1 of 3...
[INFO] Human scroll simulation running...
[INFO] Processing Page 2 of 3...
[INFO] Human scroll simulation running...
[INFO] Processing Page 3 of 3...
[INFO] Human scroll simulation running...
[INFO] Browser closed successfully.
[INFO] Data saved successfully: dynamic_scraped_records.xlsx
```

### Excel file will contain these columns:

| Target Page | Author Identity | Scraped Payload | Extraction Timestamp |
|-------------|----------------|-----------------|----------------------|
| 1 | Albert Einstein | The world is... | 2026-05-18 02:12:52 |
| 1 | J.K. Rowling | It is our choices... | 2026-05-18 02:12:55 |

The Excel file will be created inside your **project folder** ✅

---

## ❗ Common Errors & Fixes

| Error Message | Cause | Fix |
|---------------|-------|-----|
| `py -3.11 not found` | Python 3.11 is not installed | [Install Python 3.11.15](https://www.python.org/downloads/release/python-31115/) |
| `running scripts is disabled` | PowerShell execution policy | Run `Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser` |
| `cannot import name stealth_async` | Wrong version of stealth installed | Run `pip install playwright-stealth==1.0.6` |
| `NotImplementedError` | Windows event loop issue | Use `WindowsProactorEventLoopPolicy()` at the bottom of the script |
| `No such file or directory` | Wrong folder opened in VS Code | Open the correct folder in VS Code |
| `ModuleNotFoundError` | Packages not installed | Run `pip install -r requirements.txt` again |

---

## 📦 Dependencies

| Package | Version | Purpose |
|---------|---------|---------|
| `playwright` | latest | Browser automation |
| `playwright-stealth` | **1.0.6** | Bypass bot detection |
| `pandas` | latest | Data processing |
| `openpyxl` | latest | Writing Excel files |
