# 이중 for문 break

# 구구단 - 이중for문을 사용하고 있음. 
# 변수 1개를 사용해야 함. 
temp = 0
''' 문제
for i in range(1, 10) :
    for j in range(1,10) :
        if j == 5 :
            # 여기에서 프로그램을 종료하는 방법
            
            break       
        print(f"{i} * {j} = {i*j}")
'''

for i in range(1, 10) :
    # if i == 2 : break # 이 방법도 있지만 문제낸 건 변수이용하는 방법
    for j in range(1,10) :
        if j == 5 :
            # 여기에서 프로그램을 종료하는 방법
            temp = 1
            break        
        print(f"{i} * {j} = {i*j}")
    if temp == 1 : break