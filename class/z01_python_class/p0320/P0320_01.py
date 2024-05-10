class Car:
    count = 0 # (1) 클래스 변수로 인식; 물론 인스턴스 변수로도 쓸 수 있지만 다른 사람이 봤을 때 헷갈릴 수 있어.
    
    def __init__(self, color="black", speed=0) : # color, speed ===> color = "", speed=0 ; 이렇게 초기화 하는 것을 키워드 변수라고 한다.
        self.color = color # init 안에 변수 선언 ==> 인스턴스 변수
        self.speed = speed
        # 클래스 변수 선언
        # Car.count=0
        
# class 사용하기 위해서는 인스턴스 선언 : 하지않으면 절대 사용할 수 없어.
c1 = Car() # 인스턴스 선언
c1.color = "white"
print("c1.color : ", c1.color) # error : 인스턴스 선언에서 매개변수가 없어. 단 초기화를 시켜놓으면 괜찮아.
                               # init에 매개변수 초기화 시켜주면 white로 잘 나와.
print("c1.speed : ", c1.speed)
Car.count = 10 # 클래스변수
print("c1.count : ", c1.count) # 10 , count (1)이 10으로 바뀜. count(1)이 클래스변수로 바뀜
# print("c1.count : ", Car.count) # print(c1.count) 이렇게 쓰지마

c2 = Car()
c2.color = "red"
print("c2.color : ", c2.color) # red
print("c1.color : ", c1.color) # white

print("c2.count : ", c2.count) # 10, count (1)이 10으로 바뀌었으니까
Car.count = 200
print("c1.count : ", c1.count)
print("c2.count : ", c2.count)
# c2.count = 100
# print("c1.count: ", c1.count) # 10
# print("c2.count: ", c2.count) # 100
# #count를 클래스 변수로 쓰고 싶으면
# Car.count = 100
# # ==> count를 클래스 변수로 쓰고 싶으면 Car.count로 써야 해. 

c2.door = 4 # 선언이 돼. c1에는 door가 없어. => 설계한 class와 달라져. 자바나 c++에서는 선언이 안돼.
print("c2.door : ", c2.door) 

c2.count = 100 # 기존의 count(클래스 변수)를 지우고 새로운 c2.count(인스턴스 변수)를 다시 생성 
               # ==> 에러 확률이 높음. 이렇게 하지 않길 권고
print("c2.count : ", c2.count) # 100
print("c1.count : ", c1.count) # 200
c3 = Car()
print("c3.count : ", c3.count) # 200
