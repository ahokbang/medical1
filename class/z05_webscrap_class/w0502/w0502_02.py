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

# db에 저장, 차트 100까지 나오도록 출력하기
'''
테이블 명: melon
멜론 사이트에서 가져오기
0. 순번(시퀀스 번호) melon_seq
1. 순위 rank
2. 변동순위 v_rank 
3. 이미지, 
4. 제목, 
5. 가수, 
6. 좋아요 수 
'''

headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36 Edg/123.0.0.0", "Accept-Language": "ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7"}
browser = webdriver.Chrome()
browser.maximize_window()

url = 'https://www.melon.com/chart/index.htm'
browser.get(url)
time.sleep(2)

# find, find_all

soup = BeautifulSoup(browser.page_source,"lxml")

# 파일저장
# with open('melon.html', 'w', encoding='utf-8') as f:
#     f.write(soup.prettify())

# 파일 불러오기
# with open('melon.html','r',encoding='utf-8') as f:
#     soup = BeautifulSoup(f, 'lxml')


# tc에서 100 순위까지 출력 해보기
trs = soup.find_all("tr",{"id":"lst50"})

for tr in trs:
    rank = tr.find("span",{"class":"rank"})
    rank = int(rank.text.strip())
    print("순위 : ",rank)

    s_rank = tr.find("span",{"class":"rank_wrap"})
    v_rank = tr.find("span",{"class":"rank_wrap"})['title']
    print(v_rank)
    if v_rank =="순위 동일":
        v_rank = 0
    elif v_rank.find('단계 하락') != -1:
        v_rank = s_rank.find("span",{"class":"down"}).text
        v_rank = int(v_rank)*-1
    else: 
        v_rank = s_rank.find("span",{"class":"up"}).text
        v_rank = int(v_rank)        
    print("순위변동 : ",v_rank)

    img = tr.find("img")['src']
    print("이미지 : ",img)

    r_title = tr.find("div",{"class":"ellipsis rank01"})
    title = r_title.find("a").text.strip()
    print("제목 : ",title)

    r_singer = tr.find("div",{"class":"ellipsis rank02"})
    singer = r_singer.find("a").text.strip()
    print("가수 : ",singer)

    r_likeNum = tr.find("button",{"class":"button_etc like"})
    likeNum = int(r_likeNum.find("span",{"class":"none"}).nextSibling.strip().replace(",",""))
    print("좋아요수 : ",likeNum)

trs1 = soup.find_all("tr",{"id":"lst100"})
for tr1 in trs1:
    rank = tr1.find("span",{"class":"rank"})
    rank = int(rank.text.strip())
    print("순위 : ",rank)

    s_rank = tr1.find("span",{"class":"rank_wrap"})
    v_rank = tr1.find("span",{"class":"rank_wrap"})['title']
    print(v_rank)
    if v_rank =="순위 동일":
        v_rank = '-'
    elif v_rank.find('단계 하락') != -1:
        v_rank = s_rank.find("span",{"class":"down"}).text
        v_rank = int(v_rank)*-1
    elif v_rank.find('단계 상승') != -1:
        v_rank = s_rank.find("span",{"class":"up"}).text
        v_rank = int(v_rank)       
    else:
        v_rank = s_rank.find("span",{"class":"none"}).text
        v_rank = "New"
         
    print("순위변동 : ",v_rank)

    img = tr1.find("img")['src']
    print("이미지 : ",img)

    r_title = tr1.find("div",{"class":"ellipsis rank01"})
    title = r_title.find("a").text.strip()
    print("제목 : ",title)

    r_singer = tr1.find("div",{"class":"ellipsis rank02"})
    singer = r_singer.find("a").text.strip()
    print("가수 : ",singer)

    r_likeNum = tr1.find("button",{"class":"button_etc like"})
    likeNum = int(r_likeNum.find("span",{"class":"none"}).nextSibling.strip().replace(",",""))
    print("좋아요수 : ",likeNum)


'''
ranks = soup.find_all("div", {"class":"wrap t_center"})
# print(ranks[0])
rank = ranks[0].find_all("span",{"class":"rank"})
# print(rank)
wraps = soup.find_all("div", {"class":"wrap"})
# print(wraps)
v_rank = wraps.find_all("span",{"class":"bullet_icons rank_static"})
# print(v_rank)
img = wraps.find_all("img")
print(img["src"])

likeNum = tr.find("span", {"class":"cnt"}).text[5:].replace(",","")
'''
# v_ranks = soup.find_all("div", {"class":"wrap"})
# print(v_ranks)
# v_rank = v_ranks[0].find_all("span", {"class":"bullet_icons rank_static"})
# print(v_rank)
# # print(trs)
# # tds = trs.find_all("td", {"class":"wrap t_right"})
# ranks = trs.find("div", {"class":"wrap t_center"})
# print(ranks)
# rank = trs[0].find_all("span",{"class":"rank"}).text
# # print("1. 순위 : ",rank)


'''trs = soup.find_all("tr",{"class":"lst50"})
# print(trs)

for i, tr in enumerate(trs):
    print('[',i+1,'번째 ]')
    rank = tr.find("span",{"class":"rank"})
    print("순위 : ", rank.text.strip())

    s_rank = tr.find("span",{"class":"rank_wrap"})
    v_rank = tr.find("span",{"class":"rank_wrap"})['title']
    if v_rank == '순위 동일':
        v_rank = 0
    elif v_rank.find('단계 하락') != 1:
        v_rank = s_rank.find("span",{"class":"down"}).text
        v_rank = int(v_rank)*-1
    else : 
        v_rank = s_rank.find("span",{"class":"up"}).text
        v_rank = int(v_rank)
    print("순위 변동 : {:+d}".format(v_rank)) # + 부호 넣기

    img = tr.find("img")['src']
    print("이미지 : ", img)

    r_title = tr.find("div",{"class":"ellipsis rank01"})
    title = r_title.find("a")
    print("제목 : ", title.text.strip())

    r_singer = tr.find("div", {"class":"ellipsis rank02"})
    singer = r_singer.find("a")
    print("가수 : ", singer.text.strip())

    r_likeNum = trs[21].find("div", {"class":"button_etc like"})
    likeNum = r_likeNum.find("span",{"class":"none"}).nextSibling().strip()
    print("좋아요 수 : ", likeNum)

    print("좋아요 수 : ", likeNum)
    print('-'*50)
print()
'''
'''
for i, tr in enumerate(trs):
    
    print("[", i+1, "번째 ]")
    rank = tr.find("span",{"class":"rank"})
    print("순위 : ", rank.text.strip())

    v_rank = tr.find("span",{"class":"rank_wrap"})['title']
    if v_rank == '순위 동일':
        v_rank = 0
    else :
        v_rank =1
    print("순위 변동 : ", v_rank)
    img = tr.find("img")['src']
    print("이미지 : ", img)

    r_title = tr.find("div",{"class":"ellipsis rank01"})
    title = r_title.find("a")
    print("제목 : ", title.text.strip())

    r_singer = tr.find("div", {"class":"ellipsis rank02"})
    singer = r_singer.find("a")
    print("가수 : ", singer.text.strip())

    r_likeNum = tr.find("div", {"class":"button_etc like"})
    likeNum = r_likeNum.find("span",{"class":"cnt"}).nextSibling().strip()
    print("좋아요 수 : ", likeNum)
'''