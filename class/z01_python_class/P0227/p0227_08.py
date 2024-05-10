'''
# 반복문
for 변수 in range(시작값, 끝값+1, 증가값) :


'''

for i in range(3) : # i - 0, 1, 2
    print("안녕")
    # i = 0일 때
    # i = 1일 때
    # i = 2일 때

for i in range(3) : # i = 0, 1, 2
    print(i) 
    
# i = 0, 1, 2, 3, ...
# i = 1, 2, 3, 4, 5, ...

for i in range(100) :
    print(i+1)
    
sum1 = 0
for i in range(1, 6, 1) :
    sum1 = sum1 + i


# 숫자 한개를 입력 받아서 1부터 입력한 수까지의 합을 구하세요.
# for i in range(1,   ) :
#     합계
# 합계 출력

sum = 0

n1 = int(input("숫자 하나를 입력하세요. >> "))

for i in range(1, n1+1, 1) : 
    sum = sum + i
print(sum)


# 짝수의 합만 구해보세요. if 사용하면 되지 않을까요?
# if 안 사용 한 거
sumen = 0

for i in range(0,n1+1,2) :
    sumen = sumen + i
print(sumen)

# if 사용 한 거
sumen = 0

for i in range(0,n1+1,1) :
    if i%2 == 0 :
        sumen = sumen + i
print(sumen)



# 1에서 부터 10까지의 곱을 구해보세요.
mtp = 1

for i in range(1, 11, 1) :
    mtp = mtp * i
print(mtp)


''' 선생님 답
# 1. 숫자 한개를 입력 받아서 1부터 입력한 수까지의 합을 구하세요.
n1 = 100
# for i in range(1,   ) :
#     합계
# 합계 출력

sn = 0 # 총합을 넣은 변수 선언
for i in range(1, n1+1) : 
    # print(i, end= " ")
    sn = sn + i # i = 1, i = 2, i = 3, ...
print("{}부터 {}까지의 총합은 {}입니다." .format(1, n1, sn))

n1 = int(input("숫자를 입력해주세요. >> "))

# 짝수의 합만 구함
# 짝수만 출력
s1 = 0 # 짝수의 합을 넣을 변수
for i in range(1, n1+1) :
    if i % 2 == 0: # 짝수일 때
    s1 = s1 + i # i = 2, i = 4, i = 6, ...
    # print(i, end=' ')
print("{}부터 {}까지의 짝수의 총합은 {}입니다." .format(1, n1, s1))

# 1 - 10까지의 곱

s2 = 1
for i in range(1, 11) :
    s2 = s2 * 1
    # i = 1 > 1*1 > 1
    # i = 2 > 1*2 > 2
    # i = 3 > 2*3 > 3
print(s2)
    

'''