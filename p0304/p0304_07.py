students = [
            [1, "홍길동", 90, 100, 99, 299, 99.97], 
            [2, "유관순", 80, 100, 99, 299, 99.97], 
            [3, "이순신", 100, 100, 99, 299, 99.97] 
                                                   ]
while True : 
    search = input("찾는 학생의 이름을 입력하세요.")
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