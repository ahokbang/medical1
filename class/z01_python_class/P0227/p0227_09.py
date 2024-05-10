print("2단 출력")
for i in range(1, 10) : # i = 1, 2, 3, 4, ..., 9
    print('2 * {} = {}' .format(i, 2*1))

for i in range(1, 10) : # i = 1, 2, 3, 4, ..., 9
    print('{} * {} = {}' .format(2, i, 2*1))
    
    
''' 해보세요. 
원하는 단을 입력 받아서 구구단을 입력하세요.
3을 입력 받으면 3단 출력
'''

n = int(input("원하는 단을 입력하세요. >> "))

for i in range(1, 10) : # i = 1, 2, 3, 4, ... , 9
    print("{} * {} = {}" .format(n, i, n*i))
    
''' 선생님 풀이
n = int(input("원하는 단을 입력하세요. >> "))

for i in range(1, 10) : # i = 1, 2, 3, 4, ..., 9
    print('{} * {} = {}' .format(n, i, n*1))
'''

print("-"*35)
# 5번 반복
# for문도 중첩할 수 있어. if문처럼
for i in range(5) :
    n = int(input("원하는 단을 입력하세요. >> "))
    for i in range(1, 10) :
        print("{} * {} = {}" .format(n, i, n*i))
        
''' 선생님 풀이
for _ in range(5) : # ********** for문 중첩할 때 i가 겹치면 안돼. i를 사용 안하니까 언더바로 바꾸어 줘. **********
    n = int(input("원하는 단을 입력하세요. >> "))
    for i in range(1, 10) :
        print("{} * {} = {}" .format(n, i, n*i))
        
현재에서는 첫번째 for문에서 i를 사용하지 않아서 문제 없지만, 추후에는 카운터 변수가 동일하면 안돼.
'''
