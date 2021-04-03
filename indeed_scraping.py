
import re
import requests
from bs4 import BeautifulSoup


indeed_result = requests.get('https://kr.indeed.com/%EC%B7%A8%EC%97%85?q=java&limit=999&start=9999')

indeed_soup = BeautifulSoup(indeed_result.text, 'html.parser')

pagination = indeed_soup.find('div', {'id':'searchCountPages'})
# print(pagination.string.strip().split()[0][:-3])     # ''페이지' 한글 3글자만 벗겨냈음. 즉 한글만 적용가능
str_list_max_page = re.findall('\d+', pagination.string.strip().split()[0]) # 모든 문자에서 숫자만 뽑아낸것
max_page = int(str_list_max_page[0])


# links = pagination.findAll('a')

# pages = []
# for link in links:
#     pages.append(link.find('span').string)
#     # pages+=link.find('span') # append 메서드와 동일한 결과

# pages = pages[:-1]
# print(pages)