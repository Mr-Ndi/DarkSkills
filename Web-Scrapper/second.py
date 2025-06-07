from bs4 import BeautifulSoup
import requests


html_text = requests.get('http://www.timesjob.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=python&textLocation=').text
# print(html_text)
soup = BeautifulSoup(html_text, 'lxml')
jobs = soup.find_all('li', class_ = 'clearfix job-bx wht-shd-bx')

for job in jobs:
    company = job.find('h3', class_='joblist-comp-name')
    skill = job.find('span', class_='srp-skills')
    date = job.find('span', class_='sim-posted')

    if company and skill and date:
        company_name = company.text.strip()
        skills = skill.text.strip()
        published_date = date.text.strip()

        print(f"Company: {company_name} | Skills: {skills} | Posted: {published_date}")
        print("-------------------------------------------------------------")

