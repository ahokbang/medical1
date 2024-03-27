'''
# 국어, 영어, 수학을 입력 받아 합계를 출력하시오.
kor = int(input("국어 점수를 입력하세요. >> "))
eng = int(input("영어 점수를 입력하세요. >> "))
math = int(input("수학 점수를 입력하세요. >> "))
# 합계
print("합계 : ", (kor+eng+math))
'''

# 2명의 학생의 국어, 영어, 수학을 입력 받아 합계를 출력하시오.
'''
kor = []
eng = []
math = []
total = []
=> 위에 처럼 묶으면 너무 많으니 하나로 묶자.
'''
students = [] # 1차원 리스트
'''
students = [[],[],[]] # 2차원 리스트
students = [[[]],[[]],[[]]] # 3차원 리스트, 보통은 2개 이상 쓰지 않아. 너무 복잡하니까. 3차원부터는 class라는 걸 쓸거야.
...
'''
student = []
for i in range(3) : 
    student = []
    name = input("이름을 입력하세요. >> ")
    kor = int(input("국어 점수를 입력하세요. >> "))
    eng = int(input("영어 점수를 입력하세요. >> "))
    math = int(input("수학 점수를 입력하세요. >> "))
    student.append(name)
    student.append(kor)
    student.append(eng)
    student.append(math)
    sum = student[1] + student[2] + student[3]
    student.append(sum)
    student.append('{:.2f}' .format(sum/3))
    students.append(student)
    
''' 선생님 풀이
# 2명의 학생이니까
student = [] # 초기화
for i in range(0,2) : # for문을 쓰면 다음의 문제가 발생해. 이전의 데이터에 추가되므로 초기화 필요
student.append(input("이름을 입력하세요."))
student.append(int(input("국어점수를 입력하시오.")))
student.append(int(input("수학점수를 입력하시오.")))
student.append(int(input("영어점수를 입력하시오.")))
sum = student[1] + student[2] + student[3]
student.append(sum)
students.append(student)
'''
# 합계
print(student)
print(students)

print("[학생성적 출력]")
print("-"*50)
print("이름\t국어\t영어\t수학\t합계\t평균\n")
print("-"*50)
# 전체출력
for stu in students :
    for s in stu :
        print(s, end='\t')
    print()
print("-"*50)

# 총 학생의 총 국어점수,총 영어점수, 총 수학점수 총 합계, 총 평균

# 2차원 리스트는 for문을 2번 사용. 3차원은 3번, 4차원은 4번 사용.
for stu in students : 
    for s in stu :
        print(s, end="\t")
    print()
print()
print("-"*50)

# 3명의 국어점수 합계, 평균을 출력하시오.
kors = 0
engs = 0
maths = 0
totals = 0
avgs = 0

# [[홍길동, 100, 100, 99, 299, 99.97], 
# [유관순, 100, 100, 99, 299, 99.97], 
# [이순신, 100, 100, 99, 299, 99.97]]
for i, stu in enumerate(students) :
    kors = kors + stu[1]
    engs = engs + stu[2]
    maths += stu[3]
    totals += stu[4]
avgs += totals/len(students)
print('\t')
print('--\t합계\t{}\t{}\t{}\t{}\t{:.2f}' .format(kors, engs, maths, totals, avgs))


''' 내가 푼 거. ********** 다시 풀어보기 **********
for i in range(len(students)) : 
    sumKor = students[1][1] + students[2][1] + students[3][1]
    print(sumKor)
    
    avgKor = sumKor/3
print("국어점수의 합계 :", sumKor)
print("국어점수의 평균 :", avgKor)
'''
