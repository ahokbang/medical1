# ********** [외우기] ********** : 데이터 가공. 데이터분석, 딥러닝의 기본!
# 기본 복사
import requests
from bs4 import BeautifulSoup
url = "https://browse.auction.co.kr/list?category=22160000&k=31&p=1"
# url = "https://browse.auction.co.kr/list?category=22160000"
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36 Edg/123.0.0.0", "Accept-Language": "ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7"}
res = requests.get(url, headers=headers)
res.raise_for_status()

# 데이터 불러오기
soup = BeautifulSoup(res.text,'lxml')

# 파일 저장
with open("auction_ntb.html", 'w', encoding='utf8') as f:
    f.write(soup.prettify())

# print(soup.prettify())


# 이름, 가격, 평점, 후기 개수, (이미지) 가져오기
#print('-'*40)
#print(soup.find("div",{"id":"section--inner_content_body_container"}))
print('-'*40)
#divs = section.find_all("div",{"class":"section--module_wrap"})
# print("개수 : ", len(divs))

section = soup.find("div",{"id":"section--inner_content_body_container"})
#print(section.find("div",{"class":"itemcard"}))
#print(section.find("div",{"class":"section--itemcard"}))
# 복수개 찾기
itemcards = section.find_all("div",{"class":"section--itemcard_info"})
# print("개수 : ", len(itemcards))
# print("이름 : ",itemcards[2].find("span",{"class":"text--title"}).text)

for i, itemcard in enumerate(itemcards[0:10]):
    print("[ ",i+1,"번째 ]")
    print("이름 : ",itemcards[2].find("span",{"class":"text--title"}).text)
    price = int((itemcard.find("strong",{"class":"text__price-seller"}).text).replace(",",""))
    print("금액 : ",'{0:,}'.format(price),"원")
    
    # 후기평점, 구매건수
    list_score = itemcard.find("ul",{"class":"list--score"})
    lis = list_score.find_all("li")
    # print("li 개수 : ", len(lis))
    if len(lis) == 0:
        print("후기평점, 구매건수 : 없음")
    elif len(lis) == 1:
        buycnt = int(lis[0].find("span",{"class":"text--buycnt"}).text[3:])
        print("구매건수 : ", buycnt)
        
    else: # li가 3개인 경우
        for_a11y = float(lis[0].find("span",{"class":"for-a11y"}).text[5:-1])
        print("후기평점 : ", for_a11y)
        buycnt = int(lis[2].find("span",{"class":"text--buycnt"}).text[3:])
        print("구매건수 : ",buycnt)
        
    print('-'*40)
