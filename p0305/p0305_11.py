# student = ['K001', 'K002', 'k003']
students = []
count = 1
# 학번, 이름, 국어, 영어, 수학, 합계, 평균 입력하는 프로그램

while True :
    chk = input("학생성적을 추가하시겠습니까? (1. 추가, 0. 취소)")
    if chk == "1" :
        student = {}
        # 프로그램을 구현하시오. ********** 다시 해보기 **********
        ''' 내가 한 거. 
        # for i in range(len(student)) :
        #     stuNo += i
        '''
        
        # stuNo = "K"+count # error
        # sruNo = "K" + str(count)  # 문자형으로 변환해줘야해 
        # 1000 : 숫자 1,000 : 문자열, ','들어가면 문자로 돼 0001은 숫자가 아니야. 문자야. 0001을 int로 바꾸면 1이 돼.
        stuNo = "K"+"{:03d}".format(count)
        name = input("이름을 입력하세요. >> ")
        kor = int(input("국어점수를 입력하세요. >> "))
        eng = int(input("영어점수를 입력하세요. >> "))
        math = int(input("수학점수를 입력하세요. >> "))
        total = kor + eng + math
        avg = "{:.2f}".format(total/3)
        student["stuNo"] = stuNo
        student["name"] = name
        student["kor"] = kor
        student["eng"] = eng
        student["math"] = math
        student["total"] = total
        student["avg"] = avg
        # 최종 저장은 리스트에 딕셔너리로 저장
        students.append(student)
        print("[ 입력한 학생정보내역 ]")
        for k in student.keys() :
            print("{} : {}" .format(k, student[k]))
        print("-"*50)
        print("학생 1명 추가되었습니다.")
        count += 1             
    else :
        print("학번추가를 종료합니다.")

