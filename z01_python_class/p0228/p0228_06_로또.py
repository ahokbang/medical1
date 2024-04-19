from random import *

n1 = randrange(1,11) # 1 - 10 까지의 정수
n2 = randint(1,10) # 1 - 10까지의 정수

# 랜덤한 숫자 6개 lotto 리스트에 넣고
# 내가 입력한 숫자 6개는 mynum 리스트에 넣어주세요.
lotto = []
mynum = []

for i in range(6) : 
    n1 = randrange(1, 11) # ********** n1을 다시 언급해야해. for 안에 들어있어야 반복하니까!! **********
    lotto.append(n1)

for i in range(6) :
    n = input("1~10 중에 숫자를 입력해주세요. >> ")
    mynum.append(n)

print(lotto)
print(mynum)


''' 선생님 풀이
# 1. 변수 선언
lotto = []
munum = []

# 2. 숫자 6개 입력받기(내가 입력한 숫자 6개는 mynum 리스트에)
for i in range(6) :
    n = int(input("{}번째 숫자를 입력해주세요. >> " .forma(i+1)))
    mynum.append(n)

# 3. 로또 숫자 생성(랜덤한 숫자 6개 lotto 리스트에 넣고)
for i in range(6) :
    tmp = randint(1,10)
    lotto.append(tmp)
- 중복 없이 숫자를 받고 싶어
f = ['딸기', '포도']
if '딸기' in f : 
    print("딸기가 있습니다.)
이걸 사용해서 중복 없이 숫자를 받을 수 있어.

for i in range(6) :
    tmp = randint(1,10)
        in tmp not in lotto : # 만약에 랜덤숫자(tmp)가 lotto 리스트에 없다면 추가해라
            lotto.append(tmp) 
print(lotto) # 동일한 숫자가 1개 있으면 숫자가 5개만 출력하게 돼

# 4. 입력숫자와 랜덤숫자 비교

print("입력하신 숫자는 {}입니다." .format(lotto))
print("입력하신 숫자는 {}입니다." .format(mynum))
'''

