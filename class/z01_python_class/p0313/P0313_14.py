
card_num = [0]*13
for i in range(13) :
    card_num[i] = i+1
card_num[0] = "A"
card_num[10] = "J"
card_num[11] = "Q"
card_num[12] = "K"

card_num = [1,2,3,4,5,6,7,8,9,10,11,12,13]

# [ 숙제 ]
# 랜덤으로 2개를 숫자를 뽑아서 출력하시오.
# 랜덤숫자 : 2 -> 1번 방에 있습니다.
# 랜덤숫자 : 9 -> 8번 방에 있습니다.
# 큰 수 : 9, 작은 수: 2
# 주석 무조건 달기, 슬랙에 올리기

import random
print(random.sample(card_num, k=2)) # 랜덤으로 숫자 2개 뽑기
print("랜덤숫자 : ")

ran_num = random.sample(card_num, k=2)
for i in ran_num :
    print(f"랜덤숫자 : {i} -> {i-1}방에 있습니다.")
if ran_num[0] > ran_num[1] :
    print(f"큰 수 : {ran_num[0]}, 작은 수 : {ran_num[1]}")
else :
    print(f"큰 수 : {ran_num[1]}, 작은 수 : {ran_num[0]}")