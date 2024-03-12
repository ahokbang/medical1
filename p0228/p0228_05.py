n1 = int(input("첫번째 숫자를 입력해주세요. >> "))
n2 = int(input("두번째 숫자를 입력해주세요. >> "))
sum = 0
# 1. n1부터 n2까지의 합 구하는데 
# # 2. n1, n2 비교해서 작은 수를 n1에 넣기

# a = 10
# b = 8
# a, b = b, a # a와 b의 숫자를 바꿔주는거야
# print('a',a)
# print('b', b)



# 1. 
for i in range(n1, n2+1, 1):
    sum += i
print(sum)


# 2. ********** n1, n2 값 비교하는거 먼저!!  **********
# for i in range(n1, n2+1, 1):
#     if n1 > n2 :
#         n1, n2 = n2, n1
#     sum += i
# print(sum)

if n1 > n2 :
    n1, n2 = n2, n1


for i in range(n1, n2+1) : # ********** for이 if 안에 안 들어가 **********
        sum += i
print(sum)


# 3. n1-n2까지의 홀수 값을 odd_list에 저장 
odd_list = [] 

for i in range(n1, n2+1, 1) :
    if i % 2 == 1:
        # print(i)
        odd_list.append(i)
print(odd_list)


''' 선생님 풀이
# 만약에 n1이 n2보다 크다면 둘의 값을 바꿔라.
if n1 > n2 : # n1, n2를 비교해서 n1이 작을경우
    n1, n2 = n2, n1 
    
#1. 
sum = 0
for i in range(1, 11): # 1부터 10까지의 합을 구할 때
    sum = sum + i
print(sum)
문제로 돌아가면, 
for i in range(n1, n2+1): # 1부터 10까지의 합을 구할 때
    sum = sum + i
print(sum)

# 2. 
for i in range(n1, n2+1) :
    sum = sum + i
print(sum)

# 3.
for i in range(n1, n2+1) :
    if i % 2 ==1 :
        # print(i)
        odd_list.append(i)
print(odd_list)
'''