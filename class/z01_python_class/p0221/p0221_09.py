# 두 수를 입력 받아서 사칙연산을 출력해보세요.
# 예: 30, 6을 입력 받아서
# 출력:
# 30 + 6 = 36
# 30 - 6 = 24
# 30 * 6 = 180
# 30 / 6 = 5.0

a = 30
b = 6
# 합
print("두 수의 합: %d + %d = %d"%(a,b,a+b))
print("두 수의 합:", a, "+", b, "=", a+b)
print("두 수의 합: {} + {} = {}".format(a, b, a+b))
print("두 수의 합:"+str(a)+"+"+str(b)+"="+str(a+b))


#차
print("두 수의 차: %d - %d = %d"%(a,b,a-b))
print("두 수의 곱: %d * %d = %d"%(a,b,a*b))
print("두 수의 나누기: %d / %d = %d"%(a,b,a/b))

# num1 = input("첫번째 숫자를 입력하세요. >> ")
# num2 = input("두번째 숫자를 입력하세요. >> ")

# print("두 수의 합: ", int(num1)+int(num2))
# print("두 수의 차: ", int(num1)-int(num2))
# print("두 수의 곱: ", int(num1)*int(num2))
# print("두 수의 나누기: ", int(num1)/int(num2))

# 선생님 답 1; 변수를 사용해서 출력하기
a = 30
b = 6
print(a, '+', b, '=', a+b)
print(a, '-', b, '=', a-b)
print(a, '*', b, '=', a*b)
print(a, '/', b, '=', a/b)

# 선생님 답 2; input 함수 사용해서 입력받은 거 출력하기
c = input("첫번째 숫자를 입력하세요. >> ") 
d = input("두번째 숫자를 입력하세요. >> ")

print(c, '+', d, '=', int(a)+int(b))

#input 자체를 형변환 해도 돼. 
e = int(input("첫번째 숫자를 입력하세요. >> "))
f = int(input("첫번째 숫자를 입력하세요. >> "))

print(e,'+', f, '=', e+f)



