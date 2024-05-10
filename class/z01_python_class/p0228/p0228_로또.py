from random import *

# 1 - 45까지의 숫자를 넣어서 

mynum = [] # 1 - 45 사이의 숫자를 입력 받음 (6개)
lotto = [] # 1 - 45 사이의 랜덤한 숫자 6개를 저장

l = []
for i in range(45) :
    i += 1
    l.append(i)
print(l)
    
for i in range(6) :
    num = int(input("1 - 45 사이의 숫자를 입력하세요. >> "))
    mynum.append(num)
print(mynum)

for i in range(100) :
    tmp = randint(0, 44)   # ********** randint는 from random import * 꼭 필요!!! **********
    l[0], l[tmp] = l[tmp], l[0]
print(l)
print(l[tmp]) # 랜덤한 숫자들이 출력 돼

for i in range(6) :
    lotto.append(l[i])
print(lotto)


# 2. 입력숫자와 랜덤숫자 비교 같은 거 출력
# - 매치하는 숫자, 개수
# m = [1, 2, 3] l = [3, 6, 7] 3, 1개 [3]
print(lotto)
print(mynum)
ok = []

for i in range(len(mynum)) :
    if mynum[i] in lotto :
        ok.append(mynum[i])

# 3. 출력
# 4. 로또 번호 생성하기


''' 선생님 풀이
from random import *
# 1. 변수 선언
mynum [] = # 입력을 1 - 45 사이의 숫자를 입력 받음 (6개)
lotto = [] # 1-45 사이의 랜덤한 숫자 6자리 저장

# 2. 입력받은 숫자 6개
# mynum = [] input()를 통해서 숫자 6개를 넣을 예정
for i in range(6) :
    n = int(input("{}번째 숫자를 입력하세요(총 6개). >> ".format(i)))
    mynum.append(n)

# 3. 로또 번호 생성하기 
1 - 45 까지의 숫자
l = []
for i in range(1, 46) :
    l.append(i)
print(i)

a, b = 10, 9
a, b = b, a
num = [0, 1, 2]
num[0], num[2] = num[2], num[0] 
# a = 9, b = 10
위를 이용하여

l 리스트에 1 - 45 중복이 없는 1 - 45까지의 숫자가 들어있음.
[ 1, 2, 3, ... , 45 ] 
  0번방          44번방
 l[0] = 0        l[44] = 45
print('로또 숫자 : {}" .format(l))
for i in range(200) :
    tmp = randint(0,44) # l[0], l[1], l[2], ... , l[44]
    l[0], l[tmp] = l[tmp], l[0]
    
print('로또 숫자 : {}" .format(l))
- l 잘 섞여 있고 중복 없음.
for i in range(6)L
    lotto.append(l[i])
- 랜덤하고 중복이 없는 숫자 6개 생성
print('로또 숫자 : {}" .format(lotto))

* 리스트에 있는지 없는지 알 수 있는 방법은,
m = [1, 2,3]

if 1 in m :
    ok.append(1)

ok = []

# 4. 입력숫자와 랜덤숫자 비교 같은 거 출력
- 매치하는 숫자, 개수,
- m = [1, 2, 3] l = [3, 6, 7] 3, 1개
- ok.append
- lotto [1, 2, 3, 4, 5, 6]
- mynum [1, 2, 3, 4, 5, 6]
list, for, if

for i in ragne(6) : i = 0, 1, 2, 3, 4, 5
    # print(mynum[i]) # mynum에 있는 요소들 출력
    if mynum[i] in lotto :
        ok.append(mynum[i]) 
    
# 5. 출력
print('입력한 숫자 : {}' .format(mynum))
print('로또 숫자 : {}' .format(lotto))
print('당첨된 숫자 : {}' .format(ok))


'''