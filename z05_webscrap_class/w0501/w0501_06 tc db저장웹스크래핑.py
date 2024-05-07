import oracledb
import requests
import time
import random
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pyautogui

# DB 연결부분
conn = oracledb.connect(user='ora_user', password='1111', dsn='localhost:1521/xe')
cursor = conn.cursor()

headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36 Edg/123.0.0.0", "Accept-Language": "ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7"}
browser = webdriver.Chrome()
browser.maximize_window()

# 5페이지까지 돌리고 싶어
# for i in range(5):
url = 'https://www.yeogi.com/domestic-accommodations?searchType=KEYWORD&keyword=%ED%98%B8%ED%85%94&checkIn=2024-06-05&checkOut=2024-06-06&personal=2&freeForm=true&page=1'
browser.get(url)
time.sleep(2)

# text 소스를 html 소스로 파싱
soup = BeautifulSoup(browser.page_source,"lxml")

## find_all
hotels = soup.find_all("a",{"class":"gc-thumbnail-type-seller-card css-wels0m"})
print("전체 개수 : ", len(hotels))
for idx, hotel in enumerate(hotels):
    print("[",idx+1,"번째 ]")
    # 1. 제목
    title = hotel.find("h3",{"class":"gc-thumbnail-type-seller-card-title css-1asqkxl"})
    title = title.text
    # print("titles 개수 : ", len(title))
    print("1. 제목 : ", title)
    # 2. 지역
    try: 
        region = hotel.find("span",{"class":"css-1rzfout"})
        region = region.text
        print("2. 지역 : ", region)
    except:
        region = ""
        print(f"2. 지역 : {region}")        
    # 3. 평점
    score = hotel.find("span", {"class":"css-9ml4lz"})
    score = float(score.text)
    print("3. 평점 : ", score)
    # 4. 평가수 
    member = hotel.find("span",{"class":"css-oj6onp"})
    member = int(member.text[:-4].replace(",",""))
    print("4. 평가수 : ", member)
    # 5. 이미지링크
    try:
        img = hotel.find("img")["src"]
        # print(img)
        # img=img["src"]
        # img = hotel.find("img",{"class":"thumbnail-image"})["src"]    
        print("5. 이미지링크 : ", img)
    except:
        img = ""
        print(f"5. 이미지링크 : {img}")
    # 6. 가격
    try : 
        price = hotel.find("span",{"class":"css-5r5920"})
        price = int(price.text.replace(",",""))
        print("6. 가격 : ", price)       
    except: 
        price = 0
        print(f"6. 가격 : {price}")
    print('-'*10)

    # DB 저장
    sql = f"insert into yeogi values (yeogi_seq.nextval,'{title}','{region}',{score},{member},'{img}',{price})"
    cursor.execute(sql)    
    
print('-'*30)

cursor.execute('commit')
cursor.close()
conn.close()