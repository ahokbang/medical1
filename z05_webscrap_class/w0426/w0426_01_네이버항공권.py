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

# url = 'https://www.naver.com'
url = 'https://flight.naver.com/'

# 브라우저 열기
browser = webdriver.Chrome()
browser.maximize_window() # 창 최대화
browser.get(url)

# 접근방법 : 
# # - class: By.CLASS_NAME
# - id : By.ID
# - name : By.NAME
# - xpath : By.XPATH ==> 제일 정확하지만 생각보다 안 찾아져

# 찾는 방법(selenium) : find_element, find_elements
# 찾는 방법(BeautifulSoup) : find, find_all

time.sleep(2)

# 출발지 선택: 직접 입력 방법
# XPATH : b[text()="국내"] ==> b 태그 안에 국내라는 글자 찾아줘
#         b[contains(text())="국"] ==> 국이 포함되어 있는 거 찾아줘
#         b[@class="send"] ==> b 태그 중에 class가 send인 거 찾아줘
#         b[@id="send"] ==> id의 경우에도 @id 
# // : 모든 페이지라는 의미
elem = browser.find_element(By.XPATH,'//b[text()="ICN"]') # b태그
time.sleep(1)
elem.click() 

# 국내 선택
time.sleep(1)
elem = browser.find_element(By.XPATH,'//button[text()="국내"]')
time.sleep(1)
elem.click()

# 김포국제공항 선택
# elem = browser.find_element(By.XPATH,'//i[text()="김포국제공항"]')
time.sleep(1)
elem = browser.find_element(By.XPATH,'//i[contains(text(),"김포국제공항")]')
time.sleep(1)
elem.click()

# 도착지 선택 
time.sleep(1)
elem = browser.find_element(By.XPATH,'//b[text()="도착"]')
time.sleep(1)
elem.click()

# 국내 선택
time.sleep(1)
elem = browser.find_element(By.XPATH,'//button[text()="국내"]')
time.sleep(1)
elem.click()

# 제주국제공항 선택
time.sleep(1)
elem = browser.find_element(By.XPATH,'//i[contains(text(),"제주국제공항")]')
time.sleep(1)
elem.click()

# 가는 날 선택
time.sleep(1)
elem = browser.find_element(By.XPATH,'//button[text()="가는 날"]')
time.sleep(1)
elem.click()

# 가는 날짜 선택 : 5/14
time.sleep(1)
# 4, 5, 6월에 14일이 존재하므로 elements로 찾기
elem = browser.find_elements(By.XPATH,'//b[text()="14"]')
print("14일 개수 : ",len(elem))
time.sleep(1)
elem[1].click()

# 오는 날짜 선택
time.sleep(1)
elem = browser.find_elements(By.XPATH,'//b[text()="15"]')
print("15일 개수 : ",len(elem))
time.sleep(1)
elem[1].click()

# 인원 선택 : 성인 2명, ==> <button>에 "성인" 포함되어 있는 거 찾음. class로 안 찾아져
elem = browser.find_element(By.XPATH,'//button[contains(text(),"성인")]')
time.sleep(1)
elem.click()

# 인원 추가
elem = browser.find_element(By.XPATH,'//button[@Class="searchBox_outer__9n6IB"]')
time.sleep(1)
elem.click()

# 항공권 검색
elem = browser.find_element(By.XPATH,'//span[text()="항공권 검색"]')
time.sleep(1)
elem.click() # 화면닫기
elem.click() # 검색하기

# 항공권 검색하는데 시간이 걸림
time.sleep(7) # 대기 시간

# 화면 대기 함수
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# 브라우저가 최대 30초까지 대기, 어떤 요소가 나타날때까지
elem = WebDriverWait(browser, 30).until(EC.presence_of_all_elements_located((By.XPATH,'//div[@class="domestic_Flight__sK0eA"]')))
print(elem)
print(elem[0].text)


# 화면 스크롤 내리기
## 현재 스크롤 높이 검색
prev_height = browser.execute_script("return document.body.scrollHeight")
print("최초 높이 : ", prev_height)

# 스크롤 이동
while True : 
    browser.execute_script("window.scrollTo(0, document.body.scrollHeight)")
    time.sleep(2)

    # 재조정된 스크롤 높이
    curr_height = browser.execute_script("return document.body.scrollHeight")
    if prev_height == curr_height:
        break # 같으면 중단하고 빠져나옴.

    prev_height = curr_height
    print("현재 높이 : ", curr_height)

# 웹스크래핑을 해서 정보를 가져오기
# 항공권 정보 가져오기

input("Enter 키 입력 시 프로그램이 종료됩니다.")
browser.quit()

# time.sleep(100)
