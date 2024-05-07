import requests
import time
import random
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36 Edg/123.0.0.0", "Accept-Language": "ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7"}

# url = 'https://www.naver.com'
url = 'https://flight.naver.com/'

# 브라우저 열기
browser = webdriver.Chrome()
# 창 최대화
browser.maximize_window()
browser.get(url)

# # 요소선택
# elem = browser.find_element(By.NAME,'query')
# # 2. 검색창 네이버항공권 입력
# elem.send_keys('네이버항공권')
# elem.send_keys(Keys.ENTER)

# elem = browser.find_element(By.CLASS_NAME,'link_name')
# elem.click()

# # 네이버항공권 창으로 이동
# # 원본창[0], 새창[1], 새창[2]
# browser.switch_to.window(browser.window_handles[1])
# -------------------------------------------------------------------
# 출발부분 클릭 : XPATH
elem = browser.find_element(By.XPATH,'//*[@id="__next"]/div/main/div[4]/div/div/div[2]/div[1]/button[1]')
elem.click()
time.sleep(2)

# 국내 클릭 : CLASS_NAME 사용, XPATH 안됨
# elem = browser.find_element(By.XPATH,'//*[@id="__next"]/div/main/div[11]/div[2]/section/section/button[1]')
elem = browser.find_element(By.CLASS_NAME,'autocomplete_Collapse__tP3pM')
elem.click()
time.sleep(2)

# 김포 클릭 : CLASS_NAME 복수개 가져오기 ==> 복수 배열로 가져오기
# elem = browser.find_element(By.CLASS_NAME,'autocomplete_Airport__3_dRP')
elem = browser.find_elements(By.CLASS_NAME,'autocomplete_Airport__3_dRP')[2]
elem.click()
# -------------------------------------------------------------------
# 도착부분 클릭 : XPATH
elem = browser.find_element(By.XPATH,'//*[@id="__next"]/div/main/div[4]/div/div/div[2]/div[1]/button[2]')
elem.click()
time.sleep(2)

# 국내 클릭 : CLASS_NAME 사용, XPATH 안됨
# elem = browser.find_element(By.XPATH,'//*[@id="__next"]/div/main/div[11]/div[2]/section/section/button[1]')
elem = browser.find_element(By.CLASS_NAME,'autocomplete_Collapse__tP3pM')
elem.click()
time.sleep(2)

# 제주 클릭 : CLASS_NAME 복수개 가져오기 ==> 복수 배열로 가져오기
# elem = browser.find_element(By.CLASS_NAME,'autocomplete_Airport__3_dRP')
elem = browser.find_elements(By.CLASS_NAME,'autocomplete_Airport__3_dRP')[1]
elem.click()
# -------------------------------------------------------------------
# 가는 날짜 부분 선택
elem = browser.find_element(By.XPATH,'//*[@id="__next"]/div/main/div[4]/div/div/div[2]/div[2]/button[1]')
elem.click()
time.sleep(2)

# 가는 날짜 선택(5/14)
elem = browser.find_element('')
elem.click()
time.sleep(2)


time.sleep(100)



''' 
1. 네이버 페이지 이동
2. 검색창 네이버항공권 입력
3. 검색창 엔터키 입력
-- 네이버 항공권 검색 이동
4. 네이버 항공권 클릭
-- 네이버 항공권 페이지 이동
5. 출발지역 선택 - 김포
6. 도착지역 선택 - 제주
7. 가는 날 선택: 5/5
8. 오는 날 선택 : 5/6
9. 성인 2인 선택
10. 항공권 검색 버튼 클릭
11. 검색하는 동안 대기
12. 검색된 항공권 스크롤 해서 하단 이동 반ㅂ고
13. 13만원 이하인 항공권 정보 저장 
'''