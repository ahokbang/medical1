# ********** 외우기 **********

students = [{'stuNo': 'S001', 'name': '홍길동', 'kor': 100, 'eng': 99, 'math': 87, 'total': 286, 'avg': 95.33}, 
            {'stuNo': 'S002', 'name': '유관순', 'kor': 98, 'eng': 93, 'math': 87, 'total': 278, 'avg': 92.67}, 
            {'stuNo': 'S003', 'name': '이순신', 'kor': 88, 'eng': 76, 'math': 30, 'total': 194, 'avg': 64.67}, 
            {'stuNo': 'S004', 'name': '김구', 'kor': 100, 'eng': 100, 'math': 100, 'total': 300, 'avg': 100.0}, 
            {'stuNo': 'S005', 'name': '강감찬', 'kor': 98, 'eng': 85, 'math': 44, 'total': 227, 'avg': 75.67}]

cnt = len(students)+1
# 학생번호 사용

while True:
    print('-'*40)
    print('[학생성적프로그램]')
    print('-'*40)
    print('1. 학생성적입력')
    print('2. 학생성적전체출력')
    print('3. 학생검색')
    print('4. 학생수정')
    print('5. 등수처리')
    print('6. 학생삭제')
    print('0. 프로그램 종료')
    print('-'*40)
    choice = input('원하는 번호를 입력하세요:  ')
    print('-'*40)
    if not choice.isdigit():
        print('숫자만 입력 가능합니다.')
        continue # 반복문 계속실행
    choice = int(choice)
    
    # 1. 학생성적입력
    if choice == 1 :
        while True :
            name = input(f"{len(students)+1}번째 학생의 이름을 입력하세요(0. 취소). >> ")
            if name == "0" :
                print("이름 입력을 취소합니다.")
                break
            student = {} # 데이터 초기화
            student["stuNo"] = "S" + "{:03d}" .format(cnt) # ********** 외우기 **********
            student["name"] = name # 딕셔너리 추가
            kor = int(input("국어점수를 입력하세요. >> "))
            student["kor"] = kor
            eng = int(input("영어점수를 입력하세요. >> "))
            student["eng"] = eng
            math = int(input("수학점수를 입력하세요. >> "))
            student["math"] = math
            total = kor + eng + math
            student["total"] = total
            avg = total / 3
            student["avg"] = float("{:.2f}".format(avg))
            # list에 추가
            students.append(student)
            cnt += 1 # 학번 증가
            print("입력 데이터 : ", student)
            print(students) # 제이슨 타입 
        
    # 2. 학생성적전체출력
    elif choice == 2 :
            # 전체 출력
        count = input("학생전체 출력을 하시겠습니까? (1. 확인, 0. 취소)")
        if count == "0" :
            break
        print('[ 학생성적전체출력 ]')
        print("-"*65)
        print("학번\t이름\t국어\t영어\t수학\t합계\t평균\t등수")
        print("-"*65)
        for s_dic in students : 
            for s_key in s_dic :
                print(s_dic[s_key], end='\t')
            print()
        print("-"*65)
        print()
    
    # 3. 학생검색    
    elif choice == 3 :
        pass
    
    # 4. 학생수정
    elif choice == 4:
        s_title = ['', '국어', '영어', '수학']
        while True : 
            search = input("찾고자 하는 학생의 이름을 입력하세요(0.취소). >> ")
            chk = 0
            if search == '0' :
                break
            for s_dic in students : # 5명이 있으면 5번 반복
                if s_dic["name"] == search :
                    break
                chk += 1
            print("찾고자하는 학생의 위치 : ", chk)  
            if chk == len(students) :
                print(f"{search} 학생을 찾을 수 없습니다. 다시 입력하세요.")
            else : 
                print(f"{search} 학생을 찾았습니다.")
                while True :
                    print("[ 수정할 과목 선택 ]")
                    print("-"*30)
                    print("1. 국어\t2. 영어\t3. 수학")
                    s_input = int(input("수정하려는 과목을 선택하세요(0. 취소)."))
                    if s_input == 1 :
                        s_1 = "kor"
                        print("[ {} 수정 ]" .format(s_title[s_input]))
                        # 해당하는 학생의 국어점수를 출력하시오.
                        print("현재 {}점수 : {}" .format(s_title[s_input], students[chk][s_1]))
                        print('-'*20)
                        score = int(input("수정할 {}점수를 입력하세요. >> " .format(s_title[s_input])))
                        students[chk][s_1] = score
                        # 합계수정
                        students[chk]["total"] = score + students[chk]["eng"] + students[chk]["math"]
                        students[chk]["avg"] = float("{:.2f}" .format(students[chk]["total"] / 3))
                        print(f"{s_title[s_input]}점수가 {students[chk]["s_1"]}점으로 수정이 완료되었습니다.")
                        print(students[chk])                       
                    elif s_input == 2 :
                        s_1 = "eng"
                        print("[ {} 수정 ]" .format(s_title[s_input]))
                        print("현재 {}점수 : {}" .format(s_title[s_input], students[chk][s_1]))
                        print('-'*20)
                        engscore = int(input("수정할 {}점수를 입력하세요. >> " .format(s_title[s_input])))
                        students[chk][s_1] = engscore
                        students[chk]["total"] = students[chk]["kor"] + students[chk]["eng"] + students[chk]["math"]
                        students[chk]["avg"] = float("{:.2f}" .format(students[chk]["total"]/3))
                        print(f"{s_title[s_input]}점수가 {students[chk][s_1]}점으로 수정이 완료되었습니다.")
                        print(students[chk])
                    elif s_input == 3 :
                        s_1 = "math"
                        print("[ {} 수정 ]" .format(s_title[s_input]))
                        print("현재 {} 점수 : {}" .format(s_title[s_input] ,students[chk][s_1]))
                        print("-"*20)
                        mathscore = int(input("수정할 {}점수를 입력하세요. >> " .format(s_title[s_input])))
                        students[chk][s_1] = mathscore
                        students[chk]["total"] = students[chk]["kor"] + students[chk]["eng"] + students[chk]["math"]
                        students[chk]["avg"] = float("{:.2f}" .format(students[chk]["total"]/3))
                        print("{}점수가 {}점으로 수정되었습니다." .format(s_title[s_input], students[chk][s_1]))
                        print(students[chk])
                    elif s_input == 0 :
                        print("과목 수정을 취소합니다.")
                        break

    # 5. 등수처리 : 데이터가 많을 때는 입력하자마자 등수처리하면 시간이 너무 오래걸려서 따로 빼둠. 시간이 많이 걸려(if문) list.append도 시간 오래걸림
    elif choice == 5:
        for i, s_dic in enumerate(students) : # i 없어도 되지 않나? for s_dic in students로 해도 나와 # 다시 해보면 안나와(3/11)
            rank_cnt = 1 # 등수 처리 변수
            # print(s_dic["total"]) # total 다 출력하기
            for i_dic in students :
                # print(s_dic["total"])
                if s_dic["total"] < i_dic["total"] : # 두 수를 비교
                    rank_cnt += 1 # 현재 학생의 합계보다 크면 1 증가
            s_dic["rank"] = rank_cnt
        print("등수처리가 완료되었습니다.")
        print(students)
        
    # 6. 학생삭제
    elif choice == 6:
        while True : 
            search = input("삭제하고자 하는 학생의 이름을 입력하세요(0.취소). >> ")
            chk = 0
            if search == '0' :
                break
            for s_dic in students : # 5명이 있으면 5번 반복
                if s_dic["name"] == search :
                    break
                chk += 1            
            print("찾고자하는 학생의 위치 : ", chk)             
            if chk >= len(students) :
                print("찾고자 하는 학생이 없습니다.")
            else :
                print("{} 학생을 찾았습니다." .format(search))
                s_input = input("{} 학생 성적을 삭제하시겠습니까? (1. 실행 0. 취소)" .format(search))
                # 삭제
                if s_input != "1" :
                    print("삭제를 취소합니다.")
                    break
                else :
                    del students[chk]
                    print("{} 학생성적이 삭제 되었습니다." .format(search))
                    print(students)
                    
    elif choice == 0:
        print('프로그램을 종료합니다.')
        break  # 반복문 종료
    
    else:
        print('선택된 서비스가 없습니다.')