'''
클래스 : 객체지향 언어 ==> 고급언어
그 전에는 절차지향 언어(assembly 언어)
'''
print(100+10)
print(200+10)
print(300+10)
print(400+10)
print(500+10)
print(600+10)
print(700+10)
print(800+10)
print(900+10)
print(100+10)

# 변수 등장

a = 120
b = 1
print(a+10)
print(a+10)
print(a+10)
print(a+10)
print(a+10)
print(a+10)
print(a+10)
print(a+10)
print(a+10)
print(a+10)

# 리스트 등장
a = [1,2,4,120]
b = 1
print(a[0]+10)
print(a[1]+10)
print(a[2]+10)
print(a[3]+10)



# 클래스 등장; 클래스는 변수도 함수도 다 넣을 수 있어. 최근에는 안 써. 콜백함수
# 동등한 변수에 있는 묶음 처리. 세부적으로 조정 가능 이점이 있어. 
# 클레스를 '사용자 정의 변수'라고도 함. 클래스를 사용하면 프로그램 난이도 올라감

'''
클래스 : 사용자 정의 변수, 함수도 포함.
클래스는 반드시 첫글자 대문자 사용. 대문자 사용하지 않는다고 에러가 발생하지는 않음.
클래스는 설계도라고 생각하면 돼.
일일이 변수를 선언할 필요 없음.
# 클래스 선언 방법
Class 이름 :
    변수들 작성
'''

class Car : # 클래스 선언
    color = "white"
    door = 5
    length = 4710
    width = 1800
    displace = 1600
    speed = 0
    
    def upSpeed(self, sp) :
        self.speed += sp
        
    def downSpeed(self, sp) :
        self.speed -= sp

# 객체선언을 할 때마다 제품(Car)이 한개씩 생산
c1 = Car() # 객체선언
print("색상 :", c1.color)
c1.color = "red"
print("변경 후 색상 :", c1.color)

c2 = Car()
print("색상 :", c2.color)    
    

c1 = Car() # 클래스 객체선언, Car 클래스에 있는 모든 변수를 사용함. 
print(c1.displace) # 출력 방법
c2 = Car()
print(c1.length)
c3 = Car()

a_l1 = 4710
a_l2 = 4710
a_l3 = 4710

a_w1 = 1800
a_w2 = 1800
a_w3 = 1800

a_d1 = 1600
a_d2 = 1600
a_d3 = 1600