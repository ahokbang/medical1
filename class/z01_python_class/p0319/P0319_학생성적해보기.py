# -- student class
class Student :
    count = 1 # 클래스변수 사용
    def __init__(self, name, kor, eng, math, stuNo=0, rank=0):
        if stuNo == 0 :
            self.stuNo = Student.count # 클래스변수 사용
        else : 
            self.stuNo = stuNo