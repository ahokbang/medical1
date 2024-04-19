class Student :
    name = ""
    kor = 0
    
    # def __init__(self) : <== 이거 없어도 자동으로 만들어줘
    def __init__(self, name="") : # name 추가되면 error 왜냐하면 (1)에 name이 없어서. 
                               # 즉 매개변수를 맞춰주지 않아서 error 발생
        pass
    def stu_print(self) :
        print("학생성적을 출력합니다.")

class Lotto :
    pass

def s_print() :
    print("클래스 밖에 있는 함수")
    

s = Student() # (1) 객체선언할 때 무조건 init() 함수 호출
s2 = Lotto()

print(s) # 주소값 출력
# 꼭 변수에 안 선언해도 돼.
Student()
print(Student()) # 이렇게 써도 돼

s_print()
# stu_print() # error 객체선언을 하지 않았기 때문
s.stu_print() # 클래스 내 함수(메소드)는 꼭 객체선언을 해야 사용 가능
              # 참조변수명.메소드명()
              
if isinstance(s2,Student) :
    print("Student class 변수입니다.")
elif isinstance(s2, Lotto) :
    print("Lotto class 변수입니다.")
    
print(type(s2))