
# 변수
a = False # bool
b = 123 # 정수
c = 1.3456 # 실수
d = '문자' # 문자열
e = [1, 2, 3] #리스트

# 출력
print("안녕하세요.")
print(123*456)
str1 = "반갑습니다."
print(str1) # 변수를 통한 출력
print("{0:s} : {1:d} / {2:d} = {3:f}" .format('수식', 7,3,7/3))
print("{} : {} / {} = {}" .format('수식', 7, 3, 7/3))

# 관계연산자 : 조건문이나 반복문에서 사용
# > : 크다. >= : 크거나 같다.
# < : 작다. <= : 작거나 같다
# == : 같다. != : 같지 않다.
print(3 > 5) # 결과가 거짓 : [False]로 출력
n1 = 10
n2 = 8
print(n1 != n2) # n1과 n2는 다르므로 # True
print(3 < n1 < 100) # True

# if n1 < 10

# 논리연산자 : and or not
a , b = 10, 9
print('and연산자') # 둘 다 참이어야 참이다. 
if a == 10 and b == 9 :
    print("참 and 참 = 참")
else :
    print("참 and 참 = 거짓")
    
if a == 10 and b != 9 :
    print("참 and 거짓 = 참")
else :
    print("참 and 거짓 = 거짓")

if a != 10 and b == 9 :
    print("거짓 and 참 = 참")
else :
    print("거짓 and 참 = 거짓")

if a != 10 and b != 0 :
    print("거짓 and 거짓 = 참")
else :
    print("거짓 and 거짓 = 거짓")

print('or 연산자') # 둘 중 하나라도 참이면 참이다. 
if a == 10 and b == 9 :
    print("참 or 참 = 참")
else :
    print("참 or 거짓 = 참")
    
if a == 10 and b != 9 :
    print("거짓 or 참 = 참")
else :
    print("거짓 or 거짓 = 거짓")

print("not 연산자") # 참 -> 거짓, 거짓 -> 참
if not a == 10 :
    print("not 참 = 참")
else :
    print("not 참 = 거짓")

if not a != 10:
    print('not 거짓 = 참')
else :
    print('not 거짓 = 거짓')
    
# 조건문 if
# if 조건문1:
#    실행문1
# elif 조건문2:
#      실행문2
# else:
#     실행문3
# 조건문1이 참이면 실행문1을 실행 후 종료
# elif가 있으면,
# 즉 조건문1이 거짓이고 조건문2가 참이면 실행문2 실행 후 종료
# 조건문1, 2가 거짓이면 실행문3 실행 후 종료

num = 5
# 숫자가 0 이상이면 양수를 출력하시오.
if num > 0:
    print('양수입니다.')
# 숫자가 0 이상이면 양수를 출력하고, 0 이하이면 음수를 출력하시오.
if num > 0:
    print("양수입니다.")
else:
    print("음수입니다.")
# 0이면 0, 양수면 양수, 음수면 음수를 출력하시오.
if num > 0:
    print("양수입니다.")
elif num == 0 :
    print("0입니다.")
else :
    print("음수입니다.")

# 실행문을 비우고 싶을 때: pass
'''
if 조건문1 :
    실행문 # 실행문을 아무것도 쓸 수 없을 때 pass 넣어줄 수 있어.
else :
    실행문
'''
if 1 == 1 :
    pass
else :
    print("else문 실행")

print("-"*25)

# 중첩 if문: if문 안에 if문 사용
if num >= 0 :
    if num == 0 :
        print("0입니다.")
    else :
        print("양수입니다.")
else :
    print("음수입니다.")
    
