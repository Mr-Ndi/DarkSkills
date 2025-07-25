import os
import requests
from dotenv import load_dotenv

load_dotenv()

AIRTABLE_API_KEY = os.getenv("AIRTABLE_API_KEY")
BASE_ID = os.getenv("AIRTABLE_BASE_ID")
TABLE_NAME = os.getenv("AIRTABLE_TABLE_NAME")

if not AIRTABLE_API_KEY or not BASE_ID or not TABLE_NAME:
    raise ValueError("Please set AIRTABLE_API_KEY, BASE_ID, and TABLE_NAME in your .env file.")

def upload_to_airtable(jobs):
    url = f"https://api.airtable.com/v0/{BASE_ID}/{TABLE_NAME}"
    headers = {
        "Authorization": f"Bearer {AIRTABLE_API_KEY}",
        "Content-Type": "application/json"
    }

    required_keys = ["Title", "Type", "Company", "Link", "Location"]

    for job in jobs:
        # Skip if any required key is missing or its value is "N/A"
        if not all(key in job and job[key] != "N/A" for key in required_keys):
            print(f"[!] Skipped incomplete job: {job}")
            continue

        # ✅ Fix duplicate link prefix
        if job["Link"].count("https://opportunity.ini.rw") > 1:
            job["Link"] = job["Link"].replace("https://opportunity.ini.rw", "", 1)

        data = {
            "fields": {
                "Title": job["Title"],
                "Type": job["Type"],
                "Company": job["Company"],
                "Link": job["Link"],
                "Location": job["Location"]
            }
        }

        if "Posted Date" in job:
            data["fields"]["Posted Date"] = job["Posted Date"]

        response = requests.post(url, json=data, headers=headers)

        if response.status_code == 201:
            print(f"[✓] Uploaded: {job['Title']}")
        else:
            print(f"[✗] Failed: {job.get('Title', 'Unknown')} → {response.status_code}: {response.text}")
