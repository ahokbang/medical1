# 람다식 함수(=무명함수)
'''
def sum(num1, num2) :
    s = num1 + num2
    return s
'''

# 위의 함수는 아래 처럼 쓸 수 있어
def sum(num1, num2) :
    return num1+num2

print(sum(10,20))

a = lambda num1, num2 : num1+num2
print(a(10,20))