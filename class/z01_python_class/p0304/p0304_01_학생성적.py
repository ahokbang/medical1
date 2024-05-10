'''
저장의 방법
1) 변수
    - 변수의 종류 : bool, int, float, str
    - 데이터베이스 프로그램
2) 리스트
3) 디셔너리
4) 토플
'''
# ********** 3/8(금) 시험 **********
# ********** 이 정도는 무조건 외워야해!! **********
# 몇번째에 뭐가 있는지 끄낼 줄 알아야해. 나머지는 함수! 함수는 암기! 
# AI는 암기가 많아.

students = [] 
student = [] # 학생성적 저장
students = [
            [1, "홍길동", 100, 100, 99, 299, 99.67, 1], 
            [2, "유관순", 99, 99, 998, 296, 98.67, 1], 
            [3, "이순신", 80, 80, 81, 241, 80.33, 1],
            [4, '김구', 100, 100, 90, 290, 96.67, 1],
            [5, '강감찬', 90, 70, 50, 210, 70.0, 1]
                                                ]
cnt = len(students) # cnt는 학번사용
while True :
    print("-"*40)
    print("[학생성적프로그램]")
    print('-'*40)
    print("1. 학생성적입력")
    print("2. 학생성적전체출력")
    print("3. 학생검색")
    print("4. 학생성적수정")
    print("5. 등수처리")
    print("6. 학생삭제")
    print("0. 프로그램 종료")
    print('-'*40)
    choice = input("원하는 번호를 입력하세요. >> ")
    if not choice.isdigit() :
        print("숫자만 입력가능합니다.")
        continue # 계속 실행 반복문(while문으로)다시 (돌아가서) 실행
    choice = int(choice)
    
    # 1. 학생성적입력 프로그램
    if choice == 1 :
        # 무한반복 
        while True : 
            # cnt += 1 # 학번 # 여기에 있으면 취소 한 것도 카운트돼
            print("학생성적을 입력합니다.")
            print("-"*10)
            student = []
            name = input("이름을 입력하세요.(-1. 취소)")
            if name == "-1" :
                break  # while True 반복 종료          
            cnt += 1 # 학번 # 취소를 하는 건 count에 포함되면 안돼니까 여기에 위치해야 해!
            student.append(cnt)
            student.append(name)
            student.append(int(input("국어점수를 입력하시오.")))
            student.append(int(input("수학점수를 입력하시오.")))
            student.append(int(input("영어점수를 입력하시오.")))
            sum = student[2] + student[3] + student[4]
            # student[0] = 학번, student[1] = 이름
        # 합계저장
            student.append(sum)
        # 평균저장
            student.append("{:.2f}" .format(sum/3))
        # 학생 정보 students에 저장
            students.append(student)
        # 전체출력    
            print(students)
     
    # 2. 학생성적출력 프로그램 ; 간단하게만 할거야.
    elif choice == 2 :
        print("[학생성적 출력]")
        print("-"*50)
        print("학번\t이름\t국어\t영어\t수학\t합계\t평균")
        print("-"*50)
        # 전체출력
        for stu in students :
            for s in stu :
                print(s, end='\t')
            print()
        kors = 0
        engs = 0
        maths = 0
        totals = 0
        avgs = 0
        for j, stu in enumerate(students) : 
            kors = kors + stu[2]
            engs = engs + stu[3]
            maths += stu[4]
            totals += stu[5]
        avgs += totals/len(students)
        print('\t')
        print('--\t합계\t{}\t{}\t{}\t{}\t{:.2f}' .format(kors, engs, maths, totals, avgs))

     # 3. 학생 검색   
    elif choice == 3 :
        while True : # 무한 반복
             # 멈춤
            search = input("검색하고 싶은 학생 이름을 입력하세요(0. 취소).")
            chk = 0 # 찾는 정보 확인
            count = 0
            if search == "0" :
                break # True를 빠져 나오는 break
            for stu in students :
                if search in stu : 
                    chk = 1 # 정보를 찾았을 때 chk를 1로 변경 
                    # print("{}의 학생정보를 찾았습니다." .format(search))
                    break # for문을 빠져나오는 break
                # else :
                #     print("찾는 학생이 없습니다.")
                count += 1
            if chk == 1 :
                # 전체학생 정보출력
                print("[{} 학생성적 출력]" .format(search))
                print("-"*50)
                print("학번\t이름\t국어\t영어\t수학\t합계\t평균")
                print("-"*50)
                for i in students[count] :
                    print(i, end="\t")
                print()
            else :
                print("찾는 학생 정보가 없습니다.")    
    
    # 4. 학생성적수정 프로그램
    elif choice == 4 :
        while True : 
            search = input("찾는 학생의 이름을 입력하세요.(0. 취소)")
            if search == "0" :
                break # True를 빠져 나오는 break
            chk = 0
            count = 0
            for stu in students :
                if search in stu : 
                    chk = 1
                    break
                count += 1 # 찾는 학생의 위치값
            if chk == 0 :
                print("찾는 학생의 정보가 없습니다.")
            else : 
                print("입력한 학생이름 {}을(를) 찾았습니다." .format(search))
                print("[ 변경할 과목 선택 ]")
                print("1. 국어 2. 영어 3. 수학 0. 취소")
                print("-"*20)
                num = int(input(">>"))
                if num == 1 :
                    print("국어를 선택하셨습니다.")
                    print("현재 국어점수 : {}" .format(students[count][2])) # ********** count 잘 이해 안 가 **********
                    num = int(input("변경점수를 입력하세요."))
                    students[count][2] = num
                    print("국어점수가 변경되었습니다. ")
                    # 합계, 평균도 수정해야 해.
                    students[count][5] = students[count][2]+students[count][3]+students[count][4]
                    students[count][6] = float("{:.2f}" .format(students[count][5]/3)) # format은 string 타입
                    # 출력
                    print(students)
                    
                elif num == 2 :
                    print("영어를 선택하셨습니다.")
                    print("현재 영어점수 : {}" .format(students[count][3]))
                    num = int(input("변경점수를 입력하세요."))
                    students[count][3] = num
                    print("영어점수가 변경되었습니다. ")
                    # 합계, 평균도 수정해야 해.
                    students[count][5] = students[count][2]+students[count][3]+students[count][4]
                    students[count][6] = float("{:.2f}" .format(students[count][5]/3))
                    # 출력
                    print(students)
                                
                elif num == 3 :
                    print("수학을 선택하셨습니다.")
                    print("현재 수학점수 : {}" .format(students[count][4])) 
                    num = int(input("변경점수를 입력하세요."))
                    students[count][4] = num
                    print("수학점수가 변경되었습니다. ")
                    # 합계, 평균도 수정해야 해.
                    students[count][5] = students[count][2]+students[count][3]+students[count][4]
                    students[count][6] = float("{:.2f}" .format(students[count][5]/3))
                    # 출력
                    print(students)
                            
                elif num == 0 :
                    print("성적수정 취소를 선택하셨습니다.")
                    break
                    
                else :
                    print("번호를 잘못 입력하셨습니다.")
    
    # 5. 등수처리
    elif choice == 5 :
        while True : 
            choice = input("등수처리를 실행하시겠습니까?(1. 실행 0. 취소)")
            if choice == "0" :
                print("등수처리를 취소하셨습니다.")
                break
            else :
                # 등수처리 진행: 이중 for문 사용
                for i_stu in students :
                    no = 1 # 초기화
                    for j_stu in students :
                        # 각각의 총합 비교
                        if i_stu[5] < j_stu[5] :
                        # 또는 i_stu[5] == j_stu[5] : 이렇게 하면 다 2등으로 나와
                            no += 1 # 비교대상 총합이 더 크면 1 증가
                    i_stu[7] = no # 등수위치에 no 저장
            print("등수처리가 완료 되었습니다.")
            print('-'*40)
            print("[ 등수확인 ]")
            print("학번\t이름\t국어\t영어\t수학\t합계\t평균\t등수")
            print("-"*50)
            print(students) # 리스트 형식으로 보여 수정 필요
            print("-"*50)
    
    # 6. 학생삭제
    elif choice == 6 :
        while True :
            search = input("삭제하려는 학생의 이름을 입력하세요.")
            
            # 이름 찾기
            cnt = 0 # 반복해서 나오는 걸 막기 위함, 이름을 찾는 위치(찾은 학생의 위치)
            
            # 전체 학생 검색
            for stu in students :
                if stu[1] == search :
                    break
                cnt += 1                
            if cnt == len(students) : # 전체학생 수
                print("{} 학생을 찾을 수 없습니다." .format(search))
            else :
                print("{} 학생을 찾았습니다." .format(search))   
                choice = input("삭제하시겠습니까? (1. 삭제 0. 취소)")             
                if choice == "1" :
                    print("{} 학생의 데이터가 삭제되었습니다." .format(search))
                    del students[cnt]
                else : 
                    print("삭제가 취소되었습니다.")
                
            print(students) # 확인용
    
    # 0. 프로그램 종료
    elif choice == 0 :
        print("프로그램을 종료합니다.")
        break # 반복문 종료