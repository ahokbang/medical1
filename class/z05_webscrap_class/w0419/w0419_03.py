import requests
from bs4 import BeautifulSoup

url = "https://www.coupang.com/np/search?q=%EB%85%B8%ED%8A%B8%EB%B6%81&channel=recent"
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36 Edg/123.0.0.0", "Accept-Language": "ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7"}
res = requests.get(url, headers=headers)
res.raise_for_status()

soup = BeautifulSoup(res.text, "lxml")

with open("coupang_notebook.html", 'w', encoding='utf8') as f:
    f.write(soup.prettify())

''' 내가 한 코드
ntbs = soup.find("ul", {"class":"search-product-list"})
ntbs_p = ntbs.find("a",{"class":"search-product-link"}).div
ntbs_name = ntbs_p.next.next.next.text
print("상품명 : ", ntbs_p.next.next.next.text)
print("금액: ", ntbs_p.find("strong",{"class":"price-value"}).text)
print("별점 : ", ntbs_p.find("span",{"class":"star"}).text)
print("별점 인원 : ", ntbs_p.find("span",{"class":"rating-total-count"}).text)

# print(soup.find("div", {"class":"name"}).text)

for ntb in ntbs[0:10]:
    print("상품명 : ", ntbs_p.next.next.next.text)
    print("금액: ", ntbs_p.find("strong",{"class":"price-value"}).text)
    print("별점 : ", ntbs_p.find("span",{"class":"star"}).text)
    print("별점 인원 : ", ntbs_p.find("span",{"class":"rating-total-count"}).text)
'''
# 선생님 코드
# print(soup.find("ul", {"class":"search-product-list"}))
# print(len(soup.find("ul", {"class":"search-product-list"}).find_all("li")))

ul_search = soup.find("ul", {"class":"search-product-list"})
# 모든 상품 검색
lis = ul_search.find_all("li")

# print("리스트 개수 : ", len(lis))

# print("", ul_search.find("li"))
# print(lis[0]) # 얘는 광고라서 자꾸 바껴
# print('-'*30)
# print(lis[1])
'''
# 상품 정보 1개 불러오기 
print("상품명 : ", lis[1].find("div",{"class":"name"}).text)
print("가격 : ", lis[1].find("strong",{"class":"price-value"}).text,"원")
print("평점 : ", lis[1].find("em",{"class":"rating"}).text)
print("평가인원수 : ", lis[1].find("span",{"class":"rating-total-count"}).text)

# 10위까지 확인하기
for i,li in enumerate(lis[0:10]) :
    print("[ ",i+1, "번째 상품 ]")
    print("상품명 : ", li.find("div",{"class":"name"}).text)
    print("가격 : ", li.find("strong",{"class":"price-value"}).text,"원")
    print("평점 : ", li.find("em",{"class":"rating"}).text)
    print("평가인원수 : ", li.find("span",{"class":"rating-total-count"}).text)
    print('-'*100)
'''

# 광고 빼기
for i,li in enumerate(lis[0:20]) :
    print("[ ",i+1, "번째 상품 ]")
    # 광고상품 제외
    if 'search-product__ad-badge' in li['class']:
        continue
    # 평점이 5.0 이상인 것만 출력 - 문자와 숫자 비교 불가하여 실수형으로 형변환 필요, 문자와 숫자 비교 시 에러 발생
    if float(li.find("em",{"class":"rating"}).text) < 5.0:
        continue
    # 평가인원수 200명 이상인 사람 출력 - 정수형으로 형변환
    if int(li.find("span",{"class":"rating-total-count"}).text[1:-1]) < 200 :
        continue
    print("li class : ", li["class"])
    # 왼쪽, 오른쪽 공백제거
    print("상품명 : ", li.find("div",{"class":"name"}).text.strip())
    print("가격 : ", li.find("strong",{"class":"price-value"}).text,"원")
    print("평점 : ", li.find("em",{"class":"rating"}).text)
    # 평가인원수 200명 이상인 사람 출력 ==> 괄호가 있으므로 slice 사용하여 잘라내기!
    print("평가인원수 : ", li.find("span",{"class":"rating-total-count"}).text[1:-1])
    print('-'*89)