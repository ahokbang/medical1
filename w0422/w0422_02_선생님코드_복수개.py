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
    # print("후기평점 : ",itemcard.find("div",{"class":"section--itemcard_info_score"}))
    if itemcard.find("ul",{"class":"list--score"}).text == "":
        print("후기평점 : 없음")
    else:
        list_score = itemcard.find("ul",{"class":"list--score"})
        # print("후기평점 : ", list_score.find("span",{"class":"for-a11y"}).text)
        # 후기 4.9 이상 출력
        if list_score.find("span",{"class":"for-a11y"}).text[5:-1] != "":
            for_a11y = float(list_score.find("span",{"class":"for-a11y"}).text[5:-1])
            if for_a11y > 4.9:
                print("후기평점 : ", for_a11y)
            else:
                print("후기평점 : 미달")
        else:
            print("후기평점 : 없음")
        
        # 구매건수 비교
        # 구매건수가 3개 이상인 제품만 출력하고 싶어.
        # 구매건수는 지금 str 타입 ==> 숫자만 슬라이싱 및 형변환
        buycnt = int(list_score.find("span",{"class":"text--buycnt"}).text[3:])
        if buycnt>2:
            print("구매건수 : ", buycnt,"건")
        else:
            print("구매건수 : 미달") # 또는 pass 또는 else 삭제
        
    print('-'*40)



'''
# itemcard = section.find("div",{"class":"section--itemcard"})
#비교를 위해 문자형인 금액을 숫자형으로 변경해줌: replace로 , 제거 후 , int로 형 변환. 데이터 분석 이후 다시 , 넣어주어야 함.
# replace 함수로 ','를 제거하고 int로 타입 변경(문자형->숫자), '{0:,}'.format(num)
print("금액 : ",'{0:,}'.format(price),"원")
# print("후기평점 : ",section.find("li",{"class":"section--itemcard_info"}))
print('-'*40) # 완료
print("후기평점 : ",itemcard.find("li",{"class":"section--itemcard_info_score"}))
'''



