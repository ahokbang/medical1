# 관계연산자
# 어떤것이 크거나 작거나 같은지를 비교
# 참은 True, 거짓은 False로 표시
# 주로 조건문, 반복문에서 사용. 단독으로는 많이 사용하지 않음
# 수식1 == 수식2 : 수식 1과 수식 2가 같은지 평가
print(3==6) # False
# 수식1 != 수식2 : 수식 1과 수식 2가 같이 않음을 평가. 프로그램 내에서 !는 not을 의미
print(3!=6) # True
# a = 6; 6을 a에 대입
# a == 6; a와 6이 같은지를 비교/평가
# 수식1 > 수식2 : 수식 1이 수식 2보다 큰가를 평가
# 수식1 >= 수식2 : 수식 1이 수식 2보다 크거나 같은가를 평가
# <, <= 작은가, 작거나 같은가
# 등호는 뒤에 사용 
print("*"*30)
num = 95 
print(num > 90)
print(num <= 90)
print(num == 90)
print(num != 90)

print(90 <= num < 100)

print("*"*30)

# 논리연산자
# 조건문, 반복문에서 사용
# and(그리고), or(또는), not(부정) 세가지 종류
# and: 둘 다 참이어야 함.
# or: 둘 중 하나라도 참이면 참
# not: 참이면 거짓, 거짓이면 참
kor = 90
avg = 80
print(kor > 80) # Ture
print(avg > 90) # False
print(kor > 80 and avg > 90) # ( True and False ) => False
print(kor > 80 or avg > 90) # ( True or False ) => True
print(not avg >= 90) # not(False) => True