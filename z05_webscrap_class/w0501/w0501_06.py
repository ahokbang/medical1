# import oracledb

# conn = oracledb.connect(user='ora_user', password='1111', dsn='localhost:1521/xe')
# cursor = conn.cursor()

# sql = ""


# cursor.close()
# conn.close()

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

url = 'https://www.yeogi.com/domestic-accommodations?searchType=KEYWORD&keyword=%ED%98%B8%ED%85%94&checkIn=2024-06-05&checkOut=2024-06-06&personal=2&freeForm=true'

browser = webdriver.Chrome()
browser.maximize_window()
browser.get(url)

time.sleep(2)

# text 소스를 html 소스로 파싱
soup = BeautifulSoup(browser.page_source,"lxml")

# 파일 저장
# with open("yeogi.html", 'w', encoding='utf-8') as f:
#     f.write(soup.prettify())

# html 파일에서 가져오기
# with open("yeogi.html", 'r', encoding='utf-8') as f:
#     soup = BeautifulSoup(f,'lxml')

# 1개만 추출
# aes = soup.find_all("a",{"class":"gc-thumbnail-type-seller-card css-wels0m"})
# # print(a)
# # print(len(a))
# # print(a[0])
# name = aes[0].find("h3",{"class":"gc-thumbnail-type-seller-card-title css-1asqkxl"}).text
# print("숙소명 : ", name)
# cite = aes[0].find("span",{"class":"css-1rzfout"}).text
# print("지역 : ", cite)
# rank = aes[0].find("span", {"class":"css-9ml4lz"}).text
# print("평점 : ", rank)
# review = aes[0].find("span", {"class":"css-oj6onp"}).text
# print("평가수 : ", review[0:4])
# img = aes[0].find("img")
# print("이미지링크 : ", img["src"])
# price = aes[0].find("span",{"class":"css-5r5920"}).text
# print("가격 : ", price,'원')

# 상위 5개 추출
# aes = soup.find_all("a",{"class":"gc-thumbnail-type-seller-card css-wels0m"})
# for i, a in enumerate(aes[0:5]):
#     print("[",i+1,"번째 ]")
#     name = a.find("h3",{"class":"gc-thumbnail-type-seller-card-title css-1asqkxl"}).text
#     print("숙소명 : ", name)
#     cite = a.find("span",{"class":"css-1rzfout"}).text
#     print("지역 : ", cite)
#     rank = a.find("span", {"class":"css-9ml4lz"}).text
#     print("평점 : ", rank)
#     review = a.find("span", {"class":"css-oj6onp"}).text
#     print("평가수 : ", review[0:4])
#     img = a.find("img")
#     print("이미지링크 : ", img["src"])
#     price = a.find("span",{"class":"css-5r5920"}).text
#     print("가격 : ", price,'원')
#     print('-'*95)
# print()

# 전체 페이지 ==> 이미지, 가격이 에러 나기도 안나기도 해...
aes = soup.find_all("a",{"class":"gc-thumbnail-type-seller-card css-wels0m"})

for i, a in enumerate(aes):
    print("[",i+1,"번째 ]")
    name = a.find("h3",{"class":"gc-thumbnail-type-seller-card-title css-1asqkxl"}).text
    print("숙소명 : ", name)
    cite = a.find("span",{"class":"css-1rzfout"}).text
    print("지역 : ", cite)
    rank = a.find("span", {"class":"css-9ml4lz"}).text
    print("평점 : ", rank)
    review = a.find("span", {"class":"css-oj6onp"}).text
    print("평가수 : ", review)
    # print("평가수 : ", review[0:4])
    img = a.find("img")
    print("이미지링크 : ", img["src"])
    price = a.find("span",{"class":"css-5r5920"}).text
    print("가격 : ", price,'원')
    print('-'*95)
print()
