
student = [[1, '홍길동', 100, 100, 100, 300, 100.0, 1],
            [2, '유관순', 90, 90, 90, 270, 90.0, 1]]



print('-'*35)
print('\t[학생성적프로그램]')
print('1. 학생성적입력') # 1명만 입력 > (이름, 국, 영, 수) student에 추가 append()  # print(student)
print('4. 학생성적전체출력') # 2명이 출력
print('-'*35)
ch = input("원하는 번호를 입력하세요.")

if ch == "1" :
    name = input("이름을 입력하세요. >> ")
    kor = int(input("국어점수를 입력하세요. >> "))
    eng = int(input("영어점수를 입력하세요. >> "))
    math = int(input("수학점수를 입력하세요. >> "))
    total = kor + eng + math
    avg = total / 3
    stu = [3, name, kor, eng, total, avg, 3]
    student.append(stu)
    print(student)
elif ch == '4' :
    print('[학생 성적 출력]')
    print('번호\t이름\t국어\t영어\t수학\t총점\t평균\t등수')
    print("{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}" .format(student[0][0], student[0][1], student[0][2],student[0][3], student[0][4], student[0][5], student[0][6], student[0][7]))
    print("{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}" .format(student[1][0], student[1][1], student[1][2],student[1][3], student[1][4], student[1][5], student[1][6], student[1][7]))
else :
    print("잘못입력하셨습니다.")

'''선생님 답
ch는 문자로 받았음에 유의
ch = input("원하는 번호를 입력하세요. >> ")

if ch == "1" :   # 1에 "" 있어야 해***********
아니면 숫자형으로 변환해줘.
ch = int(ch)


if ch == 1 : # 학생 성적 입력
    print('[학생 성적 입력']) # 이름, 국어, 영어, 수학 필요
    name = input("이름을 입력하세요. >> ")
    kor = int(input("국어점수를 입력하세요. >> "))
    eng = int(input("영어점수를 입력하세요. >> "))
    math = int(input("수학점수를 입력하세요. >> "))
    total = kor+eng+math
    avg = total/3
    # stu1 = [3, name, kor, eng, math, total, avg, 1]
    stu1.append(kor+eng+math)
    stu1 = [3, name, kor, eng, math]
    stu1.append(total)
    stu1.append(avg)
    stu1.append(1)
    studend.append(stu1)
    print(student)
    
    
elif ch == 4 : # 학생 성적 전체 출력
    print('[학생 성적 출력'])
    print('번호\t이름\t국어\t영어\t수학\t총점\t평균\t등수')
    print('{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}' .format(student[0][0], student[0][1], student[0][2], student[0][3], student[0][4], student[0][5], student[0][6],student[0][7])) # 홍길동
    print('{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}' .format(student[1][0], student[1][1], student[1][2], student[1][3], student[1][4], student[1][5], student[1][6],student[1][7])) # 유관순

else :
    print("잘못입력하셨습니다.")

'''
