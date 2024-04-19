import requests
from bs4 import BeautifulSoup

url = "https://news.naver.com/main/ranking/popularDay.naver"
headers = {"User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36 Edg/122.0.0.0"}
res = requests.get(url,headers=headers)
res.raise_for_status()
# print(res.text)
soup = BeautifulSoup(res.text,"lxml")
# 파일 저장
# with open('test.html', 'w', encoding='utf8') as f :
#     f.write(soup.prettify())

print(soup.title) # 타이틀이 여러개일 경우 첫번째 태그 출력
print(soup.title.text) # soup 태그사용해서 text 글자 출력
print(soup.a) # soup 태그사용
print(soup.a.attrs) # 속성값을 딕셔너리 형태로 출력 # soup에서 a태그의 속성값 출력 ; 전부 출력
print(soup.a["href"]) # soup a태그 선택속성값 출력; 선택값 1개 출력 
print(soup.find("div",attrs={"id":"footer"})) # soup에서 find 태그, 속성 모두를 가지고 검색
# print(soup.find("div",{"id":"footer"})) 위의 코드는 옆에 처럼 써도 돼.
# print(soup.div)

'''
태그: <> 안에 있는 것

'''