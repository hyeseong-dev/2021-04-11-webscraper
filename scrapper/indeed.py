import re
import requests

from urllib.parse import unquote
from pprint       import pprint
from bs4          import BeautifulSoup


LIMIT = 50

def get_last_page(url):
    result     = requests.get(url)
    soup       = BeautifulSoup(result.text, 'html.parser')
    pagination = soup.find('div', {'id':'searchCountPages'})
    str_list_max_page = re.findall('\d+', pagination.get_text(strip=True)) # 모든 문자에서 숫자만 뽑아낸것
    max_page = int(str_list_max_page[0])
    return max_page


def extract_job(html):
        title   = html.find('h2', {'class':'title'}).find('a')['title']
        company = html.find('span', {'class': 'company'}) # find: 첫 번째 찾은 결과를 돌려줌 V.S find_all : 전체를 찾아서 리스트에 담아 리턴함
        company_anchor = company.find('a')
        if company.find('a') is not None:
            company = (str(company_anchor.string).strip()) # str으로 만들어 주는 이유는 빈공백을 제거하기 위해 우선 문자열로 변환시킨 후 정제처리를 하기위함임.
        else:
            company = str(company.string.strip())
        print(company)
        location = html.find('div', {'class':'recJobLoc'})['data-rc-loc']
        job_id   = html['data-jk']
        
        return {'title': title, 
                'company': company, 
                'location':location, 
                'link': f'https://www.indeed.com/viewjob?jk={job_id}'
            }

def extract_jobs(last_page,url):
    jobs=list()
    for page in range(last_page):
        print(f"Scrapping Indeed page {page+1}")
        result  = requests.get(f'{url}&start={page*LIMIT}')
        soup    = BeautifulSoup(result.text, 'html.parser')
        results = soup.find_all('div', {'class':'jobsearch-SerpJobCard'})
        for result in results:
            job = extract_job(result)
            jobs.append(job)
    return jobs


def get_jobs(word):
    word = 'python'
    url = 'https://kr.indeed.com/jobs?q={word}&start=9999&limit=50'
    last_page = get_last_page(url)
    jobs      = extract_jobs(last_page,url)
    return jobs

