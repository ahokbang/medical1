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

print(shape_list)
print(num_list)

# 포커 순서
# 스페이드 > 다이아 > 하트 > 클로버
# A > K > Q > J > 10~2

# 카드 1세트를 구gus해서 출력하시오. : 52장

# 선생님 풀이 ********** 꼭 이해하기! **********
card_list = [[0]*2 for i in range(52)]
cnt = 0
for i in shape_list : # spade, diamond, heart, clover
    for j in range(13) :
        card_list[cnt] = [i, num_list[j]]
        print(card_list[cnt])
        cnt += 1

# 카드 랜덤 섞기
random.shuffle(card_list)

arr_num = 0

while True :
        
    print("1. 카드 1장 뽑기")
    print("2. 카드 5장 뽑기")
    print("0. 종료")
    c_num = int(input("번호를 선택해주세요. >> "))
    print("현재 남은 카드 : ", len(card_list)-arr_num)
    if c_num == 1 :
        print(card_list[arr_num])
        arr_num += 1
    elif c_num == 2 :
        for i in range(5) :
            print(card_list[arr_num])
            arr_num += 1

print(card_list)