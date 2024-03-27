'''
지역변수의 리스트와 전역변수의리스트
- 전역변수 리스트를 매개변수로 전달 시 return을 받지 않아도 됨.
'''

'''
def multi(num1, num2) :
    result_list = [] # (1) # 지역변수
    result_list.append(num1+num2)
    result_list.append(num1-num2)
    return result_list
   
num1 = int(input("숫자를 입력하세요. >> "))
num2 = int(input("숫자를 입력하세요. >> "))
result_list = multi(num1, num2) # (3) 
print("결과값 : ", result_list) # (2)
'''
# 함수 안에서 정의한 리스트는 지역변수기 때문에 함수를 벗어난 (2)번 자리에서 출력될 수 없어. error
# 그래서 (3)에 "result_list ="를 추가
# 또는
def multi(num1, num2, result_list) :
    result_list.append(num1+num2)
    result_list.append(num1-num2)
    
result_list = []    # 전역변수
num1 = int(input("숫자를 입력하세요. >> "))
num2 = int(input("숫자를 입력하세요. >> "))
multi(num1, num2, result_list)
print("결과값 : ", result_list) # (2)
