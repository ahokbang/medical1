# 1부터 25까지 숫자를 랜덤으로 섞은 다음 2차원 리스트에 넣어보세요.

# [
#    [1, 2, 3, 4, 5], 
#    [6, 7, 8, 9, 10], 
#    [11, 12, 13, 14, 15], 
#    [16, 17, 18, 19, 20], 
#    [21, 22, 23, 24, 25]
#                         ]

# 랜덤으로 섞어서 출력하시오.

# 1. 1부터 25까지 리스트 생성
# 2. 랜덤으로 섞기
# 3. 2차원 리스트에 넣기

# import random

# num = random.randint(1,3)
# print(num)

# random을 사용해서 숫자 맞추기 프로그램 구현
# 1부터 10까지 숫자 랜덤으로 생성 숫자를 맞추는 프로그램
import random
num = random.randint(1,100)
cnt = 0
print("정답 : ", num)
nums = []

while True :
    in_num = int(input("1~100까지의 숫자를 입력하세요."))
    nums.append(in_num)
    cnt += 1
    if num > in_num :
        print("입력한 숫자보다 더 큽니다.")
    elif num < in_num :
        print("입력한 숫자보다 더 작습니다.")
    else :
        print("정답입니다.")
        print("{}번 만에 맞추었습니다." .format(cnt))
        break
    
'''
import random
num = random.randint(1,100)
cnt = 1 # 도전 횟수
save_num = [] 
print("정답 : ", num)
while True :
    in_num = int(input("1~100까지의 숫자를 입력하세요."))
    save_num.append(in_num)
    if num > in_num :
        print("입력한 숫자보다 더 큽니다.")
    elif num < in_num :
        print("입력한 숫자보다 더 작습니다.")
    else :
        print("정답입니다.")
        print("{}번 만에 맞추었습니다." .format(cnt))
        break
    cnt += 1
'''
