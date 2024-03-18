class Car:
    car_name = "" # <== 변수값 없이 초기화로 세팅해도 돼.
    color = ""
    door = 0
    length = 0
    width = 0
    speed = 0
    
    # 생성자
    def __init__(self,car_name="", color="", door=5,length=1000, width=1000, speed=0) : # 상단의 car_name과 init의 car_name,매개변수는 다른 변수
    # def __init__(self,c_n,c,d,l,w,s) <== 이렇게 써도 돼
        self.car_name = car_name
        self.color = color
        self.door = door
        self.length = length
        self.width = width
        self.speed = speed
    
    
    def up_speed(self, s): # class 내의 함수는 무조건 self라는 걸 넣어줘야 해.
        self.speed += s

'''
speed = 0 # class 안의 speed와는 다른 speed야.
def aaa_speed(a) :
    a_speed += a 
''' 
# 기본 생성자를 사용한 객체선언
c1 = Car()
c1.car_name = "드뉴아반떼"
c1.color = "white"
c1.door = 5
c1.length = 2000
c1.width = 1000
c4 = Car()
print("기본 성능 :", c4.car_name, c4.color, c4.door, c4.length, c4.width, c4.speed)

# 생성자를 사용한 객체(=인스턴스) 선언
c1 = Car('드뉴아반떼', "white", 5, 200, 1000, 60) # Car 뒤에 괄호에는 생성자를 넣게 되어 있어.
print("철수 차 성능 : ", c1.car_name, c1.color, c1.door, c1.length, c1.width, c1.speed)

c2 = Car("드뉴아반떼", "green", 5, 200, 1000, 100)
print("영희 차 성능 : ", c2.car_name, c2.color, c2.door, c2.length, c2.width, c2.speed)

c3 = Car("디올뉴그랜저", "white pear", 5, 2500, 1400, 150)
print("반장 차 성능 : ", c3.car_name, c3.color, c3.door, c3.length, c3.width, c3.speed)

# c1 = Car()
# c1.car_name = "드뉴아반떼"
# c1.color = "white"
# c1.door = 5
# c1.length = 2000
# c1.width = 1000
# c1.up_speed(60) # 기존 속도에 속도를 더해서 넣어. 현재 speed에서 60을 더해 줌.
# c1.up_speed(40) # 현재 speed는? ==> 100
# c1.up_speed(50) # 현재 speed는? ==> 150
# c1.speed = 50 # 현재 speed는? ==> 50
    
    
# 철수의 차를 1대 생산
# car_name = "드뉴아반떼"
# color = "white"
# door = 5
# length = 2000
# width = 1000
# speed = 0
    
# color = "red"
# speed = 60

# print("철수 차 성능 : ", color, door, length, width, speed)


# c2 = Car()
# c2.car_name = "드뉴아반떼"
# c2.color = "green"
# c2.door = 5
# c2.length = 2000
# c2.width = 1000
# c2.up_speed(60) # 기존 속도에 속도를 더해서 넣어. 현재 speed에서 60을 더해 줌.

# # 영희의 차를 1대 생산해서, 색상은 green, 나머지 동일, speed = 100 설정해서 출력하시오.
# car_name1 = "드뉴아반떼"
# color1 = "green"
# door1 = 5
# length1 = 2000
# width1 = 1000
# speed1 = 100

# print("영희 차 성능 : ", color1, door1, length1, width1, speed1)


# c3 = Car()
# c3.car_name = "디올뉴그랜저"
# c3.color = "whie pear"
# c3.door = 5
# c3.length = 2500
# c3.width = 1400
# c3.up_speed(150)

# # 반장 - 디올뉴그랜저, 화이트펄, 길이: 2500, 폭: 1400, speed = 150
# car_name2 = "디올뉴그랜저"
# color2 = "white pear"
# door2 = 5
# length2 = 2500
# width2 = 1400
# speed2 = 150

# print("반장 차 성능 : ", color2, door2, length2, width2, speed2)


# print("철수 차 성능 : ", c1.car_name, c1.color, c1.door, c1.length, c1.width, c1.speed)
# print("영희 차 성능 : ", c2.car_name, c2.color, c2.door, c2.length, c2.width, c2.speed)
# print("반장 차 성능 : ", c3.car_name, c3.color, c3.door, c3.length, c3.width, c3.speed)