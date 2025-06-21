from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import time
from urllib.parse import urlparse

def scrape_jobs_with_selenium(target_url):
    print(f"Scraping jobs from: {target_url}")

    # Set up headless Chrome
    options = Options()
    options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    driver = webdriver.Chrome(options=options)

    try:
        driver.get(target_url)
        time.sleep(5)  # Give time for JavaScript to load content

        soup = BeautifulSoup(driver.page_source, "html.parser")

        # Dynamically extract base URL
        parsed_url = urlparse(target_url)
        base_url = f"{parsed_url.scheme}://{parsed_url.netloc}"

        job_cards = soup.select('div.bg-card')
        if not job_cards:
            print("No job cards found.")
            return []

        jobs = []
        for card in job_cards:
            title_elem = card.select_one("h2") or card.select_one("h3")
            company_elem = card.select_one("div:has(svg) + div")
            type_elem = card.select_one("span.rounded-full")
            location_elem = card.select_one("div:contains('Rwanda')")
            date_elem = card.select_one("div:contains('Posted:')")
            link_elem = card.select_one("a[href*='/opportunities/']")

            title = title_elem.get_text(strip=True) if title_elem else "N/A"
            company = company_elem.get_text(strip=True) if company_elem else "N/A"
            job_type = type_elem.get_text(strip=True) if type_elem else "N/A"
            location = location_elem.get_text(strip=True) if location_elem else "N/A"
            link = base_url + link_elem["href"] if link_elem else "N/A"

            posted_date = None
            if date_elem and "Posted:" in date_elem.text:
                posted_date = date_elem.text.replace("Posted:", "").strip()

            if not title or not link or title == "N/A" or link == "N/A":
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
