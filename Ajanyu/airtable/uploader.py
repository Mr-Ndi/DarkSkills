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

    for job in jobs:
        data = {
            "fields": {
                "Title": job["Title"],
                "Type": job["Type"],
                "Company": job["Company"],
                "Link": job["Link"],
                "Location": job["Location"],
                "Posted Date": job["Posted Date"]
            }
        }

        response = requests.post(url, json=data, headers=headers)
        if response.status_code != 200:
            print(f"Failed to upload: {job['Title']}, Error: {response.text}")
        else:
            print(f"Uploaded: {job['Title']}")
