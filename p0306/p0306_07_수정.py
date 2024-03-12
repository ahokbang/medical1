# 리스트를 딕셔너리로 변경
'''
students = [
            [S001, "홍길동", 100, 99, 87, 286, 95.33, 2], 
            [S002, "유관순", 98, 93, 87, 278, 92.67, 3], 
            [S003, "이순신", 88, 76, 30, 194, 64.67, 5],
            [S004, '김구', 100, 100, 100, 300, 100, 1],
            [S005, '강감찬', 98, 85, 44, 227, 75.67, 4]
                                                ]
'''
students = [{'stuNo': 'S001', 'name': '홍길동', 'kor': 100, 'eng': 99, 'math': 87, 'total': 286, 'avg': 95.33}, 
            {'stuNo': 'S002', 'name': '유관순', 'kor': 98, 'eng': 93, 'math': 87, 'total': 278, 'avg': 92.67}, 
            {'stuNo': 'S003', 'name': '이순신', 'kor': 88, 'eng': 76, 'math': 30, 'total': 194, 'avg': 64.67}, 
            {'stuNo': 'S004', 'name': '김구', 'kor': 100, 'eng': 100, 'math': 100, 'total': 300, 'avg': 100.0}, 
            {'stuNo': 'S005', 'name': '강감찬', 'kor': 98, 'eng': 85, 'math': 44, 'total': 227, 'avg': 75.67}]
subject = ['순번', '학번', '이름', '국어', '영어', '수학', '합계', '평균', '등수']
s_title = ['', '국어', '영어', '수학']
cnt = len(students)+1 # 학번

while True : 
    # 찾는 부분 프로그램 작성하시오.
    ''' 내가한 거 : ********** 다시 해보기 ***********
    for stu in students :
        schName = input("수정할 학생의 이름을 입력하세요(0. 취소). >> ") ; => 얘만 반복돼
        if schName == '0' :
            break
        elif schName in stu :
            print(f"입력하신 학생의 이름은 {schName}입니다.")
            print("학생이 있습니다.")
    '''
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
                # 함수선언
                # 함수호출
                # s_update(s_1)
                '''
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
                '''
            elif s_input == 2 :
                s_1 = "eng"
                # 함수
                # s_update(s_1)
                '''
                print("[ {} 수정 ]" .format(s_title[s_input]))
                print("현재 {}점수 : {}" .format(s_title[s_input], students[chk][s_1]))
                print('-'*20)
                engscore = int(input("수정할 {}점수를 입력하세요. >> " .format(s_title[s_input])))
                students[chk][s_1] = engscore
                students[chk]["total"] = students[chk]["kor"] + students[chk]["eng"] + students[chk]["math"]
                students[chk]["avg"] = float("{:.2f}" .format(students[chk]["total"]/3))
                print(f"{s_title[s_input]}점수가 {students[chk]["s_1"]}점으로 수정이 완료되었습니다.")
                print(students[chk])
                '''
            elif s_input == 3 :
                s_1 = "math"
                # 함수
                # s_update(s_1)
                '''
                print("[ {} 수정 ]" .format(s_title[s_input]))
                print("현재 {} 점수 : {}" .format(s_title[s_input] ,students[chk][s_1]))
                print("-"*20)
                mathscore = int(input("수정할 {}점수를 입력하세요. >> " .format(s_title[s_input])))
                students[chk][s_1] = mathscore
                students[chk]["total"] = students[chk]["kor"] + students[chk]["eng"] + students[chk]["math"]
                students[chk]["avg"] = float("{:.2f}" .format(students[chk]["total"]/3))
                print("{}점수가 {}점으로 수정되었습니다." .format(s_title[s_input], students[chk][s_1]))
                print(students[chk])
                '''
            elif s_input == 0 :
                print("과목 수정을 취소합니다.")
                break

'''
# 함수 선언 : 소스코드를 거의 동일하게 만들어놔야 함수를 활용할 수 있어
def s_update(s_1) :
    print("[ {} 수정 ]" .format(s_title[s_input]))
    print("현재 {}점수 : {}" .format(s_title[s_input], students[chk][s_1]))
    print('-'*20)
    score = int(input("수정할 {}점수를 입력하세요. >> " .format(s_title[s_input])))
    students[chk][s_1] = score
    # 합계수정
    students[chk]["total"] = students[chk]["kor"] + students[chk]["eng"] + students[chk]["math"]
    students[chk]["avg"] = float("{:.2f}" .format(students[chk]["total"] / 3))
    print(f"{s_title[s_input]}점수가 {students[chk]["kor"]}점으로 수정이 완료되었습니다.")
    print(students[chk])
    
    
    
함수를 사용하면 에러가 있는 그 부분을 실행하지 않는 한 프로그램이 돌아가. 
함수를 사용하지 않으면 프로그램 전체가 실행이 되지 않아.

딕셔너리는 리스트보다 유지보수가 용이, 키 값이 있어 어떤 데이터인지 확인 가능
함수, 클래스 등 계속 배울거야.
'''