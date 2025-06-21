from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.service import Service
from bs4 import BeautifulSoup
import time
from urllib.parse import urlparse

def scrape_jobs_with_selenium(target_url):
    print(f"Scraping jobs from: {target_url}")

    # Set up Firefox in headless mode
    options = Options()
    options.add_argument("--headless")
    service = Service("/usr/local/bin/geckodriver")
    driver = webdriver.Firefox(service=service, options=options)

    try:
        driver.get(target_url)
        time.sleep(25)  # Let JS-rendered content load

        soup = BeautifulSoup(driver.page_source, "html.parser")
        parsed_url = urlparse(target_url)
        base_url = f"{parsed_url.scheme}://{parsed_url.netloc}"

        # Get each job card container
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

        print(f"Found {len(jobs)} jobs.")
        return jobs

    finally:
        driver.quit()
        print("Web driver closed.")
