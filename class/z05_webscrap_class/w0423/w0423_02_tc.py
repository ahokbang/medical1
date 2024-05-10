from selenium import webdriver
import time
import requests
from bs4 import BeautifulSoup  as bs



# selenium으로 정보 가져오기
browser = webdriver.Chrome()
browser.get("https://comic.naver.com/bestChallenge")
time.sleep(3)
soup = BeautifulSoup(browser.page_source,'lxml')
with open("webtoons2.html",'w',encoding='utf-8') as f:
    f.write(soup.prettify())
# print("완료")

# 실시간 인기 베스트도전 1등~10등, 순위, 웹툰명, 작가명, 이미지 가져오기 
list_ul = soup.find("ul",{"class":"AsideList__content_list--FXDvm AsideList__challenge--HeKuU"})
print(list_ul)

lis = list_ul.find_all("li")
print("-"*40)

# 동영상 다시 보기
print("개수 : ", len(lis))
print('-'*40)

for li in lis:
    w_rank = li.find("strong", {"class":"AsideList__ranking--sNPZy"}).text
    title = li.find('span',{'class':'text'}).text
    img_url = li.find("img",{"class":"Poster__image--d9XTI"})['src']
    print("등수 : ", w_rank)
    print("제목 : ", title)
    print("작가 : ", li.find("a",{"class":"ContentAuthor__author--CTAAP"}).text)
    print("이미지링크 : ", img_url)
    # 이미지파일 저장방법
    img_poster = requests.get(img_url)
    # img_poster = requests.get(img_url, headers=headers)
    with open('weebtoons_{}.jpeg'.format(w_rank),'wb') as f:
        f.write(img_poster.content)
    print('-'*40)
    
    