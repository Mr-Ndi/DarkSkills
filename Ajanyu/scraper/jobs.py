from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options
import time

def scrape_jobs(firefox_binary, geckodriver_path):
    options = Options()
    options.binary_location = firefox_binary
    service = Service(geckodriver_path)

    driver = webdriver.Firefox(service=service, options=options)

    try:
        driver.get("https://opportunity.ini.rw/")
        time.sleep(5)

        print("🌐 Page loaded.")
        job_cards = driver.find_elements(By.CSS_SELECTOR, "div[data-slot='card']")
        print(f"🧾 Found {len(job_cards)} job cards")

        jobs = []
        for card in job_cards:
            try:
                title = card.find_element(By.CSS_SELECTOR, "div[data-slot='card-title']").text
                company = card.find_element(By.CSS_SELECTOR, "div[data-slot='card-description']").text

                # Badge spans: [0] = deadline, [1] = contract
                badges = card.find_elements(By.CSS_SELECTOR, "span[data-slot='badge']")
                deadline = badges[0].text if len(badges) > 0 else "N/A"
                contract = badges[1].text if len(badges) > 1 else "N/A"

                # Location
                location = card.find_element(By.CSS_SELECTOR, "div[data-slot='card-content'] span").text

                # Posted date
                footer = card.find_element(By.CSS_SELECTOR, "div[data-slot='card-footer']")
                date_posted = footer.find_element(By.TAG_NAME, "span").text.strip().replace("Posted:", "").strip()

                # URL
                link_el = card.find_element(By.CSS_SELECTOR, "a[href*='/opportunities/']")
                url = "https://opportunity.ini.rw" + link_el.get_attribute("href")

                jobs.append({
                    "title": title,
                    "company": company,
                    "location": location,
                    "contract": contract,
                    "deadline": deadline,
                    "date_posted": date_posted,
                    "url": url
                })

            except Exception as e:
                print(f"⚠️ Skipped a card: {e}")
                continue

        return jobs

    finally:
        driver.quit()
