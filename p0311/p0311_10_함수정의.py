# 함수선언 : def 이름()
# 함수호출 : 이름()
# 함수선언 매개변수 개수 : def 이름(매개변수) -> 이름(매개변수)
# 리턴 개수와는 상관이 없음.
# 즉, 리턴의 결과값을 받지 않아도 되지만, 리턴의 개수는 맞춰야 함. 
# 함수내의 변수는 지역변수여서 함수가 종료되면 사라짐.
# 함수내의 변경된 변수값을 전역변수에 반영하고 싶으면 return으로 돌려줘야 함.
# 함수내 global이라고 하면, 전액변수에 선언되어 있는 변수주소를 가져와서 return을 사용하지 않아도 됨.
# global은 참고용으로만 알고 웬만하면 사용하지 마. 프로그램의 변경된 내용 찾기 어려움. return 사용권장!!
# 매개변수 리스트, 딕셔너리를 사용할 경우 return 할 필요가 없음.


'''
def cal(v1, v2) :
    pass

cal(100) # 매개변수 2개(v1, v2)인데 1개면 에러
cal(100, 200, 300) # 매개변수 2개(v1, v2)인데 3개면 에러
'''

''' 
def cal(v1) :
    return 100

cal(100)  # 리턴을 안 받는 거 괜찮지만,
# num1, num2 = cal(100) # 변수의 개수는 맞춰야 해.vq 하나인데 nu,1, num2 두개는 안됨.
print(num1)
'''

def cal(v1) : # 지역변수
    sum = 500 # 지역변수
    v1 = 200  # 지역변수

v1 = 100
cal(v1)
print(v1) # 100

def cal(v1) :
    v1 = 200
    return v1

sum = 0    # 전역변수
ver1 = 100 # 전역변수
ver1 = cal(ver1)
print(ver1) # 200 # ********** 이해 잘 안돼 **********
print(sum) 

def cal(v1, sum) :
    sum = sum + 500
    v1 = 200
    return v1, sum

sum = 10
v1 = 100
cal(v1, sum)
print(v1)


def func1() :
    a = 100 # 지역변수
    print("func1 a = ", a)
    # 지역변수값을 전역변수에 적용시키는 방법 
    # 코드를 추가하시오.
    return a  # 지역변수 a의 100이

# 전역변수의 값을 호출 100
def func2() :
    print("func2 b = ", a+10) # a = 100
    
a = 20 # 전역변수

a = func1() # 100
func2()
print("결과값 : ", a) # 100



# 전역변수를 쓰고 싶다면
def func1() :
    global a # 전역변수를 가져옴. 리턴 필요 없음, 어디서 변수가 바꼈는지 확인이 안되서 잘 안씀.
    a = 100 # 지역변수
    print("func1 a = ", a)

# 전역변수의 값을 호출 100
def func2() :
    print("func2 b = ", a) # a = 100
    
a = 20 # 전역변수 <===== 함수에서 global a를 불러와서, 함수의 그 다음줄인 a=100의 100이 여기로 저장됨.

a = func1() # 100
func2()
print("결과값 : ", a) # 100


# 함수선언
def func1(a, a_list) :
    a = 100 # 지역변수
    a_list[0] = 100 # 지역변수
    a_list = [100, 200, 300] # 새로운 변수 선언으로 영향을 미치지 않아
    return a

a = 10 # 전역변수
a_list = [1,2,3]

# 함수호출
a = func1(a, a_list) # 2개 이상의 데이터를 저장하는 변수는 주소값을 저장함.

#데이터 출력
print(a)
print(a_list)