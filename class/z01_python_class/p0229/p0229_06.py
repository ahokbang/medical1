# contiue 예제
# 1 - 100 합계를 구하는데 3의 배수는 제외하고 더하기
# 1 - 100까지 출력, 3의 배수는 제외하고 출력
# [1 2 4 5 7 8 10 ... ]
# while of for 사용해서

# for
print("for")
sum = 0 
for i in range(1, 101) :
    if i % 3 == 0 :
        continue
    print("{}" .format(i), end=' ')
    sum = sum + i
print()
print('합계 : ', sum)

# while
print("while")
j = 0
sum1 = 0
while j <= 100 :
    j += 1
    if j % 3 == 0 :
        continue
        print(j, end=' ')
    sum += j
    


''' 선생님 풀이
# for
for i in range(1, 101) :
    if i % 3 == 0 :
        continue
    print(i, end=' ')
print ()

# while
i = 1
while i < 101 :
    if i % 3 == 0:
        i = i + 1
        continue 
    print(i, end = ' ')
    i = i + 1


# 3의 배수를 제외하고 더하기

sum = 0
for i in ragne(1, 101) :
    if i % 3 == 0 :
        continue
    print()
******** 추가 작성 필요 *********


i = 1
sum1 = 0
while i < 101:
    if i%3 == 0:
        i = i+1
        conrinue
    sum1 += i
    i = i + 1
print('1-100 3의 배수 제외한 합: {}" .format(sum1))
'''
    