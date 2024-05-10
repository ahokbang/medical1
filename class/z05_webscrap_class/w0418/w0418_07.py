import requests
from bs4 import BeautifulSoup
url = "https://finance.naver.com/sise/lastsearch2.naver"
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36"}
res = requests.get(url, headers)
res.raise_for_status()

soup = BeautifulSoup(res.text,"lxml")

type_tr = soup.find("tr",{"class":"type1"})
print("th : ", type_tr.th) # 첫번째 th 출력, [순위]
print("find_next_sibling : ", type_tr.th.find_next_sibling("th")) # 현재 th에서 다음 th를 찾아줌, [종목명]
print("next : ", type_tr.th.next) # th 태그 다음 단락
print("next2 : ", type_tr.th.next.next) # 공란
print("next3 : ", type_tr.th.next.next.next) # [종목명]
print("find_next_siblings : ", type_tr.th.find_next_siblings("th")) # 현재 th에서 다음 th 모두를 찾아줌, [종목명]

# 이전은 find_previous, 바로 앞 요소(들)는(은) find_previous_sibling(s)





