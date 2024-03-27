import stuUpdate

stu = [1, '홍길동', 100, 100, 100, 300, 100.0, 1]
s_title = ["", "국어", "영어", "수학"]

while True :
    print('-'*40)
    print("학생데이터 : ", stu)
    # print("1. 학생성적입력")
    # print("2. 학생성적출력")
    print("3. 학생성적수정")
    # print("0. 프로그램종료")

    choice = int(input("원하는 번호를 입력하세요. >> "))
    
    if choice == 3 :
        stuUpdate.stu_update(choice, s_title, stu) # < ===== 선생님 파일 확인필요 **********

                        