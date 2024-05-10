# 오늘부터 파일저장 시 첫글자 대문자로!!

# 함수: 
# - 파일(코드)의 관리 및 반복적인 코드의 재사용을 위해 사용
# - 함수 선언 : def 이름() 정의
# - 함수값은 return
# - 함수호출 : 이름()
# - 매개변수 : 함수로 데이터 전달하는 변수, 매개변수 개수 항상 같아야 한다.
# - 가변매개변수선언 : *values,  가변매개변수는 일치하지 않아도 된다.
# - 리스트, 딕셔너리 매개변수는 주소값이 전달된다. 

# 퀴즈 1. 
# 함수를 사용하여 두 수를 입력받아 더하기, 빼기, 곱하기, 나누기 결과값을 출력하시오.

def cal(num1, num2) : 
    r_list = [0]*6
    r_list[0] = num1
    r_list[1] = num2
    r_list[2] = num1 + num2
    r_list[3] = num1 - num2
    r_list[4] = num1 * num2
    r_list[5] = num1 / num2
       
    return r_list
 
save_list = [] 
 
 
# 무한반복 하고 싶어,
while True : 
# 두 수를 입력 받아 리턴 받은 다음, 출력하시오.
# input은 전역변수에서 받아야 함.
    num1 = int(input("첫번째 숫자를 입력하세요. 0. 종료 >> ")) 
    if num1 == 0 :
        break
    
    num2 = int(input("두번째 숫자를 입력하세요. >> "))
    print("1. + 2. - 3. * 4. / ")
    c = input("원하는 사칙연산을 입력하세요. >> ")

    # 함수호출
    r_list = cal(num1, num2)
    # save_list에 r_list 저장, for문 사용
    save_list.append(r_list)
    
    # list일 경우 *list = list[0], list[1], list[2], list[3]
    print("{}, {} 결과값 : {},{},{},{}" .format(*r_list))

print("[ 현재까지 입력한 숫자, 결과값 ]")
# 프로그램 종료 시 현재까지 입력한 숫자와 결과값을 모두 출력해보세요.
for s in save_list :   # ********** for문 못 풀었어. 숙지하기 **********
    print("{}, {} 결과값 : {},{},{},{}" .format(*s))
    
# print(save_list)
# 10, 20 결과값 : 30, -10, 200, 0.5