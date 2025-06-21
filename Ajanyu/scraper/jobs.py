import requests

def fetch_jobs_from_api():
    url = "https://opportunity.ini.rw/api/opportunities?locale=en&limit=20&offset=0&type=job"
    print(f"Scraping jobs from: {url}")

    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
    except requests.RequestException as e:
        print(f"Failed to fetch data: {e}")
        return []
    except ValueError:
        print("Failed to parse JSON response.")
        return []

    items = data.get("data", [])
    if not items:
        print("No jobs found in API response.")
        return []

    jobs = []
    for item in items:
        title = item.get("title")
        slug = item.get("slug")
        company = item.get("company", {}).get("name")
        job_type = item.get("job_type")
        location = item.get("location")
        posted_date = item.get("posted_at")

        if not title or not slug:
            print(f"[!] Skipped due to missing data: {title or 'N/A'}")
            continue

        job = {
            "Title": title,
            "Link": f"https://opportunity.ini.rw/en/opportunities/{slug}",
            "Company": company or "N/A",
            "Type": job_type or "N/A",
            "Location": location or "N/A",
        }

        if posted_date:
            job["Posted Date"] = posted_date

        jobs.append(job)

    print(f"Found {len(jobs)} jobs.")
    return jobs
