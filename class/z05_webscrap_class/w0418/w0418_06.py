import requests
from bs4 import BeautifulSoup
url = "https://finance.naver.com/sise/lastsearch2.naver"
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36"}
res = requests.get(url, headers=headers)
res.raise_for_status

soup = BeautifulSoup(res.text,"lxml")
# ---------------------------------------- 여기까지가 기본 구문

# 삼성전자행 출력해보기

# print(soup.find("table",{"class":"type_5"}))
t_table = soup.find("table",{"class":"type_5"})
trs = t_table.find_all("tr")
tr = trs[2]
# print(tr)
tds = trs[2].find_all("td")
for td in tds:
    # print(td.text)
    print(td.text.strip()) # 공백 제거









''' 내가 한 거 
# print(soup.find("tr",{"class":"type1"})) # attr 생략 가능
type_td_tltle = soup.find("td",{"class":"tltle"})
type_td_no = soup.find("td",{"class":"no"})
type_td_number = soup.find_all("td",{"class":"number"})

print(type_td_tltle)
print(type_td_no.text)
print(type_td_number)
'''