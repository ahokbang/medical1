
students = [{'stuNo': 'S001', 'name': '홍길동', 'kor': 100, 'eng': 99, 'math': 87, 'total': 286, 'avg': 95.33}, 
            {'stuNo': 'S002', 'name': '유관순', 'kor': 98, 'eng': 93, 'math': 87, 'total': 278, 'avg': 92.67}, 
            {'stuNo': 'S003', 'name': '이순신', 'kor': 88, 'eng': 76, 'math': 30, 'total': 194, 'avg': 64.67}, 
            {'stuNo': 'S004', 'name': '김구', 'kor': 100, 'eng': 100, 'math': 100, 'total': 300, 'avg': 100.0}, 
            {'stuNo': 'S005', 'name': '강감찬', 'kor': 98, 'eng': 85, 'math': 44, 'total': 227, 'avg': 75.67}]

# 학생성적입력 부분 구현하시오.
# 학생성적출력 부분 구현하시오.
choice = input("원하는 번호를 누르세요. 1: 학생성적입력 2. 학생성적출력 >> ")
# 학생성적입력
cnt = len(students) + 1 # 학번
while True :
    if choice == "1" :
        name = input(f"{len(students)+1}번째 학생의 이름을 입력하세요(0. 취소). >> ")
        if name == '0' :
            print("입력을 취소합니다.")
            break
            
        student = {} # 초기화
        student["stuNo"] = "S" + "{:03d}".format(cnt)
        student["name"] = name
        kor = int(input("국어점수를 입력하세요. >> "))
        student["kor"] = kor
        eng = int(input("영어점수를 입력하세요. >> "))
        student["eng"] = eng
        math = int(input("수학점수를 입력하세요. >> "))
        student["math"] = math
        total = kor + eng + math
        student["total"] = total
        avg = total/3
        student["avg"] = float("{:.2f}" .format(avg))
        students.append(student)
        cnt += 1
        print("입력데이터 : ", student)
        print(students)

    # 학생성적출력
    elif choice == '2' :
        numPrt= input("학생성적을 출력하시겠습니까? (1. 실행 0. 취소)")
        if numPrt == "0" :
            break
        print('-'*65)
        print("[ 학생성적전체출력]")
        print('-'*65)
        print("학번\t이름\t국어\t영어\t수학\t합계\t평균\t등수")
        print('-'*65)
        for s_dic in students :
            for s_key in s_dic :
                print(s_dic[s_key], end='\t')
            print()
        print('-'*65)
        print()
        
            
        

    


