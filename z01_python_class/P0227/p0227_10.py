num = []
# for 문을 사용해서 1 ~ 10까지의 숫자를 채우세요.
print(num) # [1,2,3,4,5,6,7,8,9,10]

for i in range(1,11) :
    num.append(i)
print(num)

'''선생님 풀이
for i in range(1,11) :
    # print(i)
    num.append(i)
print(num) # [1,2,3,4,5,6,7,8,9,10]

# 더 단순하게 작성 가능; 한 줄로 표현 가능
num1 = [i for i in range(1,11)]
print(num1)

'''

print()

num2 = []
# 1 ~ 10까지 짝수를 num2 리스트에 넣으세요.
print(num2) # [2,4,6,8,10]

for j in range(0,11,2) : 
    num2.append(j)
print(num2)


'''선생님 풀이
for i in range(1,11) :
    if i % 2 == 0 :
    num2.appned(i)
    # print(i)
print(num2) # [2,4,6,8,10]
'''

# 1 ~ 10까지의 합을 for문을 사용해서 구할 수 있음.
# num 리스트를 사용해서 1 ~ 10까지의 합을 구해보세요.
# num 리스트 내의 숫자들의 합을 구하세요.
# num2 리스트 내 숫자들의 합을 구하세요. 

# num 리스트를 사용해서 1 ~ 10까지의 합을 구해보세요.
sum = 0
for i in range(len(num)) :
    sum = sum + num[i]
# print(num)
print(sum)

''' 선생님 풀이
1. 첫번째 방법
s1 = 0 # 최종 더하기에 사용될 변수
for n in num :
    # print(n, end= ' ') # 요소 하나하나를 가져와서 1~10까지 출력
    s1 += n 
print(s1)
print()
2. 두번째 방법 
s2 = 0 # 최종 더하기에 사용될 변수
for i in range(len(num)) :
    s2 = s2 + num[i]
    print(num[i], end = ' ')
print(s2)
    
'''

# num2 리스트 내 숫자들의 합을 구하세요.
sum1 = 0
for i in range(len(num2)) : 
    sum1 = sum1 + num2[i]
# print(num2)
print(sum1)

''' 선생님 풀이
s3 = 0 # 최종 더하기에 사용될 변수
for n in num2 :
    s3 = s3 + n
    # print(n, end=' ')
s4 = 0 # 최종 더하기에 사용될 변수
for i in range(len(num2)) : 
    s4 = s4 + num2[i]
    
print(s3, s4)

'''