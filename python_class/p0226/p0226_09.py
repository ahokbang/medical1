
numL = []

# 0에서부터 5가지 넣어보세요. append
print(numL)
numL.append(0)
numL.append(1)
numL.append(2)
numL.append(3)
numL.append(4)
numL.append(5)
print(numL)

# for 문을 사용하여 0 ~ 5까지 숫자 넣기
# [ 0, 1, 2, 3, 4, 5]
#   0, 1, 2, 3, 4, 5
# num[4]

num = []
for i in range(5) : # i는 0에서부터 6미만까지 1씩 증가
    num.append(i)
    
print('num[] = ', num)

aa = [1, 2, 3, 4,]
# index를 사용해서 값 읽기

for i in aa : # 리스트에 있는 것을 하나하나 가져와라. 
    print(i)

for i in range(0, 4) :
    print(aa[i])
    
f = ['사과', '복숭아', '딸기', '포도', '자몽']
for i in f :
    print(i)
for i in range(len(f)) : # 리스트의 길이 len 함수는 반복문에서 많이 사용
    print(f[i])

# 해보세요.     
c = ['미국', '영국', '호주', '캐나다', '일본', '중국']
# for 문을 사용해서 출력해보기. 2가지 방법으로 다 해보기
for i in c:
    print(i)
for i in range(0, 6):
    print(c[i])

''' 선생님 답
for i in c :
    print(i)
    
for i in range(len(c)) :
    print(c[i])
'''
# 1에서 100까지 들어가는 numL=[]를 만들고 출력해보기
numL = []
for i in range(1, 101, 1) :
    numL.append(i)
print(numL)

''' 선생님 답
numL = []
numL.append(1) ~ append(100)
for i in range(100):
    numL.append(i+1)
    # print(i+1, end='')  ; 출력 확인
print(numL)

for i in range(100) :
    print(numL[i])
'''

# 반복문 안에 if문 사용
for i in range(10) :
    # print(i) # 0 ~ 9까지 출력이 됨.
    if i == 9 :
        print('9입니다.')
        
    
lan = ['영어', '스페인어', '일본어', '중국어']
for i in lan :
    print(i)
    if i == '영어' :
        print("영어입니다.")
    else :
        print("다른 언어입니다.")
        

# 2의 배수만 출력 (1 ~ 100 사이)
# 1) 증감 사용
n = []
for i in range(2, 101, 2) :   # ********** 101이 아닌 102까지 써줘야 100이 포함돼! **********
    n.append(i)
print(n)

# 2) if 사용
n =[]
for i in range(2, 101, 1) :
    if i%2 == 0 :
        n.append(i)
print(n)

# 7의 배수만 출력 (1 ~ 100 사이)
# 1) 증감 사용
n = []
for i in range(7, 101, 7) :
    n.append(i)
print(n)

# 2) if 사용
n = []
for i in range(7, 101, 7) :
    if i%7 == 0:
        n.append(i)
print(n)

aa = [100, 90, 86, 79, 72, 52, 98, 94]
# 80점 이상만 합격 출력 > 합격이 5개 출력 


''' 내가 풀은 거 : ********** 못 풀었어. ***********
for i in aa :
    if aa[i] >= "80" :

답 :
for i in aa :
    print(i)
    if i >= 80:
        print("합격")
'''

''' 선생님 답
# 2의 배수만 출력 (1 ~ 100 사이)
1) 증감 사용
for i in range(2, 102, 2) :
    print(i, end='')
print() # 줄바굼
2) if 사용
for i in range (100):
    print(i, end=',') # 0 ~ 99까지 출력
    print(i+1, end= ',') # 0 ~ 100까지 출력
2의 배수이라는 조건이 있으므로
for i in range(100):
    if (i+1)%2 == 0 :
        print(i+1, end-'')
i+1 헷갈리면,
for i in range(1, 101) :
    if i%2 == 0 :
        print(i, end='') 
        
        
# 7의 배수만 출력 (1 ~ 100 사이)
1) 증감 사용
for i in range (7, 101, 7) :
    print(i, end='')

2) if 사용
for i in range(100) :
    if (i+1)%7 == 0 :
        print(i+1, end='')
        
i+1 헷살리면
for i in range(1,100):
    if i%7 == 0 :
        print(i, end='')
    
aa = [100, 90, 86, 79, 72, 52, 98, 94]
# 80점 이상만 합격 출력 > 합격이 5개 출력 
for a in aa :
    print (a)
    if a >= 80 :
        print("합격")
        
'''        
f = ['사과', '복숭아', '딸기', '포도', '자몽']
# 딸기가 있으면 딸기, 다른 과일은 다른 과일이라고 출력
for i in f :
    print(i)
    if i == "딸기" :
        print("딸기")
    else :
        print("다른 과일")

num = [1, 2, 5, 7, 9, 10, 23, 43]
# 짝수면 짝수, 홀수면 홀수를 출력
# for i in num:
for i in num :
    print(i)
    if i%2 =="0": 
        print("짝수")
    else :
        print("홀수")

# for i in range(len(num)): **********못 풀었어 **********
# for i in range(len(num)):
#     print(num)
#     if int(num[0:7])%2 == "0" :
#         print("짝수")
#     else:
#         print("홀수")
        
        
''' 선생님 답
# 딸기가 있으면 딸기, 다른 과일은 다른 과일이라고 출력
for i in f :
    if i == "딸기" :
        print("딸기입니다.")
    else :
        print("다른 과일 입니다.")
        
# 짝수면 짝수, 홀수면 홀수를 출력
1) for n in num:
for i in num :
    print(n) # 리스트 요소들이 출력
    if n % 2 == 0 :
        print(n, '짝수')
    else:
        print(n, '홀수')

# for i in range(len(num))
for i in range(len(num)): # range를 쓸 경우 0부터 1씩 증가
    print(i) i : 0, 1, 2, 3, ... 
    print(num[i]) # num[0], num[1], num[2], ...
    if num[i]%2 == 0 :
        print(num[i], "짝수")
    else: 
        print(num[i],'홀수')
'''