import requests
from bs4 import BeautifulSoup
from urllib.parse import urlparse

def scrape_jobs(target_url):
    response = requests.get(target_url)
    soup = BeautifulSoup(response.text, 'html.parser')

    # Dynamically extract the base URL (scheme + domain)
    parsed_url = urlparse(target_url)
    base_url = f"{parsed_url.scheme}://{parsed_url.netloc}"

    jobs = []
    job_cards = soup.select('div[data-slot="card"]')

    if not job_cards:
        print("No job cards found.")
        return jobs

    for card in job_cards:
        # Extract elements
        title_elem = card.select_one('div[data-slot="card-title"]')
        type_elem = card.select_one('div.rounded-full.bg-muted.px-3.py-1.text-sm.font-medium')
        company_elem = card.select_one('div[data-slot="card-description"]')
        link_elem = card.select_one('a.block')
        location_elem = card.select_one('div.text-sm.mt-1')
        date_elem = card.select_one('div.text-sm.text-muted-foreground')

        # Parse text or fallback
        title = title_elem.get_text(strip=True) if title_elem else 'N/A'
        job_type = type_elem.get_text(strip=True) if type_elem else 'N/A'
        company = company_elem.get_text(strip=True) if company_elem else 'N/A'
        link = base_url + link_elem['href'] if link_elem and link_elem.has_attr('href') else 'N/A'
        location = location_elem.get_text(strip=True) if location_elem else 'N/A'

        # Extract posted date only if valid
        posted_date = None
        if date_elem and 'Posted:' in date_elem.text:
            raw_date = date_elem.text.replace('Posted:', '').strip()
            if raw_date:  # basic sanity check
                posted_date = raw_date

        # Build the record safely
        job = {
            'Title': title,
            'Type': job_type,
            'Company': company,
            'Link': link,
            'Location': location,
        }

        # Only add date if it's valid
        if posted_date:
            job['Posted Date'] = posted_date

        jobs.append(job)

    return jobs
