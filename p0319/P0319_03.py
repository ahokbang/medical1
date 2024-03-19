import os

class Student :
    count = 1 # 클래스변수 사용 
    
    def __init__(self, name, kor, eng, math,stuNo=0, rank=0) : # stuNo, rank는 키워드 변수. 값을 안 넣어도 돼. 그 앞에 있는 변수들은 값을 넣어야 해.
        if stuNo == 0 :
            self.stuNo = Student.count # 클래스변수 사용
        else :
            self.stuNo = stuNo
        self.name = name
        self.kor = kor
        self.eng = eng
        self.math = math
        self.total = kor + eng + math
        self.avg = float("{:.2f}" .format(self.total/3))
        self.rank = rank
            
    def __str__(self) : # 객체 호출하면 출력됨.
        return f"학생성적 : {self.stuNo}, {self.name}, {self.kor}, {self.eng}, {self.math}, {self.total}, {self.avg}, {self.rank}"
        

students = []

# 파일 불러와서 저장하기
f = open("stu.txt", "r", encoding='utf8')
while True :
    txt = f.readline()
    if txt == "" : break
    txt_list = txt.split(',') # split은 문자열로 나누겠다는 뜻이므로 형변환 필요
    # 1,홍길동,99,99,87,286,95.0,1
    s = Student(txt_list[1], int(txt_list[2]), int(txt_list[3]), int(txt_list[4]), int(txt_list[0]), int(txt_list[7]))
    students.append(s)
f.close()

# 리스트 출력
for stu in students :
    print(stu)
    