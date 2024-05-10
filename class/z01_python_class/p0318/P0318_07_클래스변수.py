class Tv( ) :
    serial_no = 0 # 클래스 변수
    
    def __init__(self, color, name, size) : # 매개변수 생성자
        self.color = color 
        self.name = name
        self.size = size # 인스턴스 변수
        Tv.serial_no += 1 # 클래스 변수 : 모든 클래스에서 공통으로 사용하는 변수
        # class명.변수명 ==> 클래수 변수
        # 아래의 c1, c2, c3 모두 영향을 주는 변수
        
    def tv_print(self) : # 인스턴스 함수
        print(f"tv :{self.serial_no}, {self.color}, {self.name}, {self.size}")
        
        
c1 = Tv("white", "스마트 TV", 100)
c1.tv_print()

# Tv.serial_no = 100 # 아래 c2, c3부터 101, 102로 바껴. 다른 클래스에 영향을 줘.

c2 = Tv("black", "FHDTV", 70)
# c2.serial_no = 2
c2.tv_print()

c3 = Tv("silver", "OLEDTV", 82)
# c3.serial_no = 3
c3.tv_print()