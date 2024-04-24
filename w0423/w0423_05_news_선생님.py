# 주식정보, 뉴스, 날씨를 메일로 전송해주는 프로그램 만들기
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import requests
from bs4 import BeautifulSoup

# 뉴스 번호, 제목, 이미지 가져오기

# selenium은 자동화프로그램
# browser = webdriver.Chrome()
# url = "https://news.naver.com/main/ranking/popularDay.naver?mid=etc&sid1=111"
# # 브라우저 페이지 열기
# browser.get(url)
# soup = BeautifulSoup(browser.page_source,'lxml')

url = "https://news.naver.com/main/ranking/popularDay.naver?mid=etc&sid1=111"
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36 Edg/123.0.0.0", "Accept-Language": "ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7"}
res = requests.get(url)
res.raise_for_status()
soup = BeautifulSoup(res.text,'lxml')

officeCard = soup.find("div",{"class":"_officeCard _officeCard0"})
ranks = officeCard.find_all("div",{"class":"rankingnews_box"})
print("개수 ", len(ranks)) #12개
for rank in ranks:
    lis = rank.find_all("li")
    print("제목 : ", lis[0].find("a",{"class":"list_title"}).text)
    
    
    print("li 개수 : ", len(lis)) # 5개
    print('-'*40)


