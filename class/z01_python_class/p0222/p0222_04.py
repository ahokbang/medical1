# 두 수를 입력 받아서 사칙연산을 출력해보세요.
# 변수 n1, n2
# 출력:
# 10 + 3 = 13
# 10 - 3 = 7
# 10 * 3 = 30
# 10 / 3 = 3.333

n1 = input("10을 입력하세요. >> ")
n1 = int(n1)

n2 = input("3을 입력하세요. >> ")
n2 = int(n2)

print("{} + {} = {}" .format(n1, n2, n1+n2))
print("{} - {} = {}" .format(n1, n2, n1-n2))
print("{} * {} = {}" .format(n1, n2, n1*n2))
print("{} / {} = {:.4}" .format(n1, n2, n1/n2))
print("\n")

# 문자열로 출력해보기
print("{} + {} = {}" .format(10, 3, 10+3))
print("{} - {} = {}" .format(10, 3, 10-3))
print("{} * {} = {}" .format(10, 3, 10*3))
print("{} / {} = {:.4}" .format(10, 3, 10/3))
print("\n")

# 변수를 만들어서 출력
n1 = 10
n2 = 3
print("{} + {} = {}" .format(n1, n2, n1+n2))
print("{} - {} = {}" .format(n1, n2, n1-n2))
print("{} * {} = {}" .format(n1, n2, n1*n2))
print("{} / {} = {:.4}" .format(n1, n2, n1/n2))
print("\n")

# 입력을 받아서 출력
n1 = input("10을 입력하세요. >> ")
n1 = int(n1)
n2 = input("3을 입력하세요. >> ")
n2 = int(n2)
print("{} + {} = {}" .format(n1, n2, n1+n2))
print("{} - {} = {}" .format(n1, n2, n1-n2))
print("{} * {} = {}" .format(n1, n2, n1*n2))
print("{} / {} = {:.4}" .format(n1, n2, n1/n2))

# 선생님 답
# 1. 문자열로 4줄 출력 : format을 사용하세요.
print("{} + {} = {}" .format(10, 3, 10+3))
print("{} - {} = {}" .format(10, 3, 10-3))
print("{} * {} = {}" .format(10, 3, 10*3))
print("{} / {} = {:.4}" .format(10, 3, 10/3))

# 2. n1 = 10, n2 = 3 변수를 선언해서 4줄 출력
n1 = 10
n2 = 3
print("{} + {} = {}" .format(n1, n2, n1+n2))
print("{} - {} = {}" .format(n1, n2, n1-n2))
print("{} * {} = {}" .format(n1, n2, n1*n2))
print("{} / {} = {:.4}" .format(n1, n2, n1/n2))

# 3. n1, n2를 입력 받아서 4줄 출력
# 입력
n1 = input("첫번째 숫자를 입력하세요. >> ")
n2 = input("두번째 숫자를 입력하세요. >> ")
# 문자를 정수로
n1 = int(n1)
n2 = int(n2)
# 출력
print("{} + {} = {}" .format(n1, n2, n1+n2))
print("{} - {} = {}" .format(n1, n2, n1-n2))
print("{} * {} = {}" .format(n1, n2, n1*n2))
print("{} / {} = {:.4}" .format(n1, n2, n1/n2))