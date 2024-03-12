print(200+100)
print(200-100)
print(200*100)
print(200/100)

# 해보세요
# 1. 200 -> 50으로 바꿔서 출력해보세요
print(50+100)
print(50-100)
print(50*100)
print(50/100)

# 2. 100 -> 10
print(50+10)
print(50-10)
print(50*10)
print(50/10)

# 3. 10 -> 30
print(50+30)
print(50-30)
print(50*30)
print(50/30)

# 4. 50 -> 20
print(20+30)
print(20-30)
print(20*30)
print(20/30)

# 변수를 사용
# 100 -> 1000, 10 -> 5
a = 100
b = 10
print(a+b)
print(a-b)
print(a*b)
print(a/b)

print('*'*20)
# 함수를 사용하여 사칙연산 계산
def cal(a, b):
    print(a+b)
    print(a-b)
    print(a*b)
    print(a/b)
    
cal(100,5)
print('-'*20)
cal(50,2)

num1 = 10
num2 = 5
print(str(num1)+'+'+str(num2)+'='+str(num1+num2)) # +는 띄어쓰기 불가
print(num1, '+', num2, '=', num1+num2) # , 는 띄어쓰기가 가능
print('%d+%d=%d'%(num1, num2, num1+num2))
print('{}+{}={}'.format(num1, num2, num1+num2))

# 수식을 10 - 5 = 5로 출력하기. 4가지 방법 다 사용
num1 = 10
num2 = 5
print(str(num1)+'-'+str(num2)+'='+str(num1-num2))
print(num1,'-', num2, '=', num1-num2)
print('%d - %d = %d'%(num1, num2, num1-num2)) # 숫자 지정 할 때하는 % 뒤에는 꼭 괄호 필요!
print('{}-{}={}'.format(num1, num2, num1-num2))

