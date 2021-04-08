import requests

from bs4 import BeautifulSoup

URL = f'https://stackoverflow.com/jobs/companies?q=python&sort=1'


def get_last_page():
    result = requests.get(URL)
    soup   = BeautifulSoup(result.text, 'html.parser')
    pages = soup.find('div', {'class':'s-pagination'}).find_all('a')
    last_page_anchor = pages[-2]
    last_page = int(last_page_anchor.get_text().strip())
    return last_page


def extract_job(html):
    title = html.find('h2', {'class':'company'})
    print(title)




def extract_jobs(last_page):
    jobs = list()
    # for page in range(last_page):
    result = requests.get(f'{URL}&pg=0')
    soup = BeautifulSoup(result.text, 'html.parser')
    results = soup.find_all('div', {'class':'company-list'})
    for result in results:
        job = extract_job(result)
        jobs.append(job)
    return jobs

def get_jobs():
    last_page = get_last_page()
    jobs = extract_jobs(last_page)
    return jobs