# quiz

# 크기가 10인 리스트를 생성하는데 7개는 0으로, 3개는 1로 채우시오.
# [1,1,1,0,0,0,0,0,0,0] 


list = [0] *  10
for i in range(3) :
    list[i] = 1
print(list)


# 크기가 100인 리스트 생성, 10개는 1로 채우시오.
# 랜덤으로 섞어서 출력하시오.
import random
list = [0] * 100
for i in range(10) :
    list[i] = 1
random.shuffle(list)
print(list)

import random

aList = [0 for i in range(100)]
print(aList) 
for i in range(10) :
    aList[i] = 1
print(aList) # 파괴 

random.shuffle(aList)   # shuffle의 경우 aList(데이터)를 파괴, 별도로 변수가 필요하지 않아
print(aList)

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

# 10*10 리스트 1개 추가
newLists = [["추첨"]*10 for _ in range(10)]

cnt = 0 # 당첨횟수

while True : 
    # print(bLists) # 답
    print("[ 10*10 좌표 ]")
    print('-'*60)
    # print(bLists)
    print("", 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, sep='     ')
    print('-'*60)
    for i, b in enumerate(newLists):
        print(i, end = "  ")
        for bb in b :
            print(bb, end="  ")
        print()
    print('-'*60)
    x = int(input("가로 좌표를 입력하세요. >> "))
    y = int(input("세로 좌표를 입력하세요. >> "))
    # bLists : 값을 비교, newLists : 표시
    if bLists[x][y] == 1 : # 당첨
        newLists[x][y] = "당첨"
    else : # 꽝
        newLists[x][y] = "[꽝]"
    cnt += 1
    if cnt == 5 :
        print("추첨이 종료되었습니다.")
        re_stt = input("추첨을 다시 시작하시겠습니까?(1. 실행 0. 취소)")
        if re_stt == "0" :
            break
        else : 
            print("추첨을 다시 시작합니다.")

'''선생님 풀이 *********** 다시 확인해보기 깃허브 파일 재확인 필요 **********
cnt += 1
    if cnt == 5 :
        print("추첨이 종료되었습니다.")
        if cnt == 10 :
            print("모두 당첨되었습니다!!!")
            break
        else : 
            print("추첨을 다시 시작합니다.")

'''

            
'''
newList: 보여지는 리스트
aList : 확인용 리스트
alist 안에는 
'''

