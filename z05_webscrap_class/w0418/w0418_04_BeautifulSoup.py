import requests
from bs4 import BeautifulSoup  # html로 변경해줌
url = "https://finance.naver.com/sise/lastsearch2.naver"
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36"}
res = requests.get(url, headers=headers)
res.raise_for_status()

print(res.text)
print(type(res.text))

# with open("stock.html", 'w', encoding='utf8') as f:
#    f.write(res.text)

soup = BeautifulSoup(res.text,"lxml") # text를 html 파싱
# print(soup)
# print(type(soup))

# with open("stock2.html", 'w', encoding='utf8') as f:
#    f.write(soup.prettify()) # html 소스를 정렬래서 출력
    
# stock1.html과 stock2.html을 보면 stock2.html의 소스코드가 더 예쁘게 정렬되어 나와
# ==> soup.prettify로 저장하는 것이 더 나음.

# 가져오는 방법 : soup.가져올 태그이름
# 네이버페이 증권(title) 찾기
print("<title> : ", soup.title) # 태그를 입력 태그 정보 가져옴
print("<title> text : ", soup.title.get_text()) # 태그의 글자를 가져옴.
print("<title> text : ", soup.title.text) # 태그의 글자를 가져옴.

# html에서는 제이쿼리일 경우 value, 자바스크립트 val
# 제이쿼리일 경우 text(), 자바스크립트일 경우 innerText
# 제이쿼리일 경우 ()있어!

# 파이선에서 영문자+괄호 있으면 함수, 영문의 첫글자가 대문자면 클래스

# html에서 id와 class 차이
# id는 유일하지만, class는 여러번 쓸 수 있어.

print("<a> 태그 : ", soup.a) 
# <a> :  <a href="#menu" tabindex="1"><span>메인 메뉴로 바로가기</span></a>
print("<a> 태그글자 : ", soup.a.text) 
# <a> :  메인 메뉴로 바로가기

# a : 태그
# href : 속성
# #ment : 속성값
# tabindex

# 속성값을 가져오고 싶을 때
print("<a> 속성전체 : ", soup.a.attrs) # 태그의 속성값 모두 가져옴
# <a> :  {'href': '#menu', 'tabindex': '1'}

# 속성값 하나만 가져오고 싶을 때
print("<a>[1개 속성] : ", soup.a["href"]) # 태그의 1개 속성 가져옴.==> 해당하는 태그의 속성값 가져옴.

