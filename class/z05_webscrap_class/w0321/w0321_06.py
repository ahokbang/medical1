import requests
from bs4 import BeautifulSoup
# url = "https://search.daum.net/search?w=tot&DA=YZR&t__nil_searchbox=btn&q=%EC%98%81%ED%99%94"


# -----------------------
for y in range(2021, 2023+1) :
    url = f"https://search.daum.net/search?w=tot&q={y}%EB%85%84%EC%98%81%ED%99%94%EC%88%9C%EC%9C%84&DA=MOR&rtmaxcoll=MOR"
    headers = {"User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36 Edg/122.0.0.0"}
    res = requests.get(url, headers = headers)
    res.raise_for_status()

    soup = BeautifulSoup(res.text, 'lxml')

    movie_list = soup.find("ol", {"class":"movie_list"})
    # print(movie_list)

    # 30개
    m_list = movie_list.find_all("li")
    sum = 0
    # print(type(m_list))
    for i, m in enumerate(m_list) :
        if i == 5 : break
        print(f"[번호 : {i+1}]")
        print("제목 : ", m.find("div", {"class" : "info_tit"}).a.text)
        print("평점 : ", m.find("em", {"class" : "rate"}).text)
        
        score = float(m.find("em", {"class" : "rate"}).text)
        sum += score
        
        avg = float("{:.2f}".format(sum/5))
        
        # print(m)
        print('-'*50)
        img_screen = m.find("img")["data-original-src"]
        print(img_screen)
        # print(m.find("img")["data-original-src"])
        # 파일 열기 (= 이미지 저장 부분)
        # with open(f'movie_{y}_{i}.jpg', 'wb') as f :
        #     re_img = requests.get(img_screen)
        #     f.write(re_img.content) # 파일이름의 내용을 저장

    print(f"{y}년 역대 영화의 총 평점 : ", sum)
    # for i in range(2021, 2023+1) : 
    #     print(f"{y}년 역대 영화의 총 평점 : ", sum)    
    print(f"{y}년 역대 영화의 총 평점의 평균 : ", avg)
# -------------------

print("개수 : ", len(m_list)) # 30개
print("종료")