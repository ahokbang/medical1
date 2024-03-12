# 어제 한 거 다시 해보기!!

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
        # 이름, 국, 영, 수, 점수를 입력 받아     
        # 1명의 학생 리스트를 만들고, 
        # student.append(학생리스트) => 전체 학생 리스트
                    
        name = input("이름을 입력하세요. >> ")
        kor = int(input("국어 점수를 입력하세요. >> "))
        eng = int(input("영어 점수를 입력하세요. >> "))
        mth = int(input("수학 점수를 입력하세요. >> "))
        
        stu = [name, kor, eng, mth]
        
        student.append(stu)
                                         
    elif ch == '4' : # 전체 학생리스트를 사용해서 출력 
        print("학생성적출력")
        # 출력, for를 사용해서 학생 수 만큼 출력
        print("이름\t국어\t영어\t수학")
        for i in range(len(student)):
            print("{}\t{}\t{}\t{}".format(student[i][0], student[i][1], student[i][2],student[i][3]))
            
    elif ch == '0' :
        print("프로그램 종료")
        
    else :
        print("잘못입력하셨습니다.")
        
    print('*'*35)
print("프로그램이 종료되었습니다.")


''' 선생님 답

들여쓰기 주의할 것 !!!

student = [] 

for i in range(10): 
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
        name = input("이름을 입력하세요. >> ")
        kor = int(input("국어점수를 입력하세요. >> "))
        eng = int(input("영어점수를 입력하세요. >> "))
        math = int(input("수학점수를 입력하세요. >> "))
        
        # 한 명의 학생의 정보를 담은 리스트
        s = [1, name, kor, eng, math, (kor+eng+math), (kor+eng+math)/3, 0]
        
        student.append(s)
        # [[1, 홍길동, 100, 100, 100, 300 100, 0], [1, 이순신, 90, 90, 90, ...], [...], ... ]
        
        #print(student)
                                         
    elif ch == '4' : # 전체 학생리스트를 사용해서 출력 
        print("학생성적출력")
        # 출력, for를 사용해서 학생 수 만큼 출력
        print("번호\t이름\t국어\t영어\t수학\t총점\t평균\t등수")
        for s in range(len(student)): # len(student) = 학생의 수
            print("{}\t{}\t{}\t{}".format(student[s][0], student[s][1], student[s][2],student[s][3]), student[s][4], student[s][5], student[s][6], student[s][7]))
            
    elif ch == '0' :
        print("프로그램 종료")
        
    else :
        print("잘못입력하셨습니다.")
        
    print('*'*35)
    
print("프로그램이 종료되었습니다.")



'''