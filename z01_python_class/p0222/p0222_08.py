# Quiz
# 1. 다음을 출력하시오. 

# 2. 원의 넓이를 출력하시오. (Pi = 3.14195, 반지름 = 10)
Pi = 3.14195
r = 10
print("원의 넓이: {}" .format(Pi*r*r))
print("*"*30) 
# 위에 껀 ppt 문제: skip


# 해보세요.
# 반지름을 입력 받아 원의 넓이와 원의 둘레를 출력하세요.
# 원의 넓이: pi * ( r ** 2)
# 원의 둘레: 2 * pi * r

# 변수: 원의 반지름 r
# pi = 3.14195

r = int(input("원의 반지름을 입력하세요. : "))
pi = 3.14195
print("원의 넓이: {}\n원의 둘레: {}" .format(pi*(r**2), 2*pi*r))

# 선생님 답
r = input("반지름 값을 입력해주세요. >> ")
r = int(r) # 정수로 변환
pi = 3.14195 # 변수 선언, 지정
print('원의 넓이: {}' .format(pi*(r**2)))
print('원의 둘레: {}' .format(2*pi*r))

# 반지름 값을 입력하면 원의 넓이와 둘레를 만들어주는 프로그램을 내가 만든거야.


 