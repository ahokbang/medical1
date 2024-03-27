# 리스트변수명 = [요소1, 요소2, ..., 요소n]
# 요소가 될 수 있는 타입 : bool, int, float, String, list

fruits = ["딸기", "사과", "배", "수박", "귤"]
# 귤을 출력
print(fruits[4])
print(fruits[-1])
print(fruits[len(fruits)-1])

# 리스트에 요소를 추가
fruits.append("포도")
print(fruits)
# 특정요소를 삭제
fruits.remove("딸기")
print(fruits)
# 리스트에서 3번째 삭제
del(fruits[3])
print(fruits)

if '한라봉' in fruits :
    print("있음")

# in list명
for f in fruits : 
    print(f)
    
# 
for i in range(len(fruits)) : # i = 0, 1, 2, ...
    print(fruits[i])

num = [[10, 20, 30], [100, 200, 300], [1, 2, 3]]

for n in num :
    print(n)

for n in num :
    for a in n :
        print(a)

print('-'*25)

for i in range(len(num)) :
    print(num[i])
    
for i in range(len(num)) :
    for j in range(len(num[i])) : # 리스트의 리스트요소의 길이가 다를 수 있으므로 두번째 for문에서도 len 필수!
        print(num[i][j])
    
# 리스트에 숫자 넣을 때 한줄로 표현하기
# - 기존 아래와 같은 방법으로 리스트에 요소를 추가했는데,
aa= []
for i in range(1,11) :
    aa.append((i))
print(aa)
# - 아래와 같이 한 줄로 표현할 수 있어.
a = [ i for i in range(1,11) ]
print(a)

a =[ 0 for _ in range(10) ] # 0을 10번 a에 넣을거야. 언더바에 i 넣어도 상관없어.
print(a)

a = [ [] for i in range(10) ] # 빈 리스트가 10개 채워져.
print(a)

a = [ i * j for i in range(1, 3) for j in range(1,3) ]
print(a)
 
a = [ i for i in range(100) if i%2 == 0 ]
print(a)
b = [ i for i in range(1,11) ]
print(b) # [ 1, 2, 3, 4, 5, 6, 7, 8, 9, 10 ]
c = [ i + 1 for i in b ]
print(c) 

# => [표현식 for 항목 in 리스트 if 조건문]

names = ['홍길동', '유관순', '이순신', '강감찬', '김구']
# 출력 
# 1. 홍길동 2. 유관순 3. 이순신 4. 강감찬 5. 김구

#for i in names :
    # print(i)
    #print("{}. {}" .format( ,i))

# 변수 1개 더 필요 ********** 못 풀었어, 다시 풀어보기 **********
for i in names :
    for j in range(len(names)) :
        print("{}. {}" .format(j, i))
        
''' 선생님 풀이
for i in range(len(names)) : # i = 0, 1, 2, 3, 4
    print("{}. {}} .format(i+1, names[i]))
    
다른 방법으로,
i = 0 # 변수 선언
for name in names :
    # print(name) # 이름이 하나 하나 출력 돼.
    i = i + 1 # i += 1
    print("{}.{}" .format(i, name))

'''
# enumerate 함수
# - index를 넣고 싶을 때 사용
for i, name in enumerate(names) : # index : 0부터 시작
    print('{}.{}' .format(i+1, name))
    
# 또는 
for i, name in enumerate(names, start = 1) : # index : 0부터 시작
    print('{}.{}' .format(i, name))

names = ['홍길동', '유관순', '이순신', '강감찬', '김구']
#            0        1        2         3        4
for i, name in enumerate(names) : # enumerate는 정확한 위치를 알려줘. 몇번방에 있는지
    print("{}는 {}번째에 있습니다." .format(name, i)) 
    
# 참고로 알아두기
for i, name in enumerate(names) :
    if '홍길동' in names :
        del(names[i])
