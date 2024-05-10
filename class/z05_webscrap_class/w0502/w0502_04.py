url = 'background-image: url(&quot;https://yaimg.yanolja.com/v5/2023/02/20/11/1280/63f3584b0a31f9.72309509.jpg&quot;)'

url[28:]

loc = url.find("http")
print("위치값 : ", loc)

print(url[loc:])