class Student :
    def __init__(self, name, total ):
        self.name = name
        self.total = total

    # def __str__(self) : # 클래스를 출력할 때 제일 먼저 호출
    #     return f"이름 : {self.name}, 총점 : {self.total}"
    
    def __del__(self) :
        return "클래스가 소멸될 때 실행"
    
    def __add__(self, s) :
        return self.total + s.total
    
    def __gt__(self, s) : # 크거나 같다라고 비교할 때
        # print(">= 클래스간 비교를 하면 이 함수가 호출이 됨.")
        return self.total > s.total
    
    def __eq__(self, s) :
        return self.name == s.name and self.total == s.total
                
# ---------------------------
# 객체 선언하면 클래스 생성

s1 = Student("홍길동", 100)
s2 = Student("유관순", 90)
s3 = Student("이순신", 95)
s4 = Student("홍길동", 100)

print(s1) # ==> 주소값 출력
          # str 추가 후에는 s1 출력
          # 클래스를 출력할 때 str 함수 호출 
          
s1 + s2 # ==> 더하기 요소가 될 때 add가 제일 먼저 호출 
print(s1+s2) # 클래스를 더하기 할 때, add 함수 호출 

s1 > s2 # 클래스는 비교 불가능(비교 기준이 없으므로)이지만 __gt__를 통해서 기준을 세워서 가능
        # 클래슨느 비교가 불가능한데, __gt__ 메소드를 생성하면 호출 
print(s1 > s2) # True

# a_list = [10,20,30,40]
# b_list = [2,3,4,5]
# print(a_list>b_list) # Fale

print(s1)
print(s4)
print(s1 == s4) # 비교 자체가 안돼. 주소값이 다르므로 항상 False가 나와
                # __eq__ 메소드 추가 후 ==> True
print("s1==s4 : ", s1==s4) # True
print("s1==s2 : ", s1==s2) # False