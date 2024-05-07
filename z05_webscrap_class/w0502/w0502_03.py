'''
1. 야놀자 홈페이지 이동
2. 검색창 클릭, 검색창에 호텔 입력
3. 날짜 선택
4. 6/5, 6/6 클릭
5. 확인버튼 클릭
6. 검색창 클릭 후 엔터키 입력
7. 검색 진행
8. 스크롤 이동 10번 반복v
9. 검색 결과가 나타나면 이미지, 제목 , 평점, 평가수, 숙박비 저장하시오.

- 오라클에서 table 생성
table명 : yanolja
yno, img, title, grade, grade_num, price

'''

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

url = "https://www.yanolja.com/"

browser = webdriver.Chrome()
browser.maximize_window()
browser.get(url)

time.sleep(1)

# 검색창 선택
elem = browser.find_element(By.XPATH,'//span[text()="무엇을 하고 놀까요?"]')
time.sleep(1)
elem.click()
time.sleep(1)

# 검색창에 '호텔' 입력
elem = browser.find_element(By.CLASS_NAME,'SearchInput_input__342U2')
elem.send_keys('호텔')
time.sleep(1)

# 날짜 입력칸 클릭
elem = browser.find_element(By.XPATH,'//*[@id="__next"]/div[1]/main/div/div[1]/form/div/div[2]/div[1]/button')
time.sleep(1)
elem.click()
time.sleep(1)

# 날짜 선택(6/5)
elem = browser.find_elements(By.XPATH,'//td[text()="5"]')
time.sleep(1)
elem[1].click()
time.sleep(1)

# 날짜 선택(6/6)
elem = browser.find_elements(By.XPATH,'//td[text()="6"]')
time.sleep(1)
elem[1].click()
time.sleep(1)

# 확인버튼 클릭
elem = browser.find_element(By.XPATH,'//button[text()="확인"]')
time.sleep(1)
elem.click()
time.sleep(1)

# 검색창 클릭 후 엔터키 입력
elem = browser.find_element(By.CLASS_NAME,'SearchInput_input__342U2')
elem.send_keys(Keys.ENTER) 
time.sleep(1)

# 검색 진행
time.sleep(5)

# 스크롤 이동 10번 반복
prev_height = browser.execute_script("return document.body.scrollHeight")
print("최초 높이 : ", prev_height)

for i in range(10):
    browser.execute_script("window.scrollTo(0, document.body.scrollHeight)")
    time.sleep(2)
    # 스크롤 높이 체크
    curr_height = browser.execute_script("return document.body.scrollHeight")
    if prev_height == curr_height:
        break
    prev_height = curr_height
    print(f"{i+1} 현재 높이 : ", curr_height)

# 검색 결과가 나타나면 이미지, 제목 , 평점, 평가수, 숙박비 저장하시오.
soup = BeautifulSoup(browser.page_source,'lxml')

with open("yanolja.html", 'w', encoding='utf-8') as f:
    f.write(soup.prettify())
# - 파일에서 가져오기
with open("yanolja.html", 'r', encoding='utf-8') as f:
    soup = BeautifulSoup(f,'lxml')

hotels = soup.find_all("div",{"class":"PlaceListItemText_container__fUIgA text-unit"})
# print(hotels)

# 이미지
# img = hotels[0].find("div",{"class":"PlaceListImage_imageText__2XEMn"})
# addImg = hotels[0].find("div",{"class":"PlaceListImage_imageText__2XEMn"}).style.find("http")
# print("이미지 링크 : ", img[addImg:])
# 제목
title = hotels[0].find("strong",{"class":"PlaceListTitle_text__2511B"}).strip()
print("제목 : ", title.text)
# 평점
grade = hotels[0].find("span",{"class":"PlaceListScore_rating__3Glxf"}).text
print("평점  : ", grade)
# 평가수
grade_num = hotels[0].find("span",{"class":"PlaceListScore_reviewInfo__3QSCU"})
print("평가수 : ", grade_num)
# 숙박비
# price = hotels[0].find()


time.sleep(100)