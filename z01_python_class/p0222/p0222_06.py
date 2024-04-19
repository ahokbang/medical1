# 산술 연산자
# + - * /
a = 5
b = 3
result = a + b
result = a -b
result = a * b
result = a / b
print(result)
result = a // b # 몫 4//2 몫: 2, 나머지: 0
print(result)
result = a % b # 나머지 # 꼭 기억하기!!
print(result)
result = a ** b # 제곱
print(result)

c = 10
d = 20
c , d = 100, 200

# 산술연산자 우선순위
# 곱셉, 나눗셈 먼저 계산 후 덧셈, 뺄셈 순으로 진행
# 괄호가 있으면 괄호 먼저 계산, 괄호가 없을 경우에는 왼쪽에서 오른쪽 방향으로 계산
r1 = 2 + 2 - 2 * 2 / 2 * 2 # 괄호 사용을 추천
r2 = 2 - (2 / 2)

# 다른 자료형으로 연산
str1 = "문자열"
n1 = 10
print(str1*n1) # 문자열 10번 반복
#print(str1+n1) # 오류. 문자열과 숫자는 같이 쓸 수 없어. 

# 문자열이 정수나 실수일 경우 int() float()를 사용해서 변환
s1 = "100"
s2 = "10.123"
print(int(s1)+1)
print(float(s2)+1)

# 숫자가 아닌 것을 변환할 수 없다.
#n = int("안녕하세요") # error

# 숫자를 문자로 바꾸고 싶으면 str() 사용
n1 = 100
n2 = 10.123
print(str(n1)+"1")
print(str(n2)+"1")

# 핸드폰 번호 출력하고 싶을 때, 0이맨 앞으로 올 수 없어.
p = 1012341234
print("0"+str(p))
# 또는
p = 12341234
print("010"+str(p))


# 숫자 두 개를 입력 받아서 나누기 값, 몫, 나머지 값을 구하세요.
# ex) n1 = 4 n2 = 2
# 출력: 
# 나누기값 : (2.0), 몫 : (2), 나머지 : (0)

n1 = int(input("첫번째 숫자를 입력하세요. : "))
n2 = int(input("두번째 숫자를 입력하세요. : "))

print("나누기값: {}" .format(n1/n2))
print("몫: {}" .format(n1//n2))
print("나머지: {}" .format(n1%n2))

# 선생님 답

n1 = input("첫번째 숫자를 입력하세요. >> ")
n2 = input("두번째 숫자를 입력하세요. >> ")
# 문자를 숫자로 변경
n1, n2 = int(n1), int(n2)
# 출력
print("나누기: {}\n몫: {}\n나머지:{}" .format(n1/n2,n1//n2,n1%n2))
print("나누기: {}   몫: {}   나머지:{}" .format(n1/n2,n1//n2,n1%n2))
# 소숫점 표현; 소숫점 첫째자리까지 표현
print("나누기: {:.1f}   몫: {}   나머지:{}" .format(n1/n2,n1//n2,n1%n2))

