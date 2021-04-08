
import re
import requests
from bs4 import BeautifulSoup

LIMIT = 50
URL = 'https://kr.indeed.com/%EC%B7%A8%EC%97%85?q=java&limit=999&start=9999'

def extract_indeed_pages():
    result = requests.get(URL)
    soup = BeautifulSoup(result.text, 'html.parser')
    pagination = soup.find('div', {'id':'searchCountPages'})
    str_list_max_page = re.findall('\d+', pagination.string.strip().split()[0]) # 모든 문자에서 숫자만 뽑아낸것
    max_page = int(str_list_max_page[0])
    return max_page

def extract_indeed_jobs(last_page):
    jobs=list()

    # for page in range(last_page):
    result = requests.get(f'{URL}&start={0*LIMIT}')
    soup = BeautifulSoup(result.text, 'html.parser')
    results = soup.find_all('div', {'class':'jobsearch-SerpJobCard'})
    for result in results:
        title = result.find('h2', {'class':'title'}).find('a')['title']
        company = result.find('span', {'class': 'company'})
        print(company)
    return jobs




# links = pagination.findAll('a')

# pages = []
# for link in links:
#     pages.append(link.find('span').string)
#     # pages+=link.find('span') # append 메서드와 동일한 결과

# pages = pages[:-1]
# print(pages)