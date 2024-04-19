# 문제
# 1. 1 ~ 5까지의 합계를 구하세요.
sum = 1 + 2 + 3 + 4 + 5
# 위의 방법 말고,
total = 0         # total = 0
total = total + 1 # total = 1
total = total + 2 # total = 1 + 2
total = total + 3 # total = 1 + 2 + 3
total = total + 4 # total = 1 + 2 + 3 + 4
total = total + 5 # total = 1 + 2 + 3 + 4 + 5

# " 순차적으로 증가하고 ~  "=> for문으로 나타낼 수 있어.

print(total)
t = 0
for i in range(1, 6, 1) : # i = 1, 2, 3, 4, 5
    t = t + i # t += 1
    
# for문을 사용해서 1에서 10까지의 합을 구해보세요.

t = 0
for i in range(1, 11, 1) :
    t += i
print(t)

''' 선생님 답
sum10 = 0
for i in range(1, 11) :
    sum10 += i  # sum10 = sum10 + 1 # 1, 2, 3, 4, 5, 6, 7, 8, 9, 10
    print(i)
print("1부터 10까지의 합은 : {}입니다." .format(sum10))
'''
# for문을 사용해서 1에서 100까지의 합을 구해보세요.

a = 0
for i in range(1, 101, 1) :
    a += i
print(a)

'''선생님 답
sum100 = 0 # 변수 초기화
for i in range (1, 101) :
    sum100 += i
print("1부터 100까지의 합은 : {}입니다." .format(sum100))
'''

# 입력한 수(n1)부터 입력한 수(n2)까지의 합을 구해보세요.

n1 = int(input("첫번째 숫자를 입력하세요. >> "))
n2 = int(input("두번째 숫자를 입력하세요. >> "))

sum = 0

if n2 > n1 : 
    for i in range((n1), (n2+1)) : 
        sum = sum + i
    print(sum)
elif n1 < n2 :
    for i in range((n2), (n1+1)) :
        sum = sum + i
    print(sum)
else :
    print(n1*2)
    
''' 선생님 답 : ********** 이거 설명 해주셨나? **********
n1 = int(input("첫번째 숫자")) # 1
n2 = int(input("두번재 숫자")) # 10

# n1부터 n2까지의 합을 구해보세요.
sum1 = 0
for i in range(n1, n2+1) # range(1, 11)
    sum1 = sum1 + i # 1, 2, 3, 4, 5, 6, 7, 8, 9, 10
    # i = 1 sum1 = 0 + 1
    # i = 2 sum1 = (0 + 1) + 2
    # i = 3 sum1 = (0 + 1 + 2) + 3
    
# s  = (((((0)+1)+2)+3)+4)+5)

'''


