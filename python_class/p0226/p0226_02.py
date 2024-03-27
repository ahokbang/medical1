'''
해보세요.

1. 나이가 10살 이상이고, 150 이상만 탑승 가능
나이, 키를 입력 받아 [탑승가능], [탑승불가능]을 출력해보세요.

'''
age = int(input("나이를 입력하세요. >> "))
height = int(input("키를 입력하세요. >> "))

if (age >= 10) and (height >= 150) :
    print("[탑승가능]")
else: 
    print("[탑승불가능]")

# 선생님 답
# input() 함수를 사용할 경우 문자열로 입력 받는다. 
# print() 함수는 출력
age = int(input("나이를 입력하세요. >> "))
height = int(input("키를 입력하세요. >> "))
print(age, height)
age = input("나이")
age = int(age)

if age >= 10:
    if height >= 150 : 
        print("탑승 가능")
    else :
        print("탑승불가능") # 나이는 10살 이상이나 키 미달
else :
    print("탑승 불가능")

'''
2. 숫자 3개 (정수를) 입력 받고, 연산 1개를 입력 받아 
ex) 조건문 연산자가 +를 입력 받으면,
a + b + c = d의 형태로 출력 (1 + 2 + 3 = 6)
연산자가 -로 입력을 받으면: (1 - 2 - 3 = -4)  
+++ --- *** /// (나누기값은 둘째자리까지 표현)
숫자 3개로 계산기
'''

num1 = int(input("첫번째 숫자를 입력하세요. >> "))
num2 = int(input("두번째 숫자를 입력하세요. >> "))
num3 = int(input("세번째 숫자를 입력하세요. >> "))
cal = input("연산 1개를 입력하세요. >> ")

if cal == "+" :
    print("{} + {} + {} = {}" .format(num1, num2, num3, num1 + num2 + num3))
if cal == "-" :
    print("{} - {} - {} = {}" .format(num1, num2, num3, num1 - num2 - num3))
if cal == "*" :
    print("{} * {} * {} = {}" .format(num1, num2, num3, num1 * num2 * num3))
if cal == "/" :
    print("{} / {} / {} = {:.2f}" .format(num1, num2, num3, num1 / num2 / num3))


# 선생님 답
a = int(input("첫번째 숫자 >> "))
b = int(input("두번째 숫자 >> "))
c = int(input("세번째 숫자 >> "))

cal = input("연산자를 입력하세요(+,-,*,/). >> ")

if cal == '+' : # cal은 문자열이기 때문에 꼭 '' 있어야 해.
    result = a + b + c
    print('{} + {} + {} = {}'.format(a, b, c, result))
elif cal == '-':
    result = a - b - c
    print('{} - {} - {} = {}'.format(a, b, c, result))
elif cal == '*' :
    result = a * b * c
    print('{} * {} * {} = {}'.format(a, b, c, result))
elif cal == '/' :
    result = a / b / c
    print('{} / {} / {} = {:.2f}'.format(a, b, c, result))
else :
    print("잘못 입력하셨습니다. 다시 입력하세요.")
    
# 결과값만 보고 싶다면,
result = 0 # 결과값을 먼저 0으로 선언해주고, 
print("{}, {}, {}연산의 결과값은 : {}" .format(a, b, c, result))