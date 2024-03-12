# 반복문
# 안녕하세요 다섯번 출력
print("안녕하세요."*5)

# 또는

print("안녕하세요.")
print("안녕하세요.")
print("안녕하세요.")
print("안녕하세요.")
print("안녕하세요.")

'''
for 변수 in 반복가능한데이터: 
    수행할 문장
'''

# 순찬적으로 커질 때 range를 사용한다. 
for i in range(0, 5, 1): # range(시작값, 끝값+1, 증가값)
                         # i가 0, 1, 2, 3, 4
    print("안녕")

for i in range(0, 5, 1): # range(시작값, 끝값+1, 증가값)
                         # i가 0, 1, 2, 3, 4
    print(i, "안녕")
    
for i in range(0,5): # 증가값이 1인 경우 생략 가능
    print(i, "Hi")
    
for i in range(4) : # n번 반복할 경우 range(n)을 사용할 수 있다.
    print("hello")

for _ in range(2) : # i 대신 언더바(_) 사용 가능
    print("반갑습니다.")

for i in range(5): # 5번 반복해라. 
    num = input("숫자를 입력하세요. >> ")
    print("입력하신 숫자는 : {}" .format(num))


# for 뒤에 오는 카운터 변수 주로 i, j 카운터 변수 사용. 필요 시 k, l, ... 추가 사용
# 카운터 변수는 반보 실행될 때마다 현재 실행 횟수에 해당하는 숫자가 들어감.
# 가장 처음은 실행한 적이 없으므로 0이 된다. 

for i in range(10): # 증가값이 1인 경우 생략
    print(i)
    # 0 1 2 3 4 5 6 7 8 9 

srt1 = "안녕하세요."
for i in srt1 :
    print(i)
    # 안녕하세요의 문자들이 하나씩 보여져

# 해보세요. 
# 1. 1에서부터 15까지 출력해보세요.
for i in range(1,16) :
    print(i)

# 2. 10을 4번 반복해서 출력해보세요.
for i in range(4) :
    print(10)

# 3. helloworld를 6번 반복해서 출력해보세요.
for i in range(6) :
    print("helloworld")

# 4. 1 ~ 100 사이의 2의 배수를 출력해보세요. (2, 4, 6, ...)
for i in range(2, 101,2) :
    print(i)

# 5. 1 ~ 100 사이의 5의 배수를 출력해보세요. (5, 10, 15, ...)
for i in range(5, 101, 5) :
    print(i)
    
''' 선생님 답
1. 
for i in range(1, 16, 1) :
    print(i)
또는
for i range(15) :
    print(i+1)
        
2.
for i range(4) :
    print(10)
    
3. 
for i in range(6) :
    print(i+1, "helloworld")   # i + 1 ; 이해가 안돼 ******* +1 없어도 되지 않나? **********
    
4. 
for i in range(2, 100, 2)
    print(i, end='') # end = '' : 줄바꿈 없이 나와. 한 줄로.

print()    # 줄바꿈된 빈공백

5.
fir i in range(5, 100, 5)

'''