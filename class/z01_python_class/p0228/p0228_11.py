'''
주석 여러 줄 쓸 때
한 줄 주석: # 주석 쓰셔도 되고
ctr + /

tab : 들여쓰기
shift + tab : 들여쓰기 삭제
alt + shift + 방향키 : 커서 있는 문장 복사
'''

num = [100, 200, 300, 400]
# for문을 사용해서 하나씩 출력해보세요. 2가지 방법 다 쓰기
# in num
# in range(len(num))


# 1)
for i in num :
    print(i, end=' ') 
print()

''' 선생님 풀이
for i in num :
    print(i, end='\t')
print()
'''

# 2)
for i in range(len(num)) : # i = 0, 1, 2, 3
    print(num[i], end=' ') # num의 0번째 ~ 3번째를 출력
print()

numlist = [[1, 2], [3, 4], [5, 6]]
#         [num[0][0], num[0][1]], [num[1][0], num[1][1]], ..., ]
# 변수 in 리스트이름 
for n in numlist : # [1, 2], [3, 4], [5, 6]
    # print(n, end='\t')
    for a in n :
        print(a, end=' ')
    print()

# in range
for i in range(len(numlist)) : # for i in range(3)과 같음
    print(i) # i = 0, 1, 2
    print(numlist[i]) # 1, 2,\n 3, 4, \n 5, 6이 출력
    for j in range(len(numlist[i])) :
        print(numlist[i][j], end= ' ')
    print()


f = [['딸기', 100, 1000], ['수박', 100, 2000], ['사과', 100, 1200], ['귤', 100, 300]]
# 요소 한개 한개를 출력해보세요.

for i in f :
    # print(i)
    for j in i :
        print(j)

print('-'*35)

for i in range(len(f)) :
    # print(f[i])
    for j in range(len(f[i])) :
        print(f[i][j])

''' 선생님 풀이
# 과일이름만 출력
print(f[0][0], f[1][0], f[2][0], f[3][0])
for i in range(len(f)) :
    print(f[i][0])

for i in range(len(f)) : # i = 0, 1, 2, 3
    for j in range(len(f[i])) : # j = 0, 1, 2
        print(f[i][j], end=' ')
        # i = 0, j = 0, 1, 2 f[0][0] f[0][1] f[0][2]
        # i = 1, j = 0, 1, 2
        # i = 2, j = 0, 1, 2
    print()
    
'''
print('-'*35)

score = [90, 80, 70, 100, 95, 85, 100]
total = []
# 점수의 총합을 구하세요.
# 그 점수를 total 리스트에 넣어주세요. 
# print(total) # [620]

sum = 0

for i in range(len(score)) :
    # print(score[i])
    sum = sum + score[i]
total.append(sum)
print(total)
    
''' 선생님 풀이
# 점수의 총합을 구하세요.
sum = 0
for s in score :
    # print(s) # 점수 하나하나
    sum = sum + s
print(sum)

아니면
sum1 = 0
for i in ragne(len(score)) : # for i range(7) : 과 동일
    # print(i) # i = 0, 1, 2, 3, 4, 5, 6
    # print(score[i]) # 점수가 출력
    sum1 += score[i]
print(sum1)

# 그 점수를 total 리스트에 넣어주세요.
total.append(sum)
print(total) # [620]

'''