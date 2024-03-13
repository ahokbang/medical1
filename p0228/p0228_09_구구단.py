# 중첩 for
# 중첩 if문 처럼 for문 안에 for가 있는 형태
for i in range(3) : # i = 0, 1, 2
    print("안녕")
    for j in range(2) : # j = 0, 1
        print('반가워')
''' 
프로그램은 순차적으로 내려와.
- i = 0 일 때,
  j = 0, j = 1
- i = 1 일 때,
j = 0, j = 1
- i = 2 일 때,
j = 0, j = 1

큰 거 반복 안에 작은 거가 반복돼.
'''

for i in range(3) : # i = 0, 1, 2
    print("i = ", i)
    for j in range(2) : # j = 0, 1
        print('j = ', j)


# for 문을 이용해서 2단을 출력
for i in range(1, 10) :
    print("2*{}={}" .format(i, 2*i))
    

# 입력 받은 숫자의 단을 출력하세요. >>
# - 3을 입력 받으면 3단 출력, 4단 입력 받으면 4단 출력

n = int(input("1-9 사이의 숫자를 입력하세요. >> "))
for i in range(1, 10) :
    print("{} * {} = {}" .format(n, i, n*i))

for i in range(2, 10) : # 2단부터 9단까지 출력
    for j in range(1*10) : # *1 ~ *9
        print('{} * {} = {}' .format(i, j, i*j))
        

for j in range(5): # j = 0 1 2 3 4 
    print(j+1, '번째 출력')
    for i in range(1,6) : # i = 1 2 3 4 5
        print(i, end=" ") # 1 2 3 4 5 를 한 줄로 출력
    print() # 줄바꿈
print('for 끝')

print('-'*35)

# [2단], [3단], ... 나오게 추가하기
for i in range(2,10) :
    print('[{}단]' .format(i))
    for j in range(1, 10) :
        print('{} * {} = {}' .format(i, j, i*j), end=' ')
    print()   # ********** 이해하기!!  **********

print('-'*35)

# 짝수 단만 출력해보세요.
for i in range(2, 10, 2) :
    print("[{}단]" .format(i))
    for j in range(1, 10) :
        print("{} * {} = {}" .format(i, j, i*j), end=' ')
    print()

# 선생님 풀이
for i in range(2, 10) : 
    if i%2 == 0:
        print("[{}단]" .format(i))
    for j in range(1, 10) :
        print("{} * {} = {}" .format(i, j, i*j), end=' ')
    print()   



print('-'*35)

# 홀수 단만 출력해보세요.
for i in range(3, 10, 2) :
    print("[{}단]" .format(i))
    for j in range(1, 10) :
        print("{} * {} = {}" .format(i, j, i*j), end=' ')
    print()

print('-'*35)

# ( *1, 3, 5, 7, 9) 출력
for i in range(2, 10) :
    print("[{}단]" .format(i))
    for j in range(1,10, 2) :
        print("{} * {} = {}" .format(i, j, i*j))
    
print('-'*35)

# ********** 문제 더 있었는지 확인해보기!!!  **********
