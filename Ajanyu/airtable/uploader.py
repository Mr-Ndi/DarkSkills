import requests
import os

AIRTABLE_API_KEY = os.getenv("AIRTABLE_API_KEY")
BASE_ID = "your_base_id"
TABLE_NAME = "your_table_name"

def upload_to_airtable(jobs):
    url = f"https://api.airtable.com/v0/{BASE_ID}/{TABLE_NAME}"
    headers = {
        "Authorization": f"Bearer {AIRTABLE_API_KEY}",
        "Content-Type": "application/json"
    }

    for job in jobs:
        data = {
            "fields": {
                "Title": job["title"],
                "Type": job["type"]
            }
        }
        response = requests.post(url, json=data, headers=headers)
        if response.status_code != 200:
            print(f"Failed to upload: {job['title']}, Error: {response.text}")
