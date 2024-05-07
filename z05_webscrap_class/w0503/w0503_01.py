
# 역대관객순
# 이미지, 제목, 누적관객수, 개봉일 
# 이미지 저장까지 해야 함.
# 2023, 2022, 2021, 2020

# 콘솔창에 출력하고 DB에 저장

'''
 DB
 테이블 명 : daum_movie
 dno : 시퀀스
 title 문자타입(100)
 img 문자타입(100)
 audience 숫자타입(10)
 ddate 날짜타입
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

url = "https:/c/search.daum.net/search?w=tot&q=%EC%97%AD%EB%8C%80%EA%B4%80%EA%B0%9D%EC%88%9C%EC%9C%84&DA=MOR&rtmaxcoll=MOR"

browser = webdriver.Chrome()
browser.maximize_window()
browser.get(url)
time.sleep(2)

# 파일저장
# with open('daum_movie.html','w',encoding='utf-8') as f:
#     f.write(soup.prettify())
# 파일열기
with open('daum_movie.html','r',encoding='utf-8') as f:
    soup =  BeautifulSoup(f,'lxml')

# 년도 선택
elem = browser.find_element(By.XPATH,'//a[text()=2023]')
time.sleep(1)
elem.click()
time.sleep(1)

soup = BeautifulSoup(browser.page_source,'lxml')

movies = soup.find_all("div",{"class":"pdt2"})
print(movies)
print(len(movies)) # 3 ==> 3page
# mvs = movies.find("div",{"class":"c-item-content"})
# print("영화 리스트 : ",mvs)
# print("len(mv) : ", len(mvs))

# mv = mvs[0].find_all("li")
# title = mv[0].find("strong",{"class":"tit-g clamp-g"}).text
# print("영화제목 : ",title)
# title = mv[1].find("strong",{"class":"tit-g clamp-g"}).text
# print("영화제목 : ",title)
# audience = mv[0].find("p",{"class":"conts-desc clamp-g"}).text
# print("누적 관객수 : ", audience)
# ddate = mv[0].find("span",{"class":"conts-subdesc clamp-g"}).text
# print("개봉일: ", ddate)



# # mv = mvs[0].find_all("li")

# for i, mv in enumerate(mvs):
#     # print("영화 리스트 : ",mv)
#     # print("len(mv) : ", len(mv))
#     print(f"[ {i+1}위 ]")
#     title = mv.find("strong",{"class":"tit-g clamp-g"}).text
#     print("영화제목 : ",title)
#     audience = mv.find("p",{"class":"conts-desc clamp-g"}).text
#     print("누적 관객수 : ", audience)
#     ddate = mv.find("span",{"class":"conts-subdesc clamp-g"}).text
#     print("개봉일: ", ddate)











'''
# img 파일 저장
with open(f"movie_{i}.jpg","wb") as f:
        re_img = requests.get(img_screen) #url링크를 다시 읽어와야 함.
        f.write(re_img.content) # 파일이름의 내용을 저장
'''