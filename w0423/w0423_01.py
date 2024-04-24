import time
from selenium import webdriver
import requests
from bs4 import BeautifulSoup

# requests로 정보 가져오기
url = "https://comic.naver.com/bestChallenge"
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36 Edg/123.0.0.0", "Accept-Language": "ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7"}
res = requests.get(url, headers=headers)
res.raise_for_status()

soup = BeautifulSoup(res.text,'lxml')

print(soup.prettify())

with open("webtoons1.html",'w',encoding='utf-8') as f:
    f.write(soup.prettify())
    
print("완료")



# browser = webdriver.Chrome()
# browser.get("https://www.naver.com/")

# time.sleep(10)

# elem = browser.find_element("MyView-module__link_login___HpHMW")
# elem
# elem.click()














'''
Requests : 웹 페이지 읽어오기, 동적 웹 페이지 x, 빠름
selenium : 사이트 자동화 프레임워크, 동접 웹 페이지 o, 느림

'''