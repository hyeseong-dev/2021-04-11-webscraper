import re
import requests

from math         import ceil
from urllib.parse import unquote
from pprint       import pprint
from bs4          import BeautifulSoup


def get_last_page(url):
    result     = requests.get(url)
    soup       = BeautifulSoup(result.text, 'html.parser')
    pagination = soup.find('span', {'class':'cnt_result'})
    str_list_max_page = re.findall('\d+', pagination.get_text(strip=True)) # 모든 문자에서 숫자만 뽑아낸것
    max_page = ceil(float(''.join(str_list_max_page))*0.01)
    return max_page


def extract_job(html):
        title   = html.find('h2', {'class':'job_tit'}).find('a')['title']
        company = html.find('strong', {'class': 'corp_name'}).find('a')['title'] # find: 첫 번째 찾은 결과를 돌려줌 V.S find_all : 전체를 찾아서 리스트에 담아 리턴함
        locations = html.find('div', {'class':'job_condition'}).find_all('a')
        location = ''
        for loc in locations:
            location += loc.get_text()
        job_id = html['value']
        return {
                'title': title, 
                'company': company, 
                'location':location, 
                'link': f'https://www.saramin.co.kr/zf_user/jobs/relay/view?rec_idx={job_id}'
             }

def extract_jobs(last_page,url):
    jobs=list()
    for page in range(last_page):
        print(f"Scrapping saramin page {page+1}")
        result  = requests.get(f'{url}&recruitPage={page+1}&recruitPageCount=100')
        soup    = BeautifulSoup(result.text, 'html.parser')
        results = soup.find_all('div', {'class':'item_recruit'})
        for result in results:
            job = extract_job(result)
            jobs.append(job)
    return jobs


def get_jobs(word):
    KEYWORD = 'java'
    url = f'https://www.saramin.co.kr/zf_user/search/recruit?searchword={KEYWORD}'
    last_page = get_last_page(url)
    jobs      = extract_jobs(last_page,url)
    return jobs

