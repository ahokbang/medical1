# 25개 1차원 리스트 생성
# 0으로 20개, 1로 5개 넣기
# 랜덤섞기
# 5*5 2차원 리스트에 넣기

import random

# 1. 0으로 25개 1차원 리스트 생성
aList = [0]*25

# 2. 1로 5개를 변경
for i in range(5) :
    aList[i] = 1
# print(aList)

# 3. 랜덤섞기
random.shuffle(aList)
# print(aList)

# 4. 5*5 2차원 리스트에 넣기
checkList = [[0]*5 for i in range(5)] # 먼저 5*5 공간 생성
# print(bList)
for i in range(5) :
    for j in range(5) :
        checkList[i][j] = aList[5*i+j] # append보다 빠른 방법 ********** **********

# 추첨 5*5 2차원 배열
viewList = [["추첨"]*5 for i in range(5)] # 먼저 5*5 공간 생성

cnt = 0
while True : 
    # 5. checklist 출력
    print("\t [ 5*5 checkList 좌표 ]")
    print('-'*40)
    print("", 0, 1, 2, 3, 4, sep='\t')
    print('-'*40)
    for i in range(5) :
        print(i, end='\t')
        for j in range (5) :
            print(checkList[i][j], end='\t')
        print()
    print('-'*40)

    # 6. viewlist 출력
    print("\t [ 5*5 viewList 좌표 ]")
    print('-'*40)
    print("", 0, 1, 2, 3, 4, sep='\t')
    print('-'*40)
    for i in range(5) :
        print(i, end='\t')
        for j in range(5) :
            print(viewList[i][j], end='\t')
        print()
    print('-'*40)

    # 7. 좌표 입력 후 확인
    x = int(input("가로 좌표를 입력하세요. >> "))
    y = int(input("세로 좌표를 입력하세요. >> "))

    if checkList[x][y] == 1 :
        viewList[x][y] = "당첨"
        cnt += 1
        if cnt == 10 :
            print("게임이 종료되었습니다.")
            re_cnt = input("게임을 다시 시작하시겠습니까? (1. 실행 0. 취소)")
            if re_cnt == "0" :
                break
            else : 
                print("게임을 다시 시작합니다.")
    else :
        viewList[x][y] = "[꽝]"

# print(bList)
# 5개의 당첨을 맞추면 프로그램 종료
# 10번 시도 후 프로그램

