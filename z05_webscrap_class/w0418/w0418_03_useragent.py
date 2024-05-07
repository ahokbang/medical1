import requests
# url = "https://www.google.com"
# url = "https://www.whatismybrowser.com/detect/what-is-my-user-agent/#google_vignette"
url = "https://www.melon.com"
headers ={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36"}
# headers 변수는 다른 걸로 바꿔도 돼 예를 들어 a
headers = {"User-Agent":"   "} # 딕셔너리 형태
# user agent는 user의 정보
res = requests.get(url, headers=headers)
#                               여기 headers는 5줄의 변수로, 6줄에 따라 a를 변수로 했다면 headers = a로 쓸 수 있음.
res.raise_for_status()

print(res.text)

# with open("user_agent.html", "w", encoding='utf8') as f:
    # f.write(res.text)