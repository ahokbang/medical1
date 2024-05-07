'''
다음 > 영화순위 > 역대 관객순 > 2019 > 2020
year title num rating
2019 극한직업 1626 3.6
2020 남산의 부장들 475 3.5
2021 모가디슈 361 3.6
2022 범죄도시2 1269 3.5
2023 서울의 봄 1312 4.1
웹스크래핑으로 데이터 가져와서 dict type으로 데이터 저장 후
DataFrame으로 출력
'''
# data = {
#     'year':[2019,2020,2021,2022,2023],
#     'title':[],
#     'num':[],
#     'rating':[]
# }

import oracledb
import requests
import time
import random
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
# 화면이 나타나는 것을 확인
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pyautogui

headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36 Edg/123.0.0.0", "Accept-Language": "ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7"}

# 2019년도
url = 'https://search.daum.net/search?w=tot&q=2019%EB%85%84%EC%98%81%ED%99%94%EC%88%9C%EC%9C%84&DA=MOR&rtmaxcoll=MOR'

browser = webdriver.Chrome()
browser.maximize_window()
browser.get(url)
time.sleep(2)

soup = BeautifulSoup(browser.page_source,'lxml')

# 파일저장
# with open('daum_movie1.html','w',encoding='utf-8') as f:
#     f.write(soup.prettify())
# 파일열기
with open('daum_movie1.html','r',encoding='utf-8') as f:
    soup =  BeautifulSoup(f,'lxml')

list = soup.find("ul",{"class":"c-list-basic ty_flow35"})
# print(list)
lis = list.find_all("li")
# print(lis[0])
title = lis[0].find("strong",{"class":"tit-g clamp-g"}).text.strip()
print("제목 : ", title)
num = lis[0].find("p",{"class":"conts-desc clamp-g"})
num = num.text.strip()[-3:6].replace(",","")
print("관객 수 : ", num)

# 평점 가져오기
elem = browser.find_element(By.CLASS_NAME,"wrap_thumb")
# elem = browser.find_element(By.XPATH,'//stron[@class="tit-g clamp-g"]')
elem.click()
time.sleep(1)

soup = BeautifulSoup(browser.page_source,'lxml')

d_rating = soup.find("sapn",{"class":"gem-star-point"})
rating = d_rating.find("sapn",{"class":"ico-pmp"})
print("평점 : ", rating)

# dict 저장
