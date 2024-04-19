''' 
1 - 100까지 더하는데, 총 합이 100이 넘었을 때 총합과, 그 수를 출력하세요.
1 + 2 + ... 

예) 1 - 10까지 더하는데 총합이 4가 넘는순간의 수를 출력
1 + 2 + 3 
총합: 6 그 수는 3

for 또는 while 사용
'''
# 1) for
sum = 0
for i in range(1, 101) :
    sum += i
    if sum > 100 :
        break
print("for : 총합:", sum,"그 수:", i)

# 2) while : ********** 익숙하지 않아. 다시 해보기 **********
i = 0
sum = 0
while i < 101 :
    i += 1
    sum += i
    if sum > 100 :
        break
print("while : 총합:", sum,"그 수:", i)

''' 선생님 풀이
1) for
sum = 0
for i in range(1, 101) :
    sum += i
    if sum > 100 :
        break

print('수 : ', i)    
print('총합 : ', sum)

2) while
total = 0
i = 1

while i <= 100 :
    total += i
    if total > 100 :
        break
    i += 1 # ********** 위치? **********
print(i)
print(total)
'''

