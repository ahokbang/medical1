# 함수선언
def cal(num1, num2) : # ***** 이거 다시 복기 *****
    sum = 0
    if num1 > num2 : # ***** 외우기 *****
        num1, num2 = num2, num1 # 2개 변수 취환
    
    for i in range(num1, num2+1, 1) :
        sum += i
    return sum

# 두 수를 입력받아 입력한 두 수 사이의 합계를 구하는 프로그램을 구현하시오.
# 1, 10 -> 1+2+3+...+10 = 55

sum = 0
num1 = int(input("첫번째 숫자를 입력하세요. >> "))
num2 = int(input("두번째 숫자를 입력하세요. >> "))

sum = cal(num1, num2)

print("합계 : ", sum)


# 자바, 자바스크립트 등 다른 프로그램에서 num1, num2 바꿔주는 방법
def cal(num1, num2) : # ***** 이거 다시 복기 *****
    sum = 0
    temp = 0
    if num1 > num2 : # ***** 외우기 *****
        temp = num1
        num1 = num2
        num2 = temp
    for i in range(num1, num2+1, 1) :
        sum += i
    return sum