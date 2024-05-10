# 해보세요.
# 1. 숫자 두개를 입력 받아서 나누기 값, 몫 값, 나머지 값을 출력
n1 = int(input("첫번째 숫자를 입력하세요. : "))
n2 = int(input("두번째 숫자를 입력하세요. : "))

print("나누기 값: {}/{}={}" .format(n1, n2, n1/n2))
print("몫 값: {}//{}={}" .format(n1, n2, n1//n2))
print("나머지 값: {}%{}={}" .format(n1, n2, n1%n2))

# 선생님 답
r1 = n1/n2
r2 = n1//n2
r3 = n1 % n2
print(r1, r2, r3)

# 2. 3개의 수의 합을 구하세요.
s1, s2, s3 = '100', '100.123', '99.9'

print("세 수의 합을 구하세요: {} + {} + {} = {}" .format(s1, s2, s3, int(s1)+float(s2)+float(s3)))
# ********** 실수는 float로 형 변환하기!! 잊지마!! **********

# 선생님 답
s1, s2, s3 = int('100'), float('100.123'), float('99.9')

# 또는 
s1 = '100' # => input('숫자입력 >> ')
s2 = '100.123'
s3 = '99.9'

a1 = int(s1)
a2 = float(s2)
a3 = float(s3)

# 또는 
result = int(s1)+float(s2)+float(s3)
print("합은 {}입니다." .format(result))
