# 반복문 for문 while문
'''
for i in range(시작, 끝+1, 증감값) :
    수행할 문장
    
while 조건식 : # 조건식이 참일 경우에만 실행할 문장 계속 반복 무한대.
    실행할 문장

변수 = 시작값 # ex) i = 0
while 변수 < 끝값 : # 이 조건이 참일 때
    반복구문
    변수 = 변수 + 증가값 # i = i + 1

'''

# for 문으로 안녕하세요를 3번 출력
for i in range(3) :
    print("안녕하세요.")

for i in range(0, 3, 1) :
    print("for : 안녕하세요.")

# while문으로 작성
i = 0
while i < 3 :
    print('while : 안녕하세요.')
    i = i + 1

# 해보세요.
# for문으로 0 ~ 10까지 출력
for i in range(0, 11) :
    print(i, end=' ')
print()

# while문을 0 ~ 10까지 출력
i = 0
while i < 11 :
    print(i, end=' ')
    i = i + 1
print()

# while을 사용해서 해보세요.
# 1 - 10 사이의 3의 배수를 출력해보세요. 3, 6, 9
i = 1
while i*3 < 11 :
    print(i*3, end=' ')
    i += 1
print()

''' 선생님 풀이
for i in range(1, 11) :
    if i % 3 == 0 :
        print(i)

j = 0
while j < 11 : # 또는 while j <= 10 : 으로 써도 돼
        if j % 3 == 0 :
        print(j , end=" ")
    j += 1 # 위치를 잘 생각해야 해!
    
'''
# 1 - 100 사이의 홀수를 출력해보세요.
i = 1
while i < 101 :
    print(i, end=' ')
    i += 2 # ********** 홀수 조건은 위에가 아니라 여기서! **********
print()

''' 선생님 풀이
for i in range(1, 101) :
    if i % 2 == 1:
        print(i, end=', ')
        
j = 1
while j <= 100 :
    if j % 2 == 1 :
        print(j, end ='\t')
    j += 1
'''
# 1 - 100까지의 합을 구해보세요. ********** 다시 해보기!! 합구하는 거 까먹었어. **********
# - 변수 하나를 더 만들어야 해. sum
sum = 0
for i in range(1, 101) :
    # print(i, end=' ')
    sum += i
print(sum)
print()

i = 1
sum = 0
while i < 101 :
    # print(sum , end=' ')
    sum += i
    i += 1
print(sum)
print()

''' 선생님 풀이
sum = 0
for i in range(1, 101) :
    sum += 1
print(sum)
print()

sum1 = 0
j = 1
while j <= 100 :
    sum1 += j
    j += 1
print(sum1)
'''

while  True : # 무한히 반복시키고자 할 때 사용
    print('ㅋ')   # ctrl + c : 무한 반복 종료

# while 조건문이 참인 경우 반복
# 때문에 while True는 무조건 참이기 때문에 무한히 반복됨
# 무한루프에 들어가면 control + c를 눌러서 강제종료할 수 있다.

# while문을 사용할 때 조건문을 잘 만드는 게 중요하다.

while  1 == 1 : # 무한루프 있으면 그 다음에 있는 문의 색이 연하게 바껴
    print('ㅋ')
    
# break, continue
# break: 반복문을 빠져나와서 다음 단계를 수행한다. 
n = 0
while n < 100:
    print(n, end=' ') # n = 0 : 출력, n = 1 : 출력, n = 2 : 출력, n = 3 : 출력 n = 4 : 출력 및 종료
    if n == 4 :
        break
    n = n + 1
    print('----------')

breakletter =  input("중단할 문자를 입력하세요. >> ")
for letter in 'python' :
    if letter == breakletter : 
        break
    print(letter)

while True : # 무한히 반복
    n = input("숫자를 입력해주세요. >> ")
    print(n)

# 특정 숫자를 사용할 때,
while True : 
    n = input("숫자를 입력해주세요(종료: 0). >> ")
    if n == '0' :
        print("종료되었습니다.")
        break

print("프로그램이 종료되었습니다.")