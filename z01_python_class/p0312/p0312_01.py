# 두 수를 입력 받아, 두 수 사이의 합계를 구하시오.

# 1. 두 수 입력
# 2. 함수 호출
# 3. 1, 10 ==> 1+2+3+4+...+10
# 4. 합계를 리턴 받아서 
# 5. 합계 : 55 출력


# n1 = int(input("첫번째 숫자를 입력하세요. >> "))
# n2 = int(input("두번째 숫자를 입력하세요. >> "))

# def cal(n1, n2) :
#     sum = 0 # for문 안에 있으면 안돼! # 지역변수
#     if n1 > n2 :
#         n1, n2 = n2 , n1
        
#     for i in range(n1, n2+1) :    
#         sum += i
    
#     return sum

# sum = cal(n1, n2) # 전역변수
# # 지역변수의 sum과 전역변수의 sum은 다른 sum. 같지 않아. 이름만 같아.
# print("합계 : ", sum)



# # sum도 넘겨주고 싶어. cal(n1, n2, sum) 이렇게
# def cal(s_list) :
#     for i in range(s_list[0], s_list[1]+1) :
#         s_list[2] += i
        
# sum = 0
# n1 = int(input("첫번째 숫자를 입력하세요. >> "))
# n2 = int(input("두번째 숫자를 입력하세요. >> "))
# s_list = [n1, n2, sum]
# cal(s_list)
# print("s_list : ", s_list)

# 1, 10 ==> 1-10까지의 더하기, 빼기, 곱하기의 결과값을 출력하시오.

def cal(s_list) :
    # 더하기
    for i in range(s_list[0], s_list[1]+1) :
        s_list[2] += i
    
    # 빼기
    for i in range(s_list[0], s_list[1]+1) :
        s_list[3] -= i
    
    # 곱하기
    for i in range(s_list[0], s_list[1]+1) :
        s_list[4] *= i  
        
sum = 0
sbt = 0
mtp = 1 # 곱하기는 0이 아닌 1로!! 

n1 = int(input("첫번째 숫자를 입력하세요. >> "))
n2 = int(input("두번째 숫자를 입력하세요. >> "))

# 함수호출
s_list = [n1, n2, sum, sbt, mtp]
cal(s_list)

print("더하기 결과값 : ", s_list[2])
print("빼기 결과값 : ", s_list[3])
print("곱하기 결과값 : ", s_list[4])

''' 선생님 풀이
def cal(s_list) :
    # 더하기
    for i in range(s_list[0], s_list[1]+1) :
        s_list[2] += i  
    # 빼기
        s_list[3] -= i  # 0-1-2 = -3
    # 곱하기
        s_list[4] *= i  
        
n1 = int(input("첫번째 숫자를 입력하세요. >> "))
n2 = int(input("두번째 숫자를 입력하세요. >> "))

# 함수호출
s_list = [n1, n2, 0, 0, 1]   <== 변수 선언 안하고 이렇게 해도 돼!
cal(s_list)

print("더하기 결과값 : ", s_list[2])
print("빼기 결과값 : ", s_list[3])
print("곱하기 결과값 : ", s_list[4])
'''

'''
파이썬 언어는 인터프리터 언어, 컴파일러 언어; 프로그램을 실행시킬 때 2가지 방식이 있어. 
- 컴파일러 : 전체 소스 코드를 한번에 기계어(0, 1)로 변환. 속도면에서 더 빠름. C, C++, 자바 등 
            실행파일 생성 ==> 기계어로 나와서 비교적 보안에 좋음. 안전적. 그래서 보안프로그램은 다 자바: 정부, 금융 프로그램
            컴파일과 실행단계 분리 ==> 실행 시 코드 실행 속도 빠름
- 인터프리터 : 한줄씩 기계어로 변환, 속도는 비교적 느리지만 편함. 파이썬, 자바스크립스 등
              ==> 그래서 파이썬에서는 함수의 위치 중요, 자바에서는 함수 위치 상관없음. 
              실행파일 생성x ==> 소스 그대로 노출되어 비교적 보안에 취약
              인터프리트 단계와 실행단계 분리되지 않아 반복 수행하므로 실행 속도 느림
'''