# # 함수선언
# def plus(v1, v2) :
#     v1 = 100 + v1 # 101
#     v2 = 200 + v2 # 202
    
# # 함수호출
# v1 = 1
# v2 = 2
# plus(v1, v2)

# # 출력 
# print(v1, v2) # 1 2


# 함수선언의 v1, v2와 함수호출의 v1, v2는 이름만 같고 다른 거야. 이름이 같다고 똑같은 변수가 아니야. 
# return을 사용하면 같게 할 수 있어.

# 함수선언
def plus(v1, v2) :
    v1 = 100 + v1 # 101
    v2 = 200 + v2 # 202
    return v1, v2 # 함수밖에서 사용하려면 return 값을 돌려줘야 함. 
    
# 함수호출
v1 = 1
v2 = 2
v1, v2 = plus(v1, v2)

# 출력 
print(v1, v2) # 101 202

for i in range(10) :
    sum = 0
    sum += i 
    # print(i)
    
for i in range(5) :
    result = 1
    result *= 1
    # print(i)
    
print(sum)
print(result)



def cal(input1, input2):
    result1 = input1 + input2
    result2 = input1 - input2
    result3 = input1 * input2
    result4 = input1 /input2
    
    return result1, result2, result3, result4
   # return input1+input2, input1-input2, input1*input2, input1/input2
    
input1 = int(input("첫번째 숫자를 입력하세요."))
input2 = int(input("두번째 숫자를 입력하세요."))

# 함수의 return을 사용해서 입력된 두 수의 사칙연산 결과값을 출력하시오. 
# 20, 10
# 결과값 : +: 30, - : 10, * : 200, / :2
result1, result2, result3, result4  = cal(input1, input2)
data = cal(input1, input2)
print("더하기 결과값 : ", result1)
print("빼기 결과값 : ", result2)
print("곱하기 결과값 : ", result3)
print("나누 결과값 : ", result4)
print("결과값 : ", data) # 튜플형태
print("더하기 결과값 : ", data[0])