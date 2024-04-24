# https://jumin.mois.go.kr/ageStatMonth.do
# 서울특별시, 인천직할시, 경기도 3개의 인구를 웹스크래핑해서 
# 서울특별시 : 인구
# 인천직할시 : 인구
# 경기도 : 인구
# 합계 : 인구를 출력하시오.

import time
from selenium import webdriver
import requests
from bs4 import BeautifulSoup

url = "https://jumin.mois.go.kr/ageStatMonth.do"
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36 Edg/123.0.0.0", "Accept-Language": "ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7"}
res = requests.get(url, headers=headers)
res.raise_for_status()

soup = BeautifulSoup(res.text,'lxml')

## 선생님 코드
# 브라우저 페이지 열기
browser = webdriver.Chrome()
browser.get(url)
time.sleep(3)

soup = BeautifulSoup(browser.page_source,'lxml')
# with open('jumin.html','w',encoding='utf-8') as f:
#     f.write(soup.prettify())

# 테이블 검색
tb = soup.find("table",{"id":"contextTable"})
# tbody 검색
tbody = tb.find("tbody")

# td 검색
trs = tbody.find_all("tr")
print("trs 개수 : ", len(trs))
print('-'*40)
print(trs[1])
print('-'*40)
# tds = trs[0].find_all("td", {"title":"2024년 03월 / 계"})
tds = trs[1].find_all("td")
seoul = tds[2].text
print("서울특별시 인구 수 : ", seoul)
tds = trs[4].find_all("td")
incheon = tds[2].text
print("인천광역시 인구 수 : ", incheon)
tds = trs[9].find_all("td")
gyunggi = tds[2].text
print("경기도 인구 수 : ", gyunggi)

total = int(seoul.replace(",",""))+int(incheon.replace(",",""))+int(gyunggi.replace(",",""))
print("수도권 인구수 : ", format(total, ","))