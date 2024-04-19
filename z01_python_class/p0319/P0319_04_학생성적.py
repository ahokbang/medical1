# student 클래스 생성, 파일 불러와서 클래스에 저장 후 출력하시오.

class Student :
    count = 1 # 클래스함수
    
    def __init__(self, name, kor, eng, math, stuNo=0, rank=0) :
        if stuNo == 0 :
            self.stuNo = Student.count
        else :
            self.stuNo = stuNo
            
        self.name = name
        self.kor = kor
        self.eng = eng
        self.math = math
        self.total = kor + eng + math 
        self.avg = float("{:.2f}" .format(self.total/3))
        self.rank = rank
    
    def __str__(self) :
        return f"학생성적 : {self.stuNo}\t{self.name}\t{self.kor}\t{self.eng}\t{self.math}\t{self.total}\t{self.avg}\t{self.rank}"

# ----------------------
# 파일 불러와서 저장하기 
# ----------------------

students = []        
      
# 1. 파일 불러오기
f = open("stu.txt", "r", encoding='utf8')
while True :
    txt = f.readline()
    if txt == "" : break
    txt_list = txt.split(',')
    s = Student(txt_list[1], int(txt_list[2]), int(txt_list[3]), int(txt_list[4]), int(txt_list[0]), int(txt_list[7]))
    students.append(s)
f.close()

# --------------------------------
def stu_main_print() :
    print('\t[ 학생성적출력 ]')
    print('-'*65)
    print('학번\t이름\t국어\t영어\t수학\t총점\t평균\t등수', sep='\t')
    print('-'*65)

# ---------------------------------

# 파일 불러오기한 후 학생 수에서 +1 추가
Student.count = len(students)+1
# # 리스트 출력
# for stu in students :
#     print(stu)

while True:
    print('-'*40)
    print("[ 학생성적프로그램 ]")
    print('-'*40)
    print("1. 학생성적입력")
    print('2. 학생성적전체출력')
    print('3. 학생검색')
    # print('4. 학생수정')
    # print('5. 등수처리')
    # print('6. 학생삭제')
    # print('7. 학생성적파일 저장')
    print('0. 프로그램 종료')
    print('-'*40)
    choice = input("원하는 번호를 입력하세요. >> ")
    choice = int(choice)
    
    if choice == 1 :
        while True : 
            name = input(f"{len(students)+1}번째 학생의 이름을 입력하세요. 0. 취소 >> ")
            if name == "0" :
                print("이름 입력을 취소합니다.")
                break
            kor = int(input("국어점수를 입력하세요. >> "))
            eng = int(input("영어점수를 입력하세요. >> "))
            math = int(input("수학점수를 입력하세요. >> "))
            # 평균, 합계는 다 클래스로 보냈어
            # list에 추가
            s = Student(name, kor, eng, math)
            students.append(Student(name, kor, eng, math))
            print("입력 데이터 : ", s)  

    if choice == 2 :
        stu_main_print()
        # 데이터 출력
        for i in students :
            print(i) # 객체를 출력
        
        print()
        

    if choice == 3 :
        print("[ 학생성적 검색 ]")
        search = input("찾고자 하는 학생 이름을 입력하세요. >> ")
        
        # 전체리스트에서 학생검색
        s_cnt = 0
        s_list = []
        for i in students :
            if search in i.name :
                s_list.append(i)
            s_cnt += 1
        
        if s_cnt != len(students) : 
            stu_main_print()
            print(students[s_cnt])
        else :
            print("찾고자 하는 학생이 없습니다. 다시 검색하세요.")