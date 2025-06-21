from playwright.sync_api import sync_playwright
from bs4 import BeautifulSoup
from urllib.parse import urlparse
import time

def scrape_jobs_with_playwright(target_url):
    print(f"Scraping jobs from: {target_url}")

    with sync_playwright() as p:
        browser = p.firefox.launch(headless=True)
        page = browser.new_page()

        page.goto(target_url)
        page.wait_for_selector("div.bg-card")  # Ensure cards are rendered
        time.sleep(20)  # Optional: let animations/render finish

        html = page.content()
        soup = BeautifulSoup(html, "html.parser")
        parsed_url = urlparse(target_url)
        base_url = f"{parsed_url.scheme}://{parsed_url.netloc}"

        job_cards = soup.select("div.bg-card")
        if not job_cards:
            print("No job cards found.")
            return []

        jobs = []
        for card in job_cards:
            title_elem = card.select_one("h2") or card.select_one("h3")
            company_elem = card.select_one("div[data-slot='card-description']")
            type_elem = card.select_one("span.rounded-full")
            location_elem = card.select_one("div.text-sm.text-muted-foreground")
            link_elem = card.select_one("a[href*='/en/opportunities/']")
            date_elem = card.find("div", string=lambda s: s and "Posted:" in s)

            title = title_elem.get_text(strip=True) if title_elem else "N/A"
            company = company_elem.get_text(strip=True) if company_elem else "N/A"
            job_type = type_elem.get_text(strip=True) if type_elem else "N/A"
            location = location_elem.get_text(strip=True) if location_elem else "N/A"
            link = base_url + link_elem["href"] if link_elem and link_elem.has_attr("href") else "N/A"

            posted_date = None
            if date_elem:
                posted_date = date_elem.get_text(strip=True).replace("Posted:", "").strip()

            if title == "N/A" or link == "N/A":
                print(f"[!] Skipped due to missing title/link: {title}")
                continue

            job = {
                "Title": title,
                "Type": job_type,
                "Company": company,
                "Location": location,
                "Link": link,
            }
            if posted_date:
                job["Posted Date"] = posted_date

            jobs.append(job)

        browser.close()
        print(f"Found {len(jobs)} jobs.")
        return jobs
