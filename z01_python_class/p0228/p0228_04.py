
# 해보세요.

# 1~100까지의 합을 구하세요.

sum = 0
for i in range(101) : # ********** range(100)은 0~99이므로 range(101) 또는 range(1, 101)이 맞아! **********
    sum = sum + i
print(sum)

'''선생님 풀이
sum0 = 0
sum0 = sum0 + 1
sum1 = sum1 + 2
sum2 = sum2 + 3 

sum3 = 0
for i in range(1, 4, 1,) : # i = 1, 2, 3
    sum3 = sum3 + i

print(sum1, sum2, sum3)

# 1~100까지의 합을 구하세요.
s1, s2, s3 = 0, 0, 0

'''

# 1~100까지 짝수의 합을 구하세요. if절을 사용
sum1 = 0
for i in range(0, 101, 2) : 
    sum1 = sum1 + i
print(sum1)

# if 절 사용
s1 = 0
for i in range(101) :
    if i % 2 == 0 :
        s1 = s1 + i
print(s1)

# 1~100까지 홀수의 합을 구하세요. if절을 사용
sum2 = 0
for i in range(1, 101, 2) :
    sum2 = sum2 + i
print(sum2)

# if절 사용
s2 = 0
for i in range(101) : 
    if i % 2 == 1 :
        s2 = s2 + i
print(s2)


''' 선생님 풀이
s1, s2, s3 = 0, 0, 0
for i in range(1, 101) :
    s1 = s1 + i
    if i%2 == 0 : # 짝수
        s2 = s2 + i
    else : # 홀수
        s3 += i
        print(i, end=' ')
print('1-100까지의 합은 {}입니다.' .format(s1))
print('1-100까지의 짝수 합은 {}입니다.' .format(s2))
print('1-100까지의 홀수 합은 {}입니다.' .format(s3))
'''

# 1 - 10 합
sum3 = 0
for i in range(1, 11) :
    sum3 = sum3 + i
print(sum3)

num = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# num 리스트 안에 있는 값들의 합
s3 = 0
for i in num :
    s3 = s3 + i
print(s3)

''' 선생님 풀이
# 1 - 10 합
s = 0
for i in range(1, 11) :
    s += i
print("1 - 10 합: {}" .format(s))

# num 리스트 안에 있는 값들의 합
num = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

t = 0 

for n in num :
    # print(n)
    t += n
print('num 리스트의 합: {}' .format(t))

# range 사용할 경우
t1 = 0
for i in range(len(num)) :
    # print(num[i])
    t1 += num[i]
print("num 리스트의 합: {}" .format(t1))

'''