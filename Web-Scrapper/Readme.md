# 🕷️ Web-Scrapper

A Python-based web scraping module that extracts **Python job listings** from the mobile version of [TimesJobs](https://m.timesjobs.com). This directory is part of the larger `DarkSkills` project and showcases practical use of web scraping techniques using `requests`, `BeautifulSoup`, and `lxml`.

---

## 📁 Contents

| File              | Description                                                                 |
|-------------------|-----------------------------------------------------------------------------|
| `courses.html`    | Sample static HTML page (e.g., saved from TimesJobs) for structure testing. |
| `main.py`         | Early scraping script targeting TimesJobs desktop site.                     |
| `second.py`       | ✅ **Final working script** using mobile-friendly layout and resilient parsing. |
| `Third_one.ipynb` | Jupyter Notebook for testing scraping logic interactively.                  |

---

## 🚀 Usage

### Prerequisites

Install the required Python packages:

```bash
pip install requests beautifulsoup4 lxml
````

> For the Jupyter Notebook:

```bash
pip install notebook
jupyter notebook
```

---

### Run the Scraper

Execute the script:

```bash
python3 second.py
```

If no jobs are found or the page layout has changed, the output will notify you:

```
⚠️ No jobs found or page structure has changed.
```

Each job listing includes:

* ✅ Job Title
* 🏢 Company Name
* 📅 Date Posted

---

## 📌 Notes

* This script uses the **mobile site** of TimesJobs because of its simpler and more consistent HTML structure.
* The `User-Agent` header is spoofed to simulate a mobile browser.
* If the scraping fails, inspect the page structure and update the class names in `second.py`.

---

## 🧠 Part of [DarkSkills](https://github.com/Mr-Ndi/DarkSkills)

This module is a part of the DarkSkills repository — a toolkit of automation, scripting, and skill development projects.

```