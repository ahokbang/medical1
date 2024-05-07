'''
[ 3. 네이버 항공권 ]
- 웹스크래핑을 통해
- 6/26 ~ 6/27
- 항공사 출발시간 도착시간 소요시간 금액을
- db에 저장하시오.
- db에서
- 항공사별 그룹핑해서 출력하시오.
- 시간 검색기능을 구현하시오.
( 출발하려는 시간을 입력하세요. >> )
- 시간을 입력하면 입력된 시간 이후로 검색
- 없으면 검색한 데이터가 없다고 나옴.
* flight 테이블
fno - 숫자타입(4) 시퀀스
airline - 문자타입(100)
departure_time - 날짜타입
arrival_time - 날짜타입
flight_time - 문자타입(20)
price - 숫자타입(10)
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

url = "https://flight.naver.com/"

browser = webdriver.Chrome()
browser.maximize_window()
browser.get(url)
time.sleep(2)

# 가는 장소 선택 
elem = browser.find_element(By.XPATH,'//b[text()="ICN"]')
time.sleep(1)
elem.click()
time.sleep(1)

# 국내 선택
elem = browser.find_element(By.XPATH,'//button[text()="국내"]')
time.sleep(1)
elem.click()
time.sleep(1)

# 김포국제공항 선택
elem = browser.find_element(By.XPATH,'//i[text()="김포국제공항"]')
time.sleep(1)
elem.click()
time.sleep(1)

# 도착 장소 선택 
elem = browser.find_element(By.XPATH,'//b[text()="도착"]')
time.sleep(1)
elem.click()
time.sleep(1)

# 국내 선택
elem = browser.find_element(By.XPATH,'//button[text()="국내"]')
time.sleep(1)
elem.click()
time.sleep(1)

# 김포국제공항 선택
elem = browser.find_element(By.XPATH,'//i[text()="제주국제공항"]')
time.sleep(1)
elem.click()
time.sleep(1)

# 날짜선택
elem = browser.find_element(By.XPATH,'//button[text()="가는 날"]').click()
time.sleep()



time.sleep(100)
