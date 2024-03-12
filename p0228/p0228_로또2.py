from random import *
# 1. 변수선언 1- 10
lotto = []
# 2. 입력받은 숫자 6개
mynum = [2, 5, 1, 9, 3, 7]
# 3. 로또 번호 생성하기

for i in range(6) :
    n = randint(1, 10)
    if n not in lotto :        # 이하 내용 갑자기 삭제 됨.
        pass                 
    
num = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] # 특징: 중복이 없다. 1 - 10까지다
#      0                           9
[1, 2, 3, 4, 5, 6]
[2, 3, 4, 5, 6, 7]

for i in range(10) :
    tmp = randint(0, 9) # 0 - 9 사이의 랜덤한 숫자 생성
    # print(tmp)
    num[0], num[tmp] = num[tmp], num[0]
    # print(num)
print(num) # 랜덤하게 섞인 숫자가 보여져.

for i in range(6) :
    lotto.append(num[i])
print(lotto) 

# 로또 번호로 사용. 6자리. 중복이 없이 랜던함 숫자
ok = []

for i in range(len(mynum)) :  # i = 0, 1, 2, 3, 4, 5
    # print(mynum[i]) # mynum에 있는 숫자들이 하나하나 출력, 리스트에 있는 숫자 출력
    if mynum[i] in lotto : 
       ok.append(num[i])
print(ok)


# ********** 로또 한번 다시 해보기!! **********