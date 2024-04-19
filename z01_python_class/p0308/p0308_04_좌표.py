# ********** 외우기 **********


import random
# 1. 0으로 25개 1차원 리스트 생성
aList = [0] * 25
# print(aList)

# 2. 1로 5개를 변경
for i in range(5) :
    aList[i] = 1
#print(aList)

# 3. 랜덤섞기
random.shuffle(aList)
print(aList)

# 4. 5*5 2차원의 리스트에 넣기
checkList = [[0]*5 for i in range(5)]
for i in range(5) :
    for j in range(5) :
        checkList[i][j] = aList[i*5+j]

# 추첨 5*5 2차원 배열
viewList = [["추첨"]*5 for i in range(5)]

c_cnt = 1                          # 도전횟수
asw_cnt = 0                        # 정답개수
my_xy = [[0]*2 for i in range(10)] # 내가 입력한 좌표
    
while True :
    # 5. checkList 출력
    print("[\t 5*5 checkList 좌표 \t]")
    print('-'*40)
    print("",0 , 1, 2, 3, 4, sep='\t')
    print('-'*40)
    for i in range(5) :
        print(i, end='\t')
        for j in range(5) :
            print(checkList[i][j], end='\t')
        print()
    print('-'*40)
    
        
    # 6. viewList 출력
    print("[\t 5*5 checkList 좌표 \t]")
    print('-'*40)
    print("",0 , 1, 2, 3, 4, sep='\t')
    print('-'*40)
    for i in range(5) :
        print(i, end='\t')
        for j in range(5) :
            print(viewList[i][j], end='\t')  
        print()
    print('-'*40)
    
    # 7. 좌표입력 후 확인
    print("[ 현재 도전 횟수 : {} ]" .format(c_cnt))
    x = int(input("가로 좌표를 입력하세요. >> "))
    y = int(input("세로 좌표를 입력하세요. >> "))
        
    if checkList[x][y] == 1 :
        viewList[x][y] = "당첨"
        asw_cnt += 1  
    else : 
        viewList[x][y] = "[꽝]"
    
    # 내가 입력한 좌표 저장
    my_xy.append([x,y])
    print("[ 내가 입력한 좌표 출력 ]" )
    print(my_xy)
        
    # 5개의 당첨을 맞추면 프로그램 종료
    if asw_cnt == 5 :
        print(" [정답을 모두 맞추셨습니다.]")
        print("프로그램을 종료합니다.")
        break
        
    # 10번 시도 후 프로그램 종료
    c_cnt += 1
    
    if c_cnt == 10 :
        print(" [ 도전 횟수를 모두 사용하셨습니다.]")
        print("프로그램을 종료합니다.")
        break
    
    # 현재까지 입력한 좌표를 모두 출력하시오. 

 
    
'''
card_list = [[0]*2 for i in range(52)]
cnt = 0
for i in shape_list : # spade, diamond, heart, clover
    for j in range(13) :
        card_list[cnt] = [i, num_list[j]]
        print(card_list[cnt])
        cnt += 1
'''