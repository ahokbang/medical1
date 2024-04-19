import requests
from bs4 import BeautifulSoup

url = "https://www.gmarket.co.kr/n/best"
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36"}
res = requests.get(url, headers=headers)
res.raise_for_status()

soup = BeautifulSoup(res.text, "lxml")

with open ('gmarket1.html', 'w', encoding='utf8') as f:
    f.write(soup.prettify())
    
# print(soup)
'''
# 베스트의 1 상품 이름, 가격 출력 [내 코드]
print("순위 : ",soup.find("p", {"class":"no1"}).text)
print("상품명 : ", soup.find("a", {"class":"itemname"}).text)
soup.find("span", {"class":"for-a11y"})
print("가격 : ", soup.find("div", {"class":"s-price"}).next.next.next.text)
'''


# 선생님 코드 (24~45)
# 베스트 상품의 순위, 상품 이름, 가격 출력 위해 아래와 같이 div 베스트를 찾는 것이 더 용이
# print("div 베스트 : ", soup.find("div", {"class": "best-list"}))
best_div = soup.find("div", {"class": "best-list"})
# print("li01 : ", best_div.find("li"))
''' 주석처리
li01 = best_div.find("li")
print("li01 순위 : ", li01.p.text)
print("li01 상품명 : ", li01.find("a",{"class":"itemname"}).text)
# print("li01 금액 : ", li01.find("div", {"class":"s-price"}).strong)
# print("li01 금액 : ", li01.find("div", {"class":"s-price"}).strong.span)
print("li01 금액 : ", li01.find("div", {"class":"s-price"}).strong.span.text)
'''
# 여러개의 베스트 상품 출력
lis = best_div.find_all("li")
# print("베스트 상품 개수 : ",len(lis))
for li in lis[0:4]:
    # print("베스트 상품 : ",li)
    print("순위 : ", li.p.text)
    print("상품명 : ", li.find("a",{"class":"itemname"}).text)
    print("금액 : ", li.find("div", {"class":"s-price"}).strong.span.text)
    print('-'*40)

    
