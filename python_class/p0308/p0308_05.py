# 리스트를 딕셔너리 형태로 변경
import random

card_list = []
print(card_list)
shape_list = ["spade", 'diamond', 'heart', 'clover']
num_list = [0]*13
for i in range(1,14) :
    num_list[i-1] = i
num_list[0] = "A"
num_list[10] = "J"
num_list[11] = "Q"
num_list[12] = "K"


# card_list = [
# ['spade', 'A'], ['spade', 2], ['spade', 3], ['spade', 4], ['spade', 5],
# ['spade', 6], ['spade', 7], ['spade', 8], ['spade', 9], ['spade', 10],
# ['spade', 'J'], ['spade', 'Q'], ['spade', 'K'], ['diamond', 'A'],
# ['diamond', 2], ['diamond', 3], ['diamond', 4], ['diamond', 5], 
# ['diamond', 6], ['diamond', 7], ['diamond', 8], ['diamond', 9],
# ['diamond', 10], ['diamond', 'J'], ['diamond', 'Q'], ['diamond', 'K'],
# ['heart', 'A'], ['heart', 2], ['heart', 3], ['heart', 4], ['heart', 5],
# ['heart', 6], ['heart', 7], ['heart', 8], ['heart', 9], ['heart', 10],
# ['heart', 'J'], ['heart', 'Q'], ['heart', 'K'], ['clover', 'A'],
# ['clover', 2], ['clover', 3], ['clover', 4], ['clover', 5], ['clover', 6],
# ['clover', 7], ['clover', 8], ['clover', 9], ['clover', 10], ['clover', 'J'],
# ['clover', 'Q'], ['clover', 'K']   
# ]

# 딕셔너리 형태로 변경
# card_list = [ {}, {}, ... ,]

card_list = [[0]*2 for i in range(52)]
cnt = 0
for i in shape_list : # spade, diamond, heart, clover
    for j in range(13) :
        card_list[cnt] = {"shpae" : i, "num" : num_list[j]}
        print(card_list[cnt])
        cnt += 1
print(card_list)
# 카드 섞기
random.shuffle(card_list)

# 출력:
# 모양 : spade, 번호 : 1

# 선생님 풀이
arr_num = 0

while True :
    print("[ 카드게임 ]")    
    print("1. 카드 1장 뽑기")
    print("2. 카드 5장 뽑기")
    print("0. 종료")
    print("현재 남은 카드 : ", len(card_list)-arr_num)
    c_num = int(input("번호를 선택해주세요. >> "))

    if c_num == 1 : # ********** print 부부 외우기 **********
        print("모양 : {}, 번호 : {}" .format(card_list[arr_num]["shpae"], card_list[arr_num]["num"]))
        arr_num += 1
    elif c_num == 2 :
        for i in range(5) :
                print("모양 : {}, 번호 : {}" .format(card_list[arr_num]["shpae"], card_list[arr_num]["num"]))
        arr_num += 1        
    else :
        print("프로그램을 종료합니다.")
        break










''' 내 풀이

arr_num = 0

while True :
        
    print("1. 카드 1장 뽑기")
    print("2. 카드 5장 뽑기")
    print("0. 종료")
    c_num = int(input("번호를 선택해주세요. >> "))

    if c_num == 1 : # ********** print 부부 외우기 **********
        print("모양 : ", card_list[arr_num]["shpae"], ", 번호 : ", card_list[arr_num]["num"] )
        
    elif c_num == 2 :
        for i in range(5) :
                print("모양 : ", card_list[arr_num]["shpae"], ", 번호 : ", card_list[arr_num]["num"] )
                
    else :
        print("프로그램을 종료합니다.")
        break

'''