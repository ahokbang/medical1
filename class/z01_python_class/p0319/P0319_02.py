class Car:
    
    def __init__(self, color, door, tire, speed) :
        self.color = color
        self.door = door
        self.tire = tire
        self.__speed = speed # (1) 변수 앞 언더바 두개를 넣으면 (2)처럼 직접적으로 속도를 변경할 수 없어. 
                             # 접근제한(캡슐화) : __변수, 클래스 내부에서만 접근이 가능하게 만듬. 
    def up_speed(self, smartkey) :
        if smartkey == "0x1100" : # 스마트키가 있어야먄 속도 조절 가능하도록 설정
            self.__speed += 10
        else : 
            print("스마트키가 다릅니다.")
        
    def down_speed(self) :
        self.__speed -= 10
    
    def get_speed(self) : # speed 출력하기 위해 추가 
        return self.__speed
    
    def set_speed(self, speed) :
        self.__speed += speed
        
c1 = Car("white", 5, 4, 0) # speed 0
c1.up_speed("0x1100") # speed 10, 스마트키가 있어야먄 속도 조절 가능하도록 설정
c1.up_speed("0x1100") # speed 20
c1.up_speed("0x1111") # 속도 올릴 수 없어.
c1.speed = 300 # (2) 속도가 갑자기 0에서 300으로 올릴 수 없어. 그래서 생성자의 변수에서 언더바언더바하면 막을 수 있어.(1)참조
# print(c1.speed) # 출력도 안돼. 에러 발생 
c1.set_speed(500) # speed 520
print(c1.get_speed()) # 이렇게 speed 출력 가능.
                      # 클래스의 변수에 직접적으로 접근이 안됨. get을 통해서만 접근 가능 
                      # speed변경은 up/down_speed, 출력은 get_speed 
                      # 제한을 줄 수 있음.

# c2 = Car("red", 4, 4, 0)