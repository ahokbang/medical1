import requests
from bs4 import BeautifulSoup
url = "https://finance.naver.com/sise/lastsearch2.naver"
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36"}
res = requests.get(url,headers=headers)
res.raise_for_status()
soup = BeautifulSoup(res.text,"lxml")
# print(soup)
# stock = soup.find("div",{"class":"box_type_l"})
s_all = soup.find("div", {"class":"box_type_l"})
tr_list = s_all.find_all("tr") # s_all 중에 tr이 몇개 있는지 
# list 타입
print(len(tr_list)) # 50 
print(type(tr_list)) # <class 'bs4.element.ResultSet> # 자바나 C에서 ResultSet은 list
samsung = tr_list[2] # 삼성은 tr 3번째에 있어 ==> tr_list[2]
print(samsung)
# print(samsung.find("a", {"class":"tltle"}).text)
print(samsung.find("a").text) # 이렇게 직혀도 나와
td_list = samsung.find_all("td")
print("순위 :" , td_list[0].text)
# print("종목명 : ", td_list[1].text)
print("종목명 : ", td_list[1].find("a").text)
print("검색비율 :", td_list[2].text)
print("현재가 : ", td_list[3].text)
print("PER : ", td_list[11].text)
print("ROE: ", td_list[12].text)
# print(tr_list[2])




# with open("stock.html", 'w', encoding='utf8') as f :
#     f.write(soup.prettify())

#print("종목명 : ", soup.find("td", {"class":"title"}).text)
# print("검색비율 : ", soup.find("td", {"class":"number"}).text)
# print("현재가 : ", soup.find("td", {"class":"number"}).text)

# print(soup.prettify())