import os
import requests
from dotenv import load_dotenv

load_dotenv()

# Load environment variables
api_key = os.getenv("AIRTABLE_API_KEY")
base_id = os.getenv("AIRTABLE_BASE_ID")
table_id_or_name = os.getenv("AIRTABLE_TABLE_NAME")

# Validate environment variables
if not all([api_key, base_id, table_id_or_name]):
    print("❌ Missing one or more required environment variables:")
    print(f"   - AIRTABLE_API_KEY: {'✅' if api_key else '❌'}")
    print(f"   - AIRTABLE_BASE_ID: {'✅' if base_id else '❌'}")
    print(f"   - AIRTABLE_TABLE_NAME: {'✅' if table_id_or_name else '❌'}")
    exit(1)

# Compose API request
url = f"https://api.airtable.com/v0/{base_id}/{table_id_or_name}"
headers = {
    "Authorization": f"Bearer {api_key}",
    "Content-Type": "application/json"
}

# Debug info
print("🔐 Token starts with:", api_key[:8], "(length:", len(api_key), ")")
print("📄 Base ID:", base_id)
print("📄 Table ID or Name:", table_id_or_name)
print("🔗 Full URL:", url)

# Make request
response = requests.get(url, headers=headers)

# Handle response
if response.status_code == 200:
    data = response.json()
    records = data.get("records", [])
    print(f"✅ Success! Found {len(records)} record(s).")
    if records:
        print("📄 First record:")
        print(records[0].get("fields", {}))
    else:
        print("ℹ️ No records found in the table.")
else:
    print("❌ Airtable API error:")
    print(f"   Status Code: {response.status_code}")
    try:
        error_data = response.json()
        print(f"   Error Type: {error_data.get('error', {}).get('type')}")
        print(f"   Message: {error_data.get('error', {}).get('message')}")
    except Exception as e:
        print("   Failed to parse error response:", e)
        print("   Raw response:", response.text)
