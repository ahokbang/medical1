# 1. 변수선언
score = [[80, 90, 85], [70, 80, 90], [84, 92,80], [72, 81, 76]]
name = ['홍길동', '유관순', '이순신', '김구']
total = []
# 2. 코딩
# 2-1) 요소 하나하나 출력해보세요. 80 90 85 70 80 90 ...
for i in score :
    #print(i)
    for a in i :
        print(a)

print('-'*35)

# 또는

for i in range(len(score)) :
    # print(score[i])
    for j in range(len(score[i])) :
        print(score[i][j])

print('-'*35)

''' 선생님 풀이
for i in range(len(score)) : # i = 0, 1, 2, 3
    # print(i) 
    print(score[i]) # score의 요소들이 출력 [80, 90, 85], [...], ...
    for j in range(len(score[i])) : # j = 0, 1, 2
        print(score[i][j]) # 요소 하나하나가 출력 됨.
'''

# 2-2) 작은 요소의 합을 구해서 total 넣어주세요.

for i in range(len(score)):
    sum = 0 # ********** 위치 중요! **********
    for j in range(len(score[i])) :
        sum += score[i][j]
    total.append(sum)
        
''' 힌트
n = [10, 20, 30]
sum1 = 0
for i in range(len(n)) :
    sum1 += score[i]
total.append(sum1)
'''

''' 선생님 풀이
# s = 0 # ********** 위치 주의!!! **********
for i in rage(len(score)) :
    s = 0 # score의 요소(i)가 바뀔 때 마다 리셋되어야 되므로 해당 위치에 있어야 함!
    # i = 0, score[0][0] + score[0][1] + score[0][2] = s
    # i = 1, score[1][0] + score[1][1] + score[1][2] = s
    # i = 2, score[2][0] + score[2][1] + score[2][2] = s
    
    for j in ragne(len(score[i])) :
        s = s + score[i][j]
    total.append(s)
print(total)

t1 = 0
for a in score :
    print("리스트입니다.', a) # [80, 90, 85] [70, 80, 90]
        t1 = 0
        for b in a :
            print("요소입니다.', b)
            t1 = t1 + b
        total.append(t1)
    # print(t1)
    
'''

# 3. 출력
# 3-1) total = [255, 240, 256, 229]
print(total)
# 3-2) 250 미만 불합격 250 이상 합격 ex) 홍길동님 합격입니다 출력
for t in range(4) :
    if total[t] >= 250 :
        print("{}님 합격입니다." .format(name[t]))
    else :
        print("{}님 불합격입니다." .format(name[t]))

''' 선생님 풀이
for i in range(4) :
# for i in range(len(total)) :
# for i in range(len(name)) :
    if total[i] >= 250 :
        print("{}님 합격입니다." .format(name[i]))
    else :
        print("{}님 불합격입니다." .format(name[i]))
'''