# 함수의 이름은 똑같을 수 없어.
# 자바 같은 경우 매개변수 개수에 따라 다른 함수 인정
# 파이썬의 경우 함수의 이름이 무조건 달라야 함. 
# 파이썬은 아래의 경우 error이지만 자바의 경우 에러 발생하지 않음
'''def aaa(num1) :
    print(num1)
    
def aaa(num1, num2) :
    print(num1, num2)     
    
aaa(1)
'''

''''
def func(num1) :
    print(num1)
    
def func2(num1, num2, num3) :
    print(num1, num2)
    
func(1)
fucn2(1,2) # error 매개변수 개수가 달라
'''

def func2(num1, num2, num3=3) : # 키워드 매개변수 : 값이 들어오지 않으면 default값으로 설정
    print(num1, num2, num3)
    
func2(1, 2)

def func3(num1=0, num2=10, num3=3) :
    print(num1,num2,num3)
    
func3(100)

