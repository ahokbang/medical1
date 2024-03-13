# n1단부터 n2단까지 출력하세요.
n1 = int(input("숫자입력"))
n2 = int(input("숫자입력"))

for i in range(n1, n2+1) :
    print("[{}단]" .format(i))
    for j in range(1, 10) : 
        print('{} * {} = {}' .format(i, j, i*j), end=' ')
    print()

print('-'*35)

# 크기 비교해서 n1 더 크면 n2, n1 바꾸기
# 출력 2, 4 : 2단부터 4단까지 출력

n1 = int(input("숫자입력"))
n2 = int(input("숫자입력"))

if n1 > n2 :
    n1, n2 = n2, n1
    
for i in range(n1, n2+1) :
    print("[{}단]" .format(i))
    for j in range(1, 10) : 
        print('{} * {} = {}' .format(i, j, i*j), end=' ')
    print()

print('-'*35)


# 선생님 풀이
# 크기 비교
if n1 > n2 :
    n1, n2 = n2, n1
# 출력 2, 4 : 2단부터 4단까지 출력
for i in range(n1, n2+1) : # 2단
    print("[{}단]" .format(i)) # * 1 ~ * 9
    for j in range(1, 10) : 
        print('{}*{}={}' .format(i, j, i*j), end='\t')
    print()

print('-'*35)

for i in range(1, 10) : # 1 - 9
    for j in range(2, 10) : # 단
        print("{}*{}={}" .format(j, i, i*j), end='\t')
    print()