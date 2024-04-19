
# [ --------------------기본구문-------------------------------------    
import requests # 웹 정보, 소스를 가져오는 라이브러리
url = "https://www.google.com"
# url = "https://www.melon.com"
headers ={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36"}
res = requests.get(url,headers=headers)
res.raise_for_status() # 에러 코드 발생 시 프로그램 종료 200 ---> 
# print(res.status_code) # 응답코드 값으로 200, 404, 406, 500, ... 등이 있음
# ] 3~8줄은 기본 구문------------------------------------------------

# 응답코드가 200이냐라고 묻는 것. (requests.codes.OK == 200)
# if res.status_code == requests.codes.OK: 
if res.status_code == 200:
    print("정상적인 페이지 호출")
else:
    print("접근할 수 없음. [에러 코드 : ", res.status_code,"]")


# 406: 페이지 없음
# 500 : (상대방 페이지의 문제로 인한) 에러
# print(res)
