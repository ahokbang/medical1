import requests
from bs4 import BeautifulSoup
url = "https://finance.naver.com/sise/lastsearch2.naver"
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36"}
res = requests.get(url, headers)
res.raise_for_status()

soup = BeautifulSoup(res.text,"lxml")

type_tr = soup.find("tr",{"class":"type1"})
trs = type_tr.find_next_siblings("tr")
# print("trs : ", trs)
print("첫째줄 출력(삼성전자 행): ", trs[1])
print("href 값 출력 : ", trs[1].td.find_next_sibling("a"))   # 내가 한 거 틀림
print("href 값 출력 : ", trs[1].a['href'])
# 선생님 방법
t_table = soup.find("table",{"class":"type_5"})
print("href 값 출력 : ", t_table.a['href'])










