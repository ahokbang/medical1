print("Hello Python")

print("Hello! " *3)
print("혼자 공부하다 모르면 동영상 강의를 참고하세요!")

# 참/거짓
print( 5 > 10)
print( 5 < 10)
print(True)
print(False
      ) 
print(True) # 대소문자 구분해, 참은 꼭 t가 대문자여야 해!
print(not True) #False
print(not (5>10)) #True

# "" '' 안에 잇는 것은 문자열이다.
print(0*10) #0
print("0" *10)

print(100) #숫자
print("100") #문자

print("100+100")
print(100+100) #숫자이기 때문에 계산값이 출력

print('숫자는 %d' %200) # %d 정수를 의미, 노란색 %뒤에 있는 숫자가 d로 들어가
print('숫자는 %d'%300)
print('%d' %200)
print("%d + %d = %d" %(2,3, 2+3)) # 노란색 퍼센트 뒤의 숫자가 순차적으로 대응

# 서로 짝이 맞지 않으면 오류를 발생시킨다.
# print ("%d"%(100,200))
# print(%d %d"%(10))
print("%d*%d=%d"%(2,1,2))
print("%d*%d=%d"%(1,2,1*2))

# 깔끔한 출력
print('%d'%123)
print('%7d' %123) # 꼭 7일 필요는 없어; 공백 생성, 123에서 3이 7번째 자리에 와
print('%7d' %123) # 7자리 숫자를 보여줌. 빈 공백으로 채움
print('%5d'%123) # 3이 5번째 자리에 와
print('%05d'%123) # 5자리 숫자를 보여줌. 빈 공백은 0으로 채움

# %d: 정수
# %f: 실수
print('%d'%123.45)
print('%f'%123.45)

print('%7.1f'%123.45) # 소숫점을 포함해서 총 7자리 출력
# 빈 공백으로 채움. 소숫점 이하는 1자리까지 표현; 7.1에서 .1이 소숫점 이하 1자리 의미
print('%07.1f'%123.45)
# 소숫점 이하는 3자리로 표현하고 빈 공백은 0으로 채움
print('%07.3f'%123.45)

print('%f'%12.3456)
print('%.2f'%12.456) # 반올림 자동
print('%.3f'%12.34567)

# 문자열은 %s를 사용
print('안녕하세요')
print('%s'%'반갑습니다')

# 문자는 %c
print('%s'%'a')
print('%c'%'a')

# Quiz
# 1. 소수점 둘째자리까지 출력하시오.
# 소수점 => 실수 => %f
print("%.2f"%758.12345678) 

# 2. 총 10자리, 빈칸은 0으로 채워 소수점 2자리까지 출력하시오.
print("%010.2f"%25.05)

# 3. 변수 150.15를 정수, 실수, 문자열로 출력하시오.
# 정수: $d, 실수: %f, 문자열: %s

# 정수
print("%d"%150.15)
#실수
print("%f"%150.15)
# 문자열
print("%s"%"150.15")

# 4. *을 10개 출력하시오.
print("%s"%"*"*10)
print("*"*10)
# print("**********") 도 돼