class Car:
    count = 0
    
    def __init__(self, color='red', door=5, tire=4, speed=0) :
        self.color = color
        self.door = door
        self.tire = tire
        self.speed = speed
        
    def up_speed(self) :
        self.speed += 10
    
    def down_speed(self) :
        self.speed -= 10  
        
    # 추후 break 기능 추가
    def stop_speed(self) :
        self.speed -= 10
        
        
# Car 클래스 상속: Car 클래스의 모든 것을 가져옴.
class Ambul_car(Car) :   
    # count = 0
    
    # def __init__(self, color='white', door=5, tire=4, speed=0) :
    #     self.color = color
    #     self.door = door
    #     self.tire = tire
    #     self.speed = speed
        
    # def up_speed(self) :
    #     self.speed += 10
    
    # def down_speed(self) :
    #     self.speed -= 10     
    # color = 'white'
    # def __init__(self, color) :
    #     self.color = color 
    
    def up_speed(self) : # 새로운 정의(재정의) ==> 함수의 오버라이딩, 자식 클래스에서 오버라이딩 된 함수
        self.speed += 20
        # return super().up_speed()
    
    def up_speed2(self) : # 기존 부모의 함수를 다시 호출하고 싶을 때
        return super().up_speed() # 부모의 요소를 가져올 때 super()
                
    def siren(self) :
        print("사이렌이 울리는 기능이 추가 됩니다.")
        
# Car 클래스 상속
class FireTruck_car(Car) :
    # count = 0
    
    # def __init__(self, color='white', door=5, tire=4, speed=0) :
    #     self.color = color
    #     self.door = door
    #     self.tire = tire
    #     self.speed = speed
        
    # def up_speed(self) :
    #     self.speed += 10
    
    # def down_speed(self) :
    #     self.speed -= 10  
            
    def water(self) :
        print("물을 뿌리는 기능이 추가 됩니다.")
        
# 중복되는 부분을 부모로 만들고, 중복되는 부분을 상속 받아서 사용 

a1 = Ambul_car()
print("현재속도 : ", a1.speed) # 0
a1.up_speed() # 자식의 오버라이딩 된 함수를 호출
print("현재속도 : ", a1.speed) # 10
a1.up_speed2() # 부모의 함수를 호출해서 사용
print("현재속도 : ", a1.speed) # 

a1.stop_speed()
print("현재속도 : ", a1.speed) # 0
print("앰뷸런스 색상 : ", a1.color) 