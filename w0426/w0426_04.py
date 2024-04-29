import requests
import time
import random
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36 Edg/123.0.0.0", "Accept-Language": "ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7"}

url = 'https://watcha.com/browse/webtoon'

# 브라우저 열기
browser = webdriver.Chrome()
browser.maximize_window() # 창 최대화
browser.get(url)

# 스크롤 내리고 마지막 웹툰 제목 추출
# 스크롤 내리기
# 현재 스크롤 높이 검색
pre_height = browser.execute_script("return document.body.scollHeight")
print("최초 높이 : ", pre_height)

# 스크롤 이동
while True:
    browser.execute_script("window.scrollTo(0, document.body.scrollHeight)")
    time.sleep(2)
    
    # 재조정된 스크롤 높이
    curr_height = browser.execute_script("return document.body.scrollHeight")
    if pre_height == curr_height:
        break # 같으면 중단하고 빠져나옴.
    
    pre_height = curr_height
    print("현재 높이 : ", curr_height)
    
# 데이터 찾기
soup = BeautifulSoup(browser.page_source,"lxml")

# div = soup.find("div",{"class":"custom-q3k7bw e97af1k2"})   
# sections = div.find_all("section",{"class":"custom-1ddjhv e1n12t0f0"})
sections = soup.find_all("section",{"class":"custom-11ytuur e1134x5i3"})
print("section 개수 : ", len(sections))
uls = sections[-1].find("ul",{"class":"evjjsye0 custom-plh92q-Row e8ldpmn0"})
lis = uls.find_all("li",{"class":"w_exposed_cell e1bnpttb3 custom-vnoe9g-RowItem etpnybg1"})
print("li 개수 : ", len(lis))
alts = lis[0].find("img")
print(lis[0].find("img"))
print("제목 : ",alts["alt"])
input("Enter키 입력시 프로그램이 종료됩니다. >>")
# 화면 닫기
browser.quit()
    
    
    
    
    
    
    
    
# uls = soup.find("ul",{"class":"evjjsye0 custom-plh92q-Row e8ldpmn0"})
# lis = uls.find_all("li",{"class":"w_exposed_cell e1bnpttb3 custom-vnoe9g-RowItem etpnybg1"})
# print("li 개수 : ", len(lis))
# alts = lis[0].find("img")
# print(alts)
# print("제목 : ", alts["alt"])