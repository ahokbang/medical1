
# for문을 사용해서 5번 반복 
print('-'*35)
print("\t[학생성적프로그램]")
print('1. 학생성적입력')
print('4. 학생성적전체출력')
print('0. 프로그램 종료')
print('-'*35)
ch = input("원하는 번호를 입력하세요. >> ")
print(ch)

for i in range(5) :
    print('-'*35)
    print("\t[학생성적프로그램]")
    print('1. 학생성적입력')
    print('4. 학생성적전체출력')
    print('0. 프로그램 종료')
    print('-'*35)
    ch = input("원하는 번호를 입력하세요. >> ")
    print(ch)
    # if 문을 사용해서 1을 누르면 [학생성적입력]
    # 4를 누르면 [학생성적전체출력]
    # 0을 누르면 [프로그램 종료]
    if ch == "1" :       # ********** ch가 문자니까 1에 "" 필수!! **********
        print("학생성적입력")
    elif ch == "4" :
        print("학생성적전체출력")
    elif ch == "0" :
        print("프로그램 종료")
    else :
        print("번호를 잘못 입력하셨습니다.")

'''선생님 답
student = [] 

for i in range(5): 
    print('-'*35)
    print("\t[학생성적프로그램]")
    print('1. 학생성적입력')
    print('4. 학생성적전체출력')
    print('0. 프로그램 종료')
    print('-'*35)
    ch = input("원하는 번호를 입력하세요. >> ")
    print(ch)
    
    if ch == "1" :
        print("학생성적입력") 
        
        stu1 = ['홍길동', 100, 100, 100]
        stu_name = '이순신'
    elif ch == '4' :
        print("학생성적출력")
        print(stu1)             ; 출력이 돼.
        print(stu_name)         ; 출력이 돼.
    elif ch == '0' :
        print("프로그램 종료")
    else :
        print("잘못입력하셨습니다.")
        
    print('*'*35)
print("프로그램이 종료되었습니다.")
    
'''
student = [] 

for i in range(5): 
    print('-'*35)
    print("\t[학생성적프로그램]")
    print('1. 학생성적입력')
    print('4. 학생성적전체출력')
    print('0. 프로그램 종료')
    print('-'*35)
    ch = input("원하는 번호를 입력하세요. >> ")
    print(ch)
    # 잘 모르겠어!!! 
    if ch == "1" :
        print("학생성적입력") 
        # 이름, 국, 영, 수, 점수를 입력 받아     
        # 1명의 학생 리스트를 만들고, 
        # student.append(학생리스트) => 전체 학생 리스트
        stu = []        
        name = input("이름을 입력하세요. >> ")
        kor = int(input("국어 점수를 입력하세요. >> "))
        eng = int(input("영어 점수를 입력하세요. >> "))
        mth = int(input("수학 점수를 입력하세요. >> "))
        
        stu.append(name)
        stu.append(kor)
        stu.append(eng)
        stu.append(mth)
        
        student.append(stu)
                                         
    elif ch == '4' : # 전체 학생리스트를 사용해서 출력 
        print("학생성적출력")
        # 출력, for를 사용해서 학생 수 만큼 출력
        for i in range(len(student)):
            print(student)    # ********** n * n으로 출력돼. 수 만큼 출력하는 걸로 어떻게 바꿀 수 있을까? **********
            
    elif ch == '0' :
        print("프로그램 종료")
    else :
        print("잘못입력하셨습니다.")
        
    print('*'*35)
print("프로그램이 종료되었습니다.")