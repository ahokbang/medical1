'''
[ 2. 쿠팡 - 노트북   ]
검색 - 노트북으로 해서
총 1,2,3페이지 까지 검색해서 ==> 1페이지만
콘솔에 출력하고, db에 저장하시오.
- coupang 테이블
cno 시퀀스
title 문자타입(100)
img 문자타입(100)
price 숫자타입(10)
grade 숫자타입(10)
eval_num 숫자타입(10)
제목, 이미지, 금액, 평점, 평가수
'''
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

url = "https://www.coupang.com/np/search?component=&q=%EB%85%B8%ED%8A%B8%EB%B6%81&channel=user"

browser = webdriver.Chrome()
browser.maximize_window()
browser.get(url)

time.sleep(2)

soup = BeautifulSoup(browser.page_source,"lxml")

ul_sch = soup.find("ul",{"class":"search-product-list"})
print(ul_sch)
lis = ul_sch.find_all("li")
print(lis)

for i, li in enumerate(lis):
    print(f"[ {i+1}번째 ]")
    title = li.find("div",{"class","name"}).text
    print("제목 : ", title)


