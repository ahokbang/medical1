def cal(num1, num2) : # def cal(n1, n2)
    num1 = num1 + 10 # ==> n1 = n1+10 과 같아
    num2 = num2 + 20 # ==> n2 = n2+20
    result = num1 + num2  # ==> resutl = n1 + n2
    return result
                        # 주소값은 같아
# ------------------------------------------

num1 = 5
num2 = 7

result = cal(num1, num2) # 함수 호출

print("현재 숫자 :", num1, num2, result) # 5, 7, 42
# 함수 안에 있는 num1, num2는 지역변수로 함수를 벗어나면 없어지므로 num1, num2는 5, 7


# 키워드 매개변수, 키워드 매개변수는 제일 뒤에 와야 함.
def cal(num1, num2=10) :  # num2가 키워드 매개변수
    num1 = num1 + 10 
    num2 = num2 + 20 
    result = num1 + num2  
    return result

num1 = 5
num2 = 7

result = cal(num1) # 함수 호출

print("현재 숫자 :", num1, num2, result) # 5, 7, 45