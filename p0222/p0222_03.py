# 연습문제
# 숫자 하나를 입력 받아서 구구단을 출력해보세요.
# 2를 입력 받으면 
# 2 * 1 = 2
# 2 * 2 = 4
# 2 * 3 = 6

# 선생님 답
# 문자열로 출력해보기
print('{}*{}={}' .format(2,1,2*1))
print('{}*{}={}' .format(2,2,2*2))
print('{}*{}={}' .format(2,2,2*3))

# 변수를 만들어서 출력
# 3단을 출력
num = 3
print('{}*{}={}' .format(num,1,2*1))
print('{}*{}={}' .format(num,2,2*2))
print('{}*{}={}' .format(num,2,2*3))

# 입력을 받아서 출력
num = input("원하는 단을 입력하세요. >> ")
num = int(num) # 숫자 형태로 바꿈
print('{}*{}={}' .format(num,1,2*1))
print('{}*{}={}' .format(num,2,2*2))
print('{}*{}={}' .format(num,2,2*3))
