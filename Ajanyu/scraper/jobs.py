import requests
from bs4 import BeautifulSoup

def scrape_jobs(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    jobs = []
    job_cards = soup.select('div[data-slot="card"]')

    if not job_cards:
        print("No job cards found.")
        return jobs

    for card in job_cards:
        title_elem = card.select_one('div[data-slot="card-title"]')
        type_elem = card.select_one('div.rounded-full.bg-muted.px-3.py-1.text-sm.font-medium')
        company_elem = card.select_one('div[data-slot="card-description"]')
        link_elem = card.select_one('a.block')
        location_elem = card.select_one('div.text-sm.mt-1')
        date_elem = card.select_one('div.text-sm.text-muted-foreground')

        title = title_elem.get_text(strip=True) if title_elem else 'N/A'
        job_type = type_elem.get_text(strip=True) if type_elem else 'N/A'
        company = company_elem.get_text(strip=True) if company_elem else 'N/A'
        link = 'https://opportunity.ini.rw' + link_elem['href'] if link_elem and link_elem.has_attr('href') else 'N/A'
        location = location_elem.get_text(strip=True) if location_elem else 'N/A'
        posted_date = date_elem.text.replace('Posted:', '').strip() if date_elem and 'Posted:' in date_elem.text else 'N/A'

        jobs.append({
            'Title': title,
            'Type': job_type,
            'Company': company,
            'Link': link,
            'Location': location,
            'Posted Date': posted_date
        })

    return jobs
