# 기본 복사
import requests
from bs4 import BeautifulSoup
url = "https://browse.auction.co.kr/list?category=22160000"
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36 Edg/123.0.0.0", "Accept-Language": "ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7"}
res = requests.get(url, headers=headers)
res.raise_for_status()

# 데이터 불러오기
soup = BeautifulSoup(res.text,'lxml')

# 파일 저장
with open("auction_ntb.html", 'w', encoding='utf8') as f:
    f.write(soup.prettify())

# print(soup.prettify())

# 내 코드
# 이름, 가격, 평점, 후기 개수, (이미지) 가져오기
div_search = soup.find("div",{"class":"component component--item_card type--general"})
# print(div_search)
divs = div_search.find_all("div")
# divs = div_search.find_all("div", {"class":"section--itemcard_info"})

print("이름 : ", divs[2].find("span",{"class":"text--title"}).text)
print("가격 : ", divs[2].find("span",{"class":"text__price-seller"}).text)
print("평점 : ", divs[2].find("span",{"class":"seller_awards"}).text)


# div = divs.find("div", {"class":"component component--item_card type--general"})
# print(div[2].find("div",{"class":"area--itemcard_title"}).text)

