'''
반복문 - for, while
for 변수 in 반복가능한데이터 :
    수행문
    
for 카운터변수 in range(시작값, 끝값+1, 증감값) :
    수행문


'''
for i in range(0, 10, 1) : # 0, 1, 2, 3, 4, 5, 6, 7, 8, 9
    print("증감 1: 수행문입니다.")
   
for i in range(0, 10, 2) : # 0, 2, 4, 6, 8
    print("증감 2: 수행문입니다.")
 
for i in range(0,3) : # 증감값이 1일 경우에는 생략 가능, 3번 반복하라는 의미
    print("두번째 수행문입니다.")
    
for i in range(5) : # 5번 반복해라.
    print("세번째 수행문입니다.")

print('-'*35)

for i in range(3) : # 3번 반복해라. 1증가 생략, 0부터 생략
    print(i)

# 카운터변수 i를 사용하지 않을 때 _로 사용 가능    
for _ in range(7) : # 안녕하세요. 7번 반복
    print("안녕하세요.")

for i in range(10, 0, -2) :
    print(i, '증감 2: 수행문입니다.')

l1 = [100, 200, 300, 400, 500]
#      0    1    2    3    4
# 리스트 안 요소 확인 in / not in
'''
for 변수 in 리스트명 :
    실행문
    
for 변수 in range(len(리스트명)) :
    실행문
    리스트명[변수]
'''
for n in l1 : # 리스트 안의 요소가 하나씩 출력 돼.
    print(n)
    
for i in range(len(l1)) :
    print(i) # 0, 1, 2, 3, 4,
    print(l1[i]) #l1[0], l1[1], l1[2], ...

print()

'''
1. for 문을 사용해서 1-100 사이의 홀수를 출력해보세요.
   1) if 사용하지 않음(증감 이용)
   2) if 사용
   
2. 50 ~ 1 사이의 6의 배수를 역순으로 출력해보세요.
출력: 48, 42, 36, 30, 24, 18, 12, 6
'''

# 1-1) 
for i in range(1, 101, 2) :
    print(i, end=' ')

print()

# 선생님 답
for i in range(1, 101, 1) : # 1 ~ 100까지 출력
    print(i, end=" ")
# 홀수를 구해야 하므로 증감값 변경

for i in range(1, 101, 2) :
    print(i, end=' ')
    
print() # 줄바꿈

# 1-2)
for i in range(1,101) :
    if i % 2 == 1 :
        print(i, end=' ')

print()

# 선생님 답
for i in range(100) :
    if (i+1) % 2 == 1 :
        print(i+1, end=", ")
        
print()

# 2.
for i in range(48, 1, -6) :
    print(i, end=" ")
    
print()

# 선생님 답
for i in range(48, 0, -6) :
    print(i, end=' ')
print ()

'''
input() 사용
입력: 두 개의 숫자를 입력 받음
출력: 사칙연산
      a + b = c
      a - b = d
      a * b = e
      a / b = f
계산을 10번 반복하는 코드를 만드세요(입력도 10번 반복됨).

처음에 4, 5를 입력하면 4+5=9, 4-5=1, ...
두번째로 8, 1 입력하면 8+1=9, 8-1=7, ...
세번째로 9, 3 입력하면 9+3=12, ...
'''

for i in range(10) :
    n1 = int(input("첫번째 숫자를 입력하세요.>> "))
    n2 = int(input("두번째 숫자를 입력하세요. >> "))
    print("{} + {} = {}" .format(n1, n2, n1+n2))
    print("{} - {} = {}" .format(n1, n2, n1-n2))
    print("{} * {} = {}" .format(n1, n2, n1*n2))
    print("{} / {} = {:.2f}" .format(n1, n2, n1/n2))

''' 선생님 답
for i in range(10) :
    n1 = int(input("첫번째 숫자 입력 >> "))
    n2 = int(input("두번째 숫자 입력 >> "))
        
    print("{} + {} = {}" .format(n1, n2, n1+n2))
    print("{} - {} = {}" .format(n1, n2, n1-n2))
    print("{} * {} = {}" .format(n1, n2, n1*n2))
    print("{} / {} = {:.2f}" .format(n1, n2, n1/n2))
'''

# 연산자도 입력 받아보기
for i in range(10) :
    n1 = int(input("첫번째 숫자를 입력하세요.>> "))
    n2 = int(input("두번째 숫자를 입력하세요. >> "))
    cal = input("사칙연산을 입력하세요(+, -, *, /). >> ")
    
    if cal == "+" : 
        print("{} + {} = {}" .format(n1, n2, n1+n2))
    elif cal == "-" :
        print("{} - {} = {}" .format(n1, n2, n1-n2))
    elif cal == "*" :
        print("{} * {} = {}" .format(n1, n2, n1*n2))
    elif cal == "/" :
        print("{} / {} = {:.2f}" .format(n1, n2, n1/n2))
    else :
        print("잘못 입력하셨습니다.")
        
''' 선생님 답
for i in range(10) :
    n1 = int(input("첫번째 숫자 입력 >> "))
    n2 = int(input("두번째 숫자 입력 >> "))
    
    if cal == "+" :    
        print("{} + {} = {}" .format(n1, n2, n1+n2))
    elif cal == '-' :
        print("{} - {} = {}" .format(n1, n2, n1-n2))
    elif cal == "*" :
        print("{} * {} = {}" .format(n1, n2, n1*n2))
    elif cal == "/" :
        print("{} / {} = {:.2f}" .format(n1, n2, n1/n2))
    else :
        print("잘못입력하셨습니다. 다시 입력하세요.") # 잘못 입력했을 경우 다시 위로 가서 다시 작성하게 돼.
    
'''