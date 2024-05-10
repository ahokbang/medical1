# 12월, 1월, 2월 겨울, 3, 4, 5월 봄 6, 7, 8,월 여름, 9, 10, 11월 가을
# 1 - 겨울입니다.
# 12 - 겨울입니다.
# 7 - 여름입니다.

season = input("월을 입력하세요. >> ")
season1 = season[0:-1] # season1 = int(season[0:-1]) ==>  10월에서 에러 발생
season2 = int(season1)

if 3 <= season2 <=5 :
    print("봄입니다.")
elif 6 <= season2 <= 8 :
    print("여름입니다.")
elif 9 <= season2 <= 11 : 
    print("가을입니다.")
else:                     # elif season2 == 12 or 1<= season2 <= 2: 로 쓸 수 있어
    print("겨울입니다.")
    
