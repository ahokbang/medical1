import requests
# 웹에 접근해서 html 소스를 가져옴. 
# res = requests.get("https://www.google.com/") # print(res) ==> <Response [200]>
# res = requests.get("https://www.daun.net/")
res = requests.get("https://www.melon.com/") # print(res) ==> <Response [406]> ==> 웹 스크래핑 차단으로 인한 페이지없음
print(res) # 코드상태 출력
print('코드 : ', res.status_code) # 코드상태만 출력, 리턴한 소스의 코드값을 출력
# <Response [code]>
# - 200: 정상 
# - 403 또는 404 : 페이지 없음
# - 500 : 프로그램 에러
print(type(res))
print(type(res.status_code))
if res.status_code == 200 :
# == if res.status_code == request.codes.ok :
    print('정상페이지 호출입니다.')
else : 
    print("에러코드 발생")

res.raise_for_status() # 코드가 200이 아니면 오류처리해서 자동 멈춤
print("-"*40)
# requests를 통해 html 소스를 출력
print(res.text)