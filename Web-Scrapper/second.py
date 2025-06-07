from bs4 import BeautifulSoup
import requests

# Use the mobile version URL directly (as in your screenshot)
URL = "https://m.timesjobs.com/mobile/jobs-search-result.html?txtKeywords=python&cboWorkExp1=3&txtLocation="

# Mobile browser user-agent
headers = {
    "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 14_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0 Mobile/15E148 Safari/604.1"
}

# Fetch and parse page
response = requests.get(URL, headers=headers)
soup = BeautifulSoup(response.text, "lxml")

# Find all job cards by li class
jobs = soup.find_all("li", class_="srp-listing clearfix")

# Check if any jobs found
if not jobs:
    print("⚠️ No jobs found or page structure has changed.")
else:
    for job in jobs:
        # Extract title from link
        link = job.find("a", class_="srp-apply-new ui-link")
        job_title = link['href'].split('/')[-1].replace('-', ' ').title() if link else "N/A"

        # Extract company from short-desc block
        company = job.find("div", class_="short-desc")
        company_text = company.text.strip() if company else "N/A"

        # Posted date
        posted_span = job.find("span", class_="shortstar70787018")
        posted = posted_span.text.strip() if posted_span else "N/A"

        print(f"Job Title  : {job_title}")
        print(f"Company    : {company_text}")
        print(f"Posted     : {posted}")
        print("-" * 50)

