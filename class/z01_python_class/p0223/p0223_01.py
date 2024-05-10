# 복습 #

# 출력 print()
print('문자열') # 문자열 출력
print(10.123) # 숫자 출력
print(123*111) # 사칙연산 후 출력

# %d 정수, %f 실수, %s 문자열을 나타낸다.
print('%d %f %s' %(10,12.1234,'문자'))
print('%.2f'%(22.358894)) # 소수 둘째잘까지 출력

# str.format()
print('문자열을 쓰고 {}' .format(1))
# 정수
print("{0:d}".format(123)) 
# 0은 0번째 위치에 해당하게 할건지, d는 정수니까 정수만 표시한다는 의미
print("{0}".format(123))
print("{}".format(123))
# 실수
print("{0:f}".format(123.456789))
print("{0}".format(123.456789))
print("{}".format(123.456789))
# print("{0:d}".format(123.456789)) 123.456789는 소수이기 때문에 d를 쓰면 error
# : 앞에는 위치를 나타냄
print("{0:.1f}".format(123.456789)) # 소수점 첫째자리까지 표현됨. 
# 0은 생략할 수 있으나 콜론은 생략할 수 없음

# 문자
print("{0:s}".format('문자'))
print("{0}".format('문자'))
print("{}".format('문자'))
# 포맷의 괄호 안의 숫자 순서대로 출력 되는 것
print("{0} {1} {2}" .format('빨', '주', '노')) # [빨 주 노]로 출력
print("{0} {2} {1}" .format('빨', '주', '노')) # [빨 노 주]로 출력

# 변수
number = 10 # 정수 - int
pi = 3.14 # 실수 - float
result = True # bool - True, False
str1 = '문장입니다.' # string
ch = 'A' # 문자
print(number) # 10 출력
print(pi) # 3.14 출력
print(result) # True 출력
print(ch) # A 출력
s1 = '1+1=2'
print(s1) # 1+1=2 출력
s2 = '{}+{}={}'.format(1,1,2)
print(s2) # 1+1=2로 출력

a = 100
a = a + 1
a += 1 # a = a + 1와 같은 표기
# +=, -=, *=, /=, //=, $=: 변수 반복 시 사용 가능 

a, b = 10, 20
a = 10
b = 10

print(a == b) # True
print(a != b) # False
print(a > b) # False
print(a >= b) # True

# 논리연산자
# and (둘이 참이어야 참) or (둘중에 하나만 참이어도 참) not (참이면 거짓, 거짓이면 참)
a, b, c = 100, 200, 150
result = (a > c) and (b > c) # false and true -> False
print(result)

r1 = True
print(not r1) # r1은 true니까 not ture -> [False] 출력

# 입력 받기 input()
name = input("이름을 입력하세요. : ")
print("당신의 이름은 {}입니다." .format(name))
# ************** input()의 결과값은 문자형!!! 꼭 기억하기!!! ***************
age = input("당신의 나이를 입력하세요: ")
# print("당신은 내년에 {}살입니다." .format(age+1)) # 오류, age가 문자형이므로 계산할 수 없어.
age = int(input("당신의 나이를 입력하세요. : "))
print("당신은 내년에 {}살입니다." .format(age+1)) # 출력 됨

# if 조건문
# if 조건문 1:
#    실행문1
# [else:
#    실행문2 ]
# '조건문 1이 참이면 실행문 1을 실행 후 종료한다',
# '조건문 1이 거짓이면 실행문 1를 실행 후 종료한다'는 의미

f = 'apple'
if f == 'apple' :
    print('먹는다.')
else:
    print("버린다.")



