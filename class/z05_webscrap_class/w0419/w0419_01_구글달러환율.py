import requests
from bs4 import BeautifulSoup

url = "https://www.google.com/search?q=%ED%99%98%EC%9C%A8+1%EB%8B%AC%EB%9F%AC&oq=ghksdbf+1ekffj&gs_lcrp=EgZjaHJvbWUqBwgBEAAYgAQyBggAEEUYOTIHCAEQABiABDIHCAIQABiABDIICAMQABgIGB7SAQk0MTc2ajBqMTWoAgiwAgE&sourceid=chrome&ie=UTF-8"
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36"}
res = requests.get(url, headers=headers)
res.raise_for_status()

soup = BeautifulSoup(res.text, "lxml")

with open ('google1.html', 'w', encoding='utf8') as f:
    f.write(soup.prettify())
    
# print(soup)

# title 출력
print(soup.title.text)

# 미국 달러 통화액수입력란 출력
# 내 코드
divs = soup.find("div",{"class":"vLqKYe egcvbb q0WxUd"})
print(divs.input["value"])

# 선생님 코드
print("미국 달러 : ", soup.find("input",{"class":"lWzCpb ZEB7Fb"})) 
# 해당 태그의 속성값 모두 출력
print("미국 달러 : ", soup.find("input",{"class":"lWzCpb ZEB7Fb"}).attrs) 
# 해당태그의 특정속성값 1개 출력
print("미국 달러 : ", soup.find("input",{"class":"lWzCpb ZEB7Fb"})["value"]) 
# (내가 생각한 건데 굳이 이렇게 할 필요는 없을 듯
print("미국 달러 : ", soup.find("input",{"class":"lWzCpb ZEB7Fb"}).attrs["value"]) 



# 대한민국 원 통화액수입력란 출력
# 내 코드
divs2 = soup.find("div",{"class":"MWvIVe egcvbb"})
print(divs2.input["value"])

# 선생님 코드
print("대한민국 원 : ", soup.find("input", {"class":"lWzCpb a61j6"})["value"])