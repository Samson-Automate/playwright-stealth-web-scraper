# 🕷️ Stealth Playwright Web Scraper (Anti-Bot Ready)

> A **production-ready web scraping engine** built with Playwright that mimics human behavior, bypasses basic bot detection, and extracts structured data into Excel & JSON formats.

---

## 🎯 Workflow Diagram

<img width="1536" height="1024" alt="ChatGPT Image May 18, 2026, 03_08_05 AM" src="https://github.com/user-attachments/assets/8344f2db-cb0a-42b0-97a6-641f8bb1f861" />
---

## 🖥️ Live Execution (Terminal Output)

### ▶️ Scraper Running Logs

<img width="1321" height="689" alt="terminal output" src="https://github.com/user-attachments/assets/cfbed9e7-e231-49a9-acc3-326fda6c0304" />---

### 📊 Extracted Data Preview

<img width="1009" height="165" alt="terminal output 2" src="https://github.com/user-attachments/assets/8498b0dd-1298-479e-994a-4081c62be287" />---

## 💻 System Requirements

Make sure you have the following installed:

- **Python 3.10+ (Recommended: 3.11)**
- **Node.js (optional, for Playwright dependencies)**
- **Git (optional)**

> ⚠️ Recommended: Use Python **3.11** for best compatibility

---

## 📦 Dependencies

| Package | Recommended Version |
|--------|--------------------|
| playwright | >=1.40 |
| playwright-stealth | 1.0.6 |
| pandas | >=2.0 |
| openpyxl | >=3.1 |

---

## ▶️ Setup & Installation

### 1. Create Virtual Environment

```bash
python -m venv venv
```

### 2. Activate Environment

```bash
venv\Scripts\activate   # Windows
source venv/bin/activate  # Mac/Linux
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Install Playwright Browser

```bash
playwright install chromium
```

---

## ⚡ Key Highlights

- 🛡️ **Stealth Mode Enabled** — reduces bot detection using browser fingerprint masking  
- 🤖 **Human-like Behavior** — randomized scrolling & delays  
- 🔄 **Auto Pagination** — handles multi-page scraping automatically  
- ⚙️ **Fully Configurable** — change target website without touching code  
- 🌐 **Proxy Support** — ready for large-scale scraping  
- 🔁 **Retry System** — handles network failures gracefully  
- 📊 **Multiple Outputs** — exports to Excel & JSON  
- 🧾 **Detailed Logging** — full visibility of scraping process  

---

## 🎯 Use Cases

- E-commerce product scraping  
- Job listings extraction  
- Blog/article scraping  
- Data collection for research  
- Automation workflows  

---

## 🧠 How It Works

1. Launches a real browser using Playwright  
2. Applies stealth techniques to reduce detection  
3. Simulates human scrolling & delays  
4. Extracts structured data using configurable selectors  
5. Navigates across multiple pages automatically  
6. Saves results into structured files  

---

## 📁 Project Structure

```
📦 scraper/
├── scraper.py
├── config.json
├── requirements.txt
└── README.md
```

---

## ⚙️ Configuration

```json
{
  "target_url": "http://quotes.toscrape.com",
  "extraction_limit_pages": 3,
  "excel_output_filename": "scraped_data.xlsx",
  "headless_mode_enabled": false,

  "selectors": {
    "container": ".quote",
    "text": ".text",
    "author": ".author"
  },

  "proxy": null
}
```

---

## ▶️ Quick Start

```bash
python scraper.py
```

---

## 📊 Output Example

| page | author | text | timestamp |
|------|--------|------|----------|
| 1 | Albert Einstein | Life is like riding a bicycle... | 2026-05-18 |

---

## ⚠️ Disclaimer

This tool is intended for **educational and ethical scraping purposes only**.

---

## 🧰 Tech Stack

- Python  
- Playwright  
- Playwright Stealth  
- Pandas  

---

## ⭐ Why This Project Stands Out

- Anti-detection techniques  
- Real-world scraping readiness  
- Clean architecture  
- Config-driven system  

---

## 📬 Work With Me

Need custom scraping or automation? Let’s build something powerful 🚀
