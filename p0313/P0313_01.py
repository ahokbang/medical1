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

def cal(num1, num2, sum, sbt, mtp, dvd) :
    
    if c == "1" : 
        sum = num1 + num2
    elif c == "2" :
        sbt = num1 - num2
    elif c == "3" :
        mtp = num1 * num2
    elif c == "4" :
        dvd = num1 / num2
        
    return sum, sbt, mtp, dvd
    

# 두 수를 입력 받아 리턴 받은 다음, 출력하시오.
# input은 전역변수에서 받아야 함.
num1 = int(input("첫번째 숫자를 입력하세요. >> ")) 
num2 = int(input("두번째 숫자를 입력하세요. >> "))
print("1. + 2. - 3. * 4. / ")
c = input("원하는 사칙연산을 입력하세요. >> ")

sum, sbt, mtp, dvd = 0, 0, 0, 0 # 밖에 있어야 해

sum, sbt, mtp, dvd = cal(num1, num2, sum, sbt, mtp, dvd)

print("{} {} {} = {} 결과값 : " .format(num1, c, num2), sum)
