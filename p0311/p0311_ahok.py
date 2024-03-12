# 학생성적 프로그램
students = [{}]

cnt = len(students)+1

choice = input("원하는 번호를 입력하세요 : ")
if not choice.isdigit() :
    print("숫자만 입력 가능합니다.") 
    continue 
choice = int(choice) 
    
# 학생성적입력
if choice == 1 :
    while True :
        name = input("{len(students)+1}번째 학생의 이름을 입력하세요.(0.취소)")
        if name == "0" :
            print("이름 입력을 취소합니다.")
            break
        
        student = {}
        student["stuNo"] = "S" + "{:03d}".format(cnt)
        student["name"] = name
        kor = int(input("국어점수를 입력하세요. >>"))
        student["kor"] = kor
        eng = int(input("영어점수를 입력하세요. >> "))
        student["eng"] = eng
        math = int(input("수학점수를 입력하세요. >> "))
        student["math"] = math
        total = kor + eng + math
        student["total"] = total
        avg = total/3
        avg = float("{:.2f}" .format(avg))
        students.append(student)
        cnt += 1
        print("입력데이터 : " .format(student))
        print(students)
        
# 학생성적출력
if choice == 2 :
    count = input("학생전체츨력을 하시겠습니까? 1. 실행")
    for s_dic in students :