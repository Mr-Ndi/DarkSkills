import os
from dotenv import load_dotenv
from scraper.jobs import scrape_jobs
from airtable.uploader import upload_to_airtable

load_dotenv()

def main():
    url = os.getenv("TARGET_URL")
    if not url:
        print("TARGET_URL not set in .env")
        return

    print(f"Scraping jobs from: {url}")
    jobs = scrape_jobs(url)
    print(f"Found {len(jobs)} jobs.")

    if jobs:
        upload_to_airtable(jobs)
        print("Upload complete.")
    else:
        print("No jobs to upload.")

if __name__ == "__main__":
    main()
