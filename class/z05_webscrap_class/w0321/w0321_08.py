import requests
from bs4 import BeautifulSoup
url = "https://finance.naver.com/sise/lastsearch2.naver"
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36"}
res = requests.get(url,headers=headers)
res.raise_for_status()
soup = BeautifulSoup(res.text,"lxml")
# print(soup)
# stock = soup.find("div",{"class":"box_type_l"})
s_all = soup.find("div", {"class":"box_type_l"})
tr_list = s_all.find_all("tr") # s_all 중에 tr이 몇개 있는지 
# list 타입
print(len(tr_list)) # 50 
print(type(tr_list)) # <class 'bs4.element.ResultSet> # 자바나 C에서 ResultSet은 list

# -----------------------------------
# samsung = tr_list[2] # 삼성은 tr 3번째에 있어 ==> tr_list[2]
# # print(samsung)
# # print(samsung.find("a").text) 
# td_list = samsung.find_all("td")
# print("순위 :" , td_list[0].text)
# print("종목명 : " , td_list[1].find("a").text)
# print("검색비율 :", td_list[2].text)
# print("현재가 : ", td_list[3].text)
# print("PER : ", td_list[10].text)
# print("ROE: ", td_list[11].text)

# second = tr_list[3]
# td_list2 = second.find_all("td")
# print("순위 :" , td_list2[0].text)
# print("종목명 : ", td_list2[1].find("a").text)
# print("검색비율 :", td_list2[2].text)
# print("현재가 : ", td_list2[3].text)
# print("PER : ", td_list2[10].text)
# print("ROE: ", td_list2[11].text)

# third = tr_list[4]
# td_list3 = second.find_all("td")
# print("순위 :" , td_list3[0].text)
# print("종목명 : ", td_list3[1].find("a").text)
# print("검색비율 :", td_list3[2].text)
# print("현재가 : ", td_list3[3].text)
# print("PER : ", td_list3[10].text)
# print("ROE: ", td_list3[11].text)

#--------------------------------------------------------
# 5번까지 출력
# for i in range(2,7) :
#     # td_list[i+1] = tr_list[i+1]
#     stock = tr_list[i]
#     td_list = stock.find_all("td")
#     print("순위 :" , td_list[0].text)
#     print("종목명 : ", td_list[1].find("a").text)
#     print("검색비율 :", td_list[2].text)
#     print("현재가 : ", td_list[3].text)
#     print("PER : ", td_list[10].text)
#     print("ROE: ", td_list[11].text)
    
# 10번까지 출력
for i in range(2,15) :
    # td_list[i+1] = tr_list[i+1]
    stock = tr_list[i]
    td_list = stock.find_all("td")
    # if len(td_list) <= 1 : continue 로도 할 수 있어.
    if len(td_list) > 1 :
        print("순위 :" , td_list[0].text)
        print("종목명 : ", td_list[1].find("a").text)
        print("검색비율 :", td_list[2].text)
        print("현재가 : ", td_list[3].text)
        print("PER : ", td_list[10].text)
        print("ROE: ", td_list[11].text)
        print('-'*50)
        print()
        
    