import requests

# User agent 사용방법
# res = requests.get('https://www.melon.com/index.htm')
# res = requests.get('https://www.whatismybrowser.com/detect/what-is-my-user-agent/')
url = "https://www.melon.com/index.htm"
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36 Edg/122.0.0.0"}
res = requests.get(url, headers=headers)
print("코드 : ", res.status_code)
res.raise_for_status()

print(len(res.text))
print(res.text)

with open("a1.html", 'w', encoding='utf8') as f :
    f.write(res.text)

print("파일이 저장되었습니다.")

'''
- 웹 크롤링 
    - 웹 상에 존재하는 컨텐츠를 수집하는 작업(프로그래밍 자동화 기능)
    - HTML 페이지를 가져와서 HTML/CSS 등을 파싱하고, 필요한 데이터만 추출하는 기법
    - Open API를 제공하는 서비스에 Open API를 호출해서 받은 데이터 중 필요한 데이터만 뽑는 기술

'''
