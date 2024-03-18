class Student :
    # stuNo = 0
    # stu_name = ""
    # kor = 0
    # eng = 0
    # math = 0
    # total = 0
    # avg = 0
    # rank = 0
    # __init__(self) 했으니까 위에 변수 선언한 건 없어도 돼.
    
    def __init__(self, stuNo=0, stu_name="", kor=0, eng=0, math=0, total=0, avg=0, rank=0) :
        self.stuNo = stuNo
        self.stu_name = stu_name
        self.kor = kor
        self.eng = eng
        self.math = math
        self.total = total
        self.avg = avg
        self.rank = rank
    
# 출력하기(1번은 기본생성자, 2,3번은 전체생성자)
# 1,홍길동,99,99,87,285,95.0,1
s1 = Student()
s1.stuNo = 1
s1.stu_name = "홍길동"
s1.kor = 99
s1.eng = 99
s1.math = 87
s1.total = s1.kor+s1.eng+s1.math
s1.avg = float("{:.2f}" .format(s1.total/3))
s1.rank = 1
print(s1.stuNo, s1.stu_name, s1.kor, s1.eng, s1.math, s1.total, s1.avg, s1.rank)

# 2,유관순,98,93,87,278,92.67,3
s2 = Student(2, "유관순", 98, 93, 87, 278, 92.67, 3)
print(s2.stuNo, s2.stu_name, s2.kor, s2.eng, s2.math, s2.total, s2.avg, s2.rank)

# 3,이순신,88,76,30,194,64.67,6
s3 = Student(3, "이순신", 88, 76, 30, 194, 64.67, 6)
print(s3.stuNo, s3.stu_name, s3.kor, s3.eng, s3.math, s3.total, s3.avg, s3.rank)



''' 선생님 풀이

class Student :
    stuNo = 0
    stu_name = ""
    kor = 0
    eng = 0
    math = 0
    total = 0
    avg = 0
    rank = 0
    
    def __int__(self, stuNo=0, stu_name="", kor=0, eng=0, math=0) :
        self.stuNo = stuNo
        self.stu_name = stu_name
        self.kor = kor
        self.eng = eng
        self.math = math
        self.total = kor + eng + math
        self.avg = float("{:.2f}" .format(self.total/3))
        self.rank = 0    

# 2,유관순,98,93,87,278,92.67,3    
s2 = Student(2,"유관순", 98, 93, 87)
print("2번 학생 :", s2.stuNo, s2.stu_name, s2.kor, s2.eng, s2.math, s2.total, s2.avg, s2.rank)

# 3,이순신,88,76,30,194,64.67,6
s3 = Student(3, "이순신", 88, 76, 30)
print("3번 학생 :", s3.stuNo, s3.stu_name, s3.kor, s3.eng, s3.math, s3.total, s3.avg, s3.rank)
'''

# 3명의 학생을 리스트에 추가 
stu_list = [s1, s2, s3]
