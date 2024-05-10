# quiz

# 크기가 10인 리스트를 생성하는데 7개는 0으로, 3개는 1로 채우시오.
# [1,1,1,0,0,0,0,0,0,0] 

''' 내 풀이
list = [[1]*3+[0]*7 ]
print(list) # 이거 아니야. 2차원으로 나와. 
'''

'''선생님 풀이
list = [0] *  10
for i in range(3) :
    list[i] = 1
print(list)
'''

# 크기가 100인 리스트 생성, 10개는 1로 채우시오.
# 랜덤으로 섞어서 출력하시오.
# import random
# list = [0] * 100
# for i in range(10) :
#     list[i] = 1
# random.shuffle(list)
# print(list)

# 선생님 풀이
import random

aList = [0 for i in range(100)]
print(aList) 
for i in range(10) :
    aList[i] = 1
print(aList) # 파괴 

random.shuffle(aList)   # shuffle의 경우 aList(데이터)를 파괴, 별도로 변수가 필요하지 않아
print(aList)

# a = 10
# print(a+10) # 비파괴형태
# a = a+10 # # 파괴형태
# print('a :', a) # a : 10

# 리스트의 경우 파괴 


print()
# [ 10*10 ] 2차원 배열을 생성하시오.
# list2 = [[0]*10]*10
# print(list2)

# list3 = [[0]*10 for _ in range(10)]

print('-'*10)

# 선생님 풀이
bLists = []
bList = []
for i, j in enumerate(aList) :
    # bList = [] # 100번 돌 때마다 계속 처음으로 초기화
    if (i+1) % 10 == 0 : # 0, 1, 2, 3, 4, 5, 6, 7, 8, 9
        bList.append(j)
        bLists.append(bList)
        bList = [] # 100번 계속 처음으로 초기화
    else :
        bList.append(j)

newLists = [["추첨"]*10 for _ in range(20)]


print("[ 10*10 좌표 ]")
print('-'*60)
# print(bLists)
print(0, 1, 2, 3, 4, 5, 6, 7, 8, 9, sep='     ')
print('-'*60)
for b in newLists:
    for bb in b :
        print(bb, end="  ")
    print()
