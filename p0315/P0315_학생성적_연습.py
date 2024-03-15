import stu_file

# stu.txt 파일열기호출
students = stu_file.stu_open()
s_title = ["", "국어", "영어", "수학"]

# 학생성적화면함수
def stu_main_print() :
    print('-'*40)
    print("[ 학생성적프로그램 ]")
    print('-'*40)
    print("1. 학생성적입력")
    print('2. 학생성적전체출력')
    print('3. 학생검색')
    print('4. 학생수정')
    print('5. 등수처리')
    print('6. 학생삭제')
    print('7. 학생성적파일 저장')
    print('0. 프로그램 종료')
    print('-'*40)
    choice = input("원하는 번호를 입력하세요. >> ")
    print('-'*40)
    if not choice.isdigit():
        print("숫자만 입력 가능합니다.")
    choice = int(choice)
    return choice

# 학생성적입력함수
def stu_insert() :
    while True : 
        name = input(f"{len(students)+1}번째 학생의 이름을 입력하세요. 0. 취소 >> ")
        if name == "0" :
            print("이름 입력을 취소합니다.")
            break
        student = {}
        student["stuNo"] = cnt
        student["name"] = name
        kor = int(input("국어점수를 입력하세요. >> "))
        student["kor"] = kor
        eng = int(input("영어점수를 입력하세요. >> "))
        student["eng"] = eng
        math = int(input("수학점수를 입력하세요. >> "))
        student["math"] = math
        