import os
from dotenv import load_dotenv
from scraper.jobs import scrape_jobs
from airtable.uploader import upload_to_airtable

load_dotenv()

FIREFOX_BIN = os.getenv("FIREFOX_BIN", "/home/me/firefox-esr/firefox/firefox")
GECKODRIVER_PATH = os.getenv("GECKODRIVER_PATH", "/snap/bin/geckodriver")

if __name__ == "__main__":
    raw_jobs = scrape_jobs(FIREFOX_BIN, GECKODRIVER_PATH)

    # Normalize keys to match Airtable expectations
    normalized_jobs = []
    for job in raw_jobs:
        normalized_jobs.append({
            "Title": job.get("title", "N/A"),
            "Company": job.get("company", "N/A"),
            "Location": job.get("location", "N/A"),
            "Type": job.get("contract", "N/A"),
            "Posted Date": job.get("date_posted", "N/A"),
            "Link": job.get("url", "N/A")
        })

    upload_to_airtable(normalized_jobs)

    # Debbugging tools
#     print(f"✅ Scraped {len(jobs)} jobs")
#     for job in jobs:
#         print(f"""
# 📌 {job['title']} @ {job['company']}
# 📍 {job['location']} | {job['contract']} | {job['deadline']}
# 🗓️  Posted: {job['date_posted']}
# 🔗 {job['url']}
#         """)
