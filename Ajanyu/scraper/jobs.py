import requests
from bs4 import BeautifulSoup

def scrape_jobs(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    
    jobs = []
    job_elements = soup.select('div[data-slot="card"]')
    
    for job_element in job_elements:
        title_elem = job_element.select_one('div[data-slot="card-title"]')
        type_elem = job_element.select_one('div.rounded-full.bg-muted.px-3.py-1.text-sm.font-medium')

        title = title_elem.get_text(strip=True) if title_elem else 'N/A'
        job_type = type_elem.get_text(strip=True) if type_elem else 'N/A'
        
        jobs.append({
            'title': title,
            'type': job_type
        })
    
    return jobs
