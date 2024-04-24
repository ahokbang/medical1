import time
from selenium import webdriver
import requests
from bs4 import BeautifulSoup

# selenium으로 정보 가져오기
browser = webdriver.Chrome()
browser.get("https://comic.naver.com/bestChallenge")
time.sleep(3)
soup = BeautifulSoup(browser.page_source,'lxml')
with open("webtoons2.html",'w',encoding='utf-8') as f:
    f.write(soup.prettify())
# print("완료")

# 실시간 인기 베스트도전 1등~10등, 순위, 웹툰명, 작가명, 이미지 가져오기 # 와!! 처음으로 내가 해냈다!!! ㅠㅜㅠㅜㅠㅜ
# print(soup.find("div",{"id":"container"}))
contain = soup.find("div",{"id":"container"})
# print(contain.find("div",{"class":"component_wrap"}))
wraps = contain.find("div",{"class":"Aside__aside_wrap--iF5ju"}) 
wrap = wraps.find("ul", {"class":"AsideList__content_list--FXDvm AsideList__challenge--HeKuU"})
# print(wrap)
lis = wrap.find_all("li",{"class":"AsideList__item--i30ly"})
print(lis)
print("순위 : ", lis[0].find("strong",{"class":"AsideList__ranking--sNPZy"}).text)
print("웹툰명 : ", lis[0].find("span",{"class":"text"}).text)
print("작가명 : ", lis[0].find("a",{"class":"ContentAuthor__author--CTAAP"}).text)
print("이미지 : ", lis[0].find("img",{"class":"Poster__image--d9XTI"})['src'])


for li in lis[0:10]:
    print("순위 : ", li.find("strong",{"class":"AsideList__ranking--sNPZy"}).text)
    print("웹툰명 : ", li.find("span",{"class":"text"}).text)
    print("작가명 : ", li.find("a",{"class":"ContentAuthor__author--CTAAP"}).text)
    print("이미지 : ", li.find("img",{"class":"Poster__image--d9XTI"})['src'])

    



# requests로 정보 가져오기
# url = "https://comic.naver.com/bestChallenge"
# headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36 Edg/123.0.0.0", "Accept-Language": "ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7"}
# res = requests.get(url, headers=headers)
# res.raise_for_status()

# soup = BeautifulSoup(res.text,'lxml')

# print(soup.prettify())

# with open("webtoons1.html",'w',encoding='utf-8') as f:
#     f.write(soup.prettify())
  
# print("완료")



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