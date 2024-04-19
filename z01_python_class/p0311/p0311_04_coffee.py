''' 교안(ppt)
함수: 무엇을 넣으면 어떤 것을 돌려주는 요술 상자
메서드와 차이점 : 함수는 외부에 별도 존재, 메서드는 클래스 안에 존재
함수의 형식 
- 함수명()
print() 함수
'''
a = 1 # 변수, 소문자로 시작되면 변수
print() # 이름 뒤에 () 있으면 함수, 소문자로 시작하고 괄호가 있으면 함수
# Cl # 클래스, 대문자로 되어 있으면 대부분 클래스

coffee = 0

# 함수 정의
# -이름 앞에 def 넣고 이름()
def machine(coffee) : 
        # 주문들어오면 진행
    print("1. 뜨거운 물을 준비한다.")
    print("2. 종이컵을 준비한다.")

    if coffee == 1 :
        print("3. 보통커피를 탄다.")
        
    elif coffee == 2 :
        print("3. 설탕커피를 탄다.")

    elif coffee == 3 :
        print("3. 블랙커피를 탄다.")

    print("4. 물을 넣는다.")
    print("5. 스푼으로 젓는다.")
    print()
    print("손님에게 가져다 준다.")
    print()
    
while True: 

    print("1. 보통커피")
    print("2. 설탕커피")
    print("3. 블랙커피 ")
    coffee = int(input("어떤 커피를 드릴까요? >> "))
    print()
    # 함수 사용(= 함수 호출)
    # - 이름(보내고 싶은 내용)
    machine(coffee)