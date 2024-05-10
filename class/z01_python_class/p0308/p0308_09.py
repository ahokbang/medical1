import random
random_num = str(random.randint(10000, 99999)) # randum_num을 str 해주어야 int error 안나!
print("[ 랜덤숫자 맞추기 ]")
print("랜덤숫자 : ", random_num)

a_input = input("숫자 5자리를 입력하세요.")

# 숫자자리로 확인해서 맞춘 개수를 출력하시오.

cnt = 0 # 맞은 갯수를 저장

for i in range(len(str(random_num))) : # 위에서 str해줘서 여기서 안해줘도 돼.
    if random_num[i] != a_input[i] :
        break
    else :
        cnt += 1 # 맞는 횟수 1 증가
print("맞는 개수 : ", cnt) 