# Car 클래서를 선언해서 
# carCount 클래스 변수
# carNo dpsms carCount 숫자를 이용해서 carNo를 넣으시오.
# 클래스 변수를 이용해서 숫자를 증가시켜 보세요.
# 변수선언 : carNo, color="white", door=5, tire = 4, speed
# up_speed 함수를 호출하면 10씩 증가
# down_speed 함수를 호출하면 10씩 감소
# c1 => 1, white, 5,4,0 -> speed 30
# c2 => 2, red, 5, 4, 0 -> speed 100
# c3 => 3, silver, 5, 4, 0 -> speed 70
# car_list 추가하고 car_list에 있는 모든 객체의 모든 color, door, tire, speed 모두 출력하시오.

class Car() :
    carCounter = 0
    carNo = 0
    color = "white"
    door = 5
    tire = 4
    speed = 0
    
    def __init__(self, color="", door=0, tire=0, speed=0) :
        self.color = color
        self.door = door
        self.tire = tire
        self.speed = speed
        Car.carCounter += 1
        self.carNo += Car.carCounter
    
    def up_speed(self, s):
        self.speed += s
        
    def down_speed(self, s):
        self.speed -= s
        
    def c_print(self) :
        print(f"{self.carNo}, {self.color}, {self.door}, {self.tire}, {self.speed}")
        
    def __str__(self) :
        return f"{self.carNo}, {self.color}, {self.door}, {self.tire}, {self.speed}"
        

car_list = []
        
c1 = Car("white", 5,4,0)
for i in range(3) :
    c1.up_speed(10)
car_list.append(c1)


c2 = Car("red", 5,4,0)
for i in range(10) :
    c2.up_speed(10)
car_list.append(c2)


c3 = Car("silver", 5, 4, 0)
for i in range(7) :
    c3.up_speed(10)
car_list.append(c3)



for i in range(len(car_list)) : 
    print(car_list[i].carNo, car_list[i].color, car_list[i].door, car_list[i].tire, car_list[i].speed)

for i in range(3) :
    print(car_list[i])
    
