# https://jumin.mois.go.kr/ageStatMonth.do
# 서울특별시, 인천직할시, 경기도 3개의 인구를 웹스크래핑해서 
# 서울특별시 : 인구
# 인천직할시 : 인구
# 경기도 : 인구
# 합계 : 인구를 출력하시오.

import time
from selenium import webdriver
import requests
from bs4 import BeautifulSoup
url = "https://jumin.mois.go.kr/ageStatMonth.do"
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36 Edg/123.0.0.0", "Accept-Language": "ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7"}
res = requests.get(url, headers=headers)
res.raise_for_status()

soup = BeautifulSoup(res.text,'lxml')

# print(soup.prettify())

with open("population.html",'w',encoding='utf-8') as f:
    f.write(soup.prettify())
# print("완료")

# print(soup.find("td",{"class":"td_admin th1"}))
table = soup.find("table",{"class":"tbl_type1"})
trs = table.find_all("tr")
print('-'*40)
# print(len(trs))
su = int(trs[4].find("td",{"title":"2024년 03월 / 계"}).text.replace(",","")) # 서울특별시
ic = int(trs[7].find("td",{"title":"2024년 03월 / 계"}).text.replace(",","")) # 인천직할시
gg =  int(trs[12].find("td",{"title":"2024년 03월 / 계"}).text.replace(",","")) # 경기도

print("서울특별 인구 : ", '{0:,}'.format(su),"명")
print("인천직할시 인구 : ",'{0:,}'.format(ic),"명") 
print("경기도 인구 : ",'{0:,}'.format(gg),"명") 
print("서울특별시, 인천직할시, 경기도 인구 총 합계 : ", '{0:,}'.format(su+ic+gg), "명")

