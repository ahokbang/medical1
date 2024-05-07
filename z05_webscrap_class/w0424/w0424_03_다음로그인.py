import requests
import time
import random
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36 Edg/123.0.0.0", "Accept-Language": "ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7"}

url = "https://www.daum.net/"

# 크롬브라우저 열기
browser = webdriver.Chrome()
#다음 페이지 이동
browser.get(url)
time.sleep(3)
# 로그인 버튼 선택 
# elem = browser.find_element(By.CLASS_NAME,"btn_login")
# 또는 Xpath 이용
elem = browser.find_element(By.XPATH,'//*[@id="loginMy"]/div/div[1]/div/a')
# 로그인 버튼 클릭
elem.click()

time.sleep(random.randint(3,7))


''' 1. 내가 한거
# 자동화 방지를 위한 자바스크립트 활용 데이터 입력
input_js = 'document.getElementById("loginId--1").value="{id}";\
            document.getElementById("password--2").value="{pw}"; \
            '.format(id='aaaa', pw='1111')
time.sleep(random.randint(3,7))
# 자바스크립트 명령어 실행
browser.execute_script(input_js)

time.sleep(random.randint(3,7))
elem = browser.find_element(By.CLASS_NAME,"btn_g highlight submit")   
time.sleep(random.randint(3,7))

# 로그인 버튼 클릭
elem.click()

# 완료
time.sleep(100)
'''

# 2. 선생님
# 자동화 방지를 위한 자바스크립트 활용 데이터 입력
input_js = 'document.getElementById("loginId--1").value="{id}";\
            document.getElementById("password--2").value="{pw}"; \
            '.format(id='aaaa', pw='1111')
time.sleep(random.randint(3,7))
# 자바스크립트 명령어 실행
browser.execute_script(input_js)


# # 이메일
# elem = browser.find_element(By.NAME, 'loginId')
# elem.send_keys('aaa@daum.net')
# time.sleep(2)

# # 이메일
# elem = browser.find_element(By.NAME,'password')
# elem.send_keys('1111')
# time.sleep(2)

time.sleep(random.randint(3,7))
elem = browser.find_element(By.XPATH,'//*[@id="loginMy"]/div/div[1]/div/a')   
time.sleep(random.randint(3,7))

# 로그인 버튼 클릭
elem.click()