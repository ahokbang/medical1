# 숫자 6개를 입력 받아 출력하시오.
# 1. 숫자 6개 입력
# 2. 숫자 6개 출력
# for i in range(6) :
#     n = int(input("숫자를 입력하세요. >> "))
#     print(n)
    
# # 숫자 1개를 입력 받아 1개를 출력하시오.
# # 1. 숫자 1개 입력
# # 2. 숫자 1개 출력
# n = int(input("숫자를 입력하세요. >> "))
# print(n)

''' 선생님 풀이
숫자 1개 입력 -> 변수 1개 필요
숫자가 1개 초과일 경우 리스트 사용

# 숫자 1개를 입력 받아 1개를 출력하시오.
1. 숫자 1개 입력
2. 숫자 1개 출력
num = input("숫자를 입력하세요.") # input은 str
print(num)

# 숫자 2개를 입력받아 2개 출력하시오.
num = input("숫자를 입력하세요.")
num2 = input("숫자를 입력하세요.")
print(num)
print(num2)

# 숫자 2개의 합을 넣으세요.
num = input("숫자를 입력하세요.")
num2 = input("숫자를 입력하세요.")
print(num)
print(num2)
print(num+num2) -> str이므로 error 발생
str -> int로 바꿔야해
num = int(input("숫자를 입력하세요."))
num2 = int(input("숫자를 입력하세요."))
print(num)
print(num2)
print(num+num2)

# 숫자 5개를 입력받아 5개 출력하시오. 
nums = []
for i in ragne(0, 5) :
    num[i] = int(input("숫자를 입력하세요.")) -> 아래 코드로 수정하심.
    nums.append(int(input("숫자를 입력하세요.")))
print(nums)
'''

# 숫자 5개의 합을 구하세요. ********** 다시 풀기 **********
nums = []
sum = 0
for i in range(0,5) :
    num = int(input("숫자를 입력하세요."))
    nums.append(num)
    sum = nums[i] + 1
print(sum)

''' 선생님 풀이

for i in range(0, 5)

sum = 0
for num in nums:
    sum += num
print("합계 : ", sum)

'''