'''
0 ~ 20 사이의 5의 배수로 이루어진 리스트를 만들어 보세요. 
출력: [0, 5, 10, 15, 20]
for, append 사용
'''
num = []
for i in range(0, 21, 5) :
    num.append(i)
print(num)

''' 선생님 답
for i in range(21) :
    print(i) # 0~20 출력
    if i % 5 == 0 :
        # print(i) # i = 0, 5, 10, 15, 20
        # append 함수를 가지고 리스트 
        num.append(i)
print(num)
'''
print()


'''
for문을 사용해서 다음을 출력 해보세요. 
1. for 사용해서 하나하나 출력해보기.
    1) in 리스트명
    2) in range() 사용
2. 카운터변수 i 사용해서 
   1.c
   2. python
   3. java
   4. jquery
   5. css
   이렇게 출력해보기
'''

lan = ['c', 'python', 'java', 'jquery','css']

# 1-1) ********** 다시 풀어보기 **********
for i in lan :
    print(i)

print()

# 1-2) ********** 다시 풀어보기 **********
for i in range(len(lan)) : # len(lan) 대신 실제 해당값인 5를 넣어도 돼.
    print(lan[i])
'''
선생님 답
for i in range(len(lan)) : # for i in range(5) : 를 출력하면 i = 0, 1, 2, 3, 4
    print(lan[i]) 
'''
print()
    
# 2.
for i in range(len(lan)) : 
    print(i+1,".",lan[i]) # ********** i는 0부터니까 i+1 **********
    
''' 
선생님 답
for i in range(5): # i = 0, 1, 2, 3, 4
    # print(i)
    # print(lan[i])
    print("{}.{}" .format(i+1, lan[i]))
    
또는

for i in range(1,6,1): # i = 0, 1, 2, 3, 4
    print("{}.{}" .format(i+1, lan[i-1]))  # ********** i - 1 이해 안가 **********
'''
print()

'''
양수면 양수, 음수면 음수
1: 양수
-1: 음수
2: 양수
...

'''
num = [1, -1, 2, 3, -4, 5, 6, -8, 9, -10]

# for in list
for i in num :
    if num[i] > 0 :
        print("{} : {}" .format(num[i], "양수"))
    elif num[i] < 0 :
        print("{} : {}" .format(num[i], "음수"))

print()

# for in range()
for i in range(len(num)) :
    # print(num[i])
    if (num[i]) > 0 : # ********** num[i]에 괄호 중요!! **********
        print("{} : {}" .format(num[i], "양수"))
    elif (num[i]) < 0 :
        print("{} : {}" .format(num[i], "음수"))
    
'''
선생님 답

for n in num:
    print(n, end=' : ')
    if n >= 0 :
        print("양수")
    else :
        print("음수)
        
for n in num:
    if n >= 0 :
        print('{} : 양수' .format(n))
    else :
        print('{} : 음수' .format(n))
        
# range 사용
for i in range(len(num)) : # i : 0,1, 2, 3, ...
    print(i)  # 0~9까지 출력
    if num[i] >= 0 : # num에 있는 i 값에 접근해야 해
        print('{} : 양수' .format(num[i]))
    else "
        print('{} : 음수' .format(num[i]))  
'''