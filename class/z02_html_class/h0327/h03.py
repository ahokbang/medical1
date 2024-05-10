# 함수선언
def sum(num1, num2):
    return num1+num2

num1 = int(input("숫자를 입력하세요. >> "))
num2 = int(input("숫자를 입력하세요. >> "))

print("두 수의 합 : ", sum(num1, num2))


# 파이썬의 경우 위에서 아래로 내려온 후 실행시키므로 
# 함수의 코드가 위에 있어야 하지만,
# 자바의 경우에는 한꺼번에 확인 후 실행함.