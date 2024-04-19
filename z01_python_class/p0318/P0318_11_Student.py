class Student :
    stuCount = 0 # 클래스변수
    stuNo = 0 # 인스턴스변수
    # name = ""
    # kor = 0
    # eng = 0
    # math = 0
    # total = 0
    # avg = 0
    # rank = 0
    # init 해줘서 위에는 주석처리 가능
    
    # 생성자 : __init__
    # 클래스에 대해 객체선언을 하면 제일 먼저 호출되는 함수
    def __init__(self, name="", kor=0, eng=0, math=0) :
        self.name = name
        if kor > 100 :
            self.kor = 100
        else : 
            self.kor = kor
        self.kor = kor
        self.eng = eng
        self.math = math
        self.total = kor+eng+math
        self.avg = float("{:.2f}" .format(self.total/3))
        self.rank = 0
        Student.stuCount += 1 # 클래스변수 선언: 클래스.변수명
        self.stuNo = Student.stuCount
        
    def stu_print(self) :
        print(self.stuNo, self.name, self.kor, self.eng, self.math, self.total, self.avg, self.rank, sep='\t')
    
    # 객체를 print하면 __str__함수를 제일 먼저 호출함.
    def __str__(self) :
        return f"{self.stuNo}, {self.name}, {self.kor}, {self.eng}, {self.math}, {self.total}, {self.avg}, {self.rank}"



# # 홍길동 학생 성적 넣기
# s1 = Student("홍길동", 100, 100, 90) # 객체선언
# # s1 stuNo를 출력하시오. 
# print(s1.stuNo)
# s2 = Student()
# print(s2.stuNo)



# 매개변수가 있는 객체선언 
s1 = Student("홍길동", 100, 100, 90)
s2 = Student("유관순", 99, 99, 98)

print(s1) # __str__ 함수호출 없으면 주소값 출력
# print(s1.stu_print())
s2.stu_print()



# get : 데이터를 읽어오는 것, 예) def getName; 이름을 가져오는 것, def getSpeed; 속도를 가져오는 것
# set : 데이터를 저장하는 것, 예) def setName; 이름을 저장하는 것, def setSpeed; 속도를 저장하는 것