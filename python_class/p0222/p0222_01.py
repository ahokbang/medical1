# 복습
# 변수, 함수
a = 1  # 변수, 변수 선언
a() # 함수; 함수는 중괄호를 사용, 새로운 이름을 만들 수 있음
print() # print는 파이썬에서 기본적으로 제공하는 함수

print('hello world!') # 문자열 출력
print(20)
print(100+200) # 숫자 출력이 가능하고 사칙연산을 할 수 있다.
print('10', 20) # 10은 '' 안에 들어가 있으므로 문자
# ,를 사용하면 변수 타입이 달라도 출력할 수 있음
print('10'+10) # 10이 문자이므로 계산할 수 없음.
# +를 사용할 경우에는 같은 타입만 출력가능
print(int('10')+10) # 문자를 숫자로 변환하여 계산
print('10'+str(10)) # 숫자를 문자로 변환하여 출력

print('hello'*20) # 문자를 n번 반복해서 출력

# %d 정수, $f 실수, %s 문자열을 나타낸다.
print('%d, %d' %(5,2))
print('%s, %f, %s' %(8, 3.14, "abc"))

# 소수점 둘째자리까지 출력을 원할 때,
print('%.2f' %(123.45678)) # %와 f 사이에 .2 cnrk

# 총 10자리 빈칸은 0, 소수점 3자리까지 출력
print('%010.3f' %25.05)
print('%10s' %'python') # 문자도 사용 가능

print('{}, {}, {}' .format(758.12, 50, 'string'))
print('{:.1f}, {:d}, {:s}' .format(758.12, 50, 'string')) # 중괄호 안에 써도 되고 안 써도 되고

# \n은 줄바꿈 출력
print('파이썬 수업을 진행하빈다. \n파이썬 기본편입니다.')
# \t는 들여쓰기
print('파이썬 수업을 진행합니다. \t파이썬 기본편입니다.')
# \는 출력 시 줄바꿈은 없으나 표기 시 줄을 바꿔 표시할 수 있다. 
print('파이썬 수업을 진행합니다. \
    파이썬 기본편입니다.')

# print ",'의 사용
print("산에 올라가면 '야호'라고 한다.")
print('산에 올라가면 "야호"라고 한다.')
print("산에 올라가면 \"야호\"라고 한다.")
