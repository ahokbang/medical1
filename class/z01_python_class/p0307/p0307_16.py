# 25개 1차원 리스트 생성
# 0으로 20개, 1로 5개 넣기
# 랜덤섞기
# 5*5 2차원 리스트에 넣기

import random

a_list = [0] * 25
for i in range(5) :
    a_list[i] = 1
print(a_list)

random.shuffle(a_list)

print(a_list)

print()


b_lists = []
b_list =[]

for i, j in enumerate(a_list) :
    if (i+1) % 5 == 0 :
        b_list.append(j)
        b_lists.append(b_list)
        b_list = []
    else :
        b_list.append(j)
print(b_lists)

'''선생님 풀이
imort random

# 0으로 25개 1차원 리스트 생성
aList = [0]*25

# 1로 5개를 변경
for i in range(5) :
    aList[i] = 1
# print(aList)

# 랜덤섞기
random.shuffle(aList)
# print(aList)

bList = [[0]*5 for i in range(5)] # 먼저 5*5 공간 생성
# print(bList)

# 5*5 2차원 리스트에 넣기
for i in range(5) :
    for j in range(5) :
        bList[i][j] = aList[5*i+j] # append보다 빠른 방법 ********** **********
# 출력
print("", 0, 1, 2, 3, 4, sep='\t')
for i in range(5) :
    for j range (5) :
    


print(bList)
'''