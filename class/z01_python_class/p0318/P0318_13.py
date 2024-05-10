class Student :
    stucount = 0
    stuNo = 0
    name = ""
    kor = 0
    eng = 0
    math = 0
    total = 0
    avg  = 0
    
    def __init__(self, name, kor, eng, math) :
        self.name = name
        self.kor = kor
        self.eng = eng
        self.math = math
        self.total = kor + eng + math
        self.avg = float("{:.2f}".format(self.total/3))
        Student.stucount += 1
        self.stuNo = Student.stucount