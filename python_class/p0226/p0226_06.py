
student = []

'''
두명 이상이 학생의 이름, 국, 영, 수 점수를 입력 받아 리스트를 생성 후,
1. student 리스트에 넣어주세요.
2. student 리스트 전체 출력
'''
# 1. 
# stu1 = input("첫번째 학생의 이름, 국, 영, 수 점수를 입력하세요. >> ")
# student.append(stu1)

# stu2 = input("두번째 학생의 이름, 국, 영, 수 점수를 입력하세요. >> ")
# student.append(stu2)

# 1. 
name1 = input("첫번째 학생의 이름을 입력하세요. >> ")
kor1 = int(input("첫번째 학생의 국어점수를 입력하세요. >> "))
eng1 = int(input("첫번째 학생의 영어점수를 입력하세요. >> "))
math1 = int(input("첫번째 학생의 수학점수를 입력하세요. >> "))
total1 = kor1 + eng1 + math1
avg1 = total1 / 3
stu1 = [name1, kor1, eng1, math1, total1, avg1]
student.append(stu1)

name2 = input("두번째 학생의 이름을 입력하세요. >> ")
kor2 = int(input("두번째 학생의 국어점수를 입력하세요. >> "))
eng2 = int(input("두번째 학생의 영어점수를 입력하세요. >> "))
math2 = int(input("두번째 학생의 수학점수를 입력하세요. >> "))
total2 = kor2 + eng2 + math2
avg2 = total2 / 3
stu2 = [name2, kor2, eng2, math2, total2, avg2]
student.append(stu2)

2. 
print(student)

'''
선생님 답 
듀플 () 딕셔너리 {} 리스트 []

학생 1명
name = input("1. 이름을 입력하세요. >> ")
kor = int(input("국어점수를 입력하세요. >> "))
eng = int(input("영어점수를 입력하세요. >> "))
math = int(input("수학점수를 입력하세요. >> "))
# 리스트에 값 넣기
# 방법 1
stu1 = [name, kor, eng, math]
stu1.append(kor+eng+math) # 총점
stu1.append((kor+eng+math)/3) # 평균
student.append(stu1)
print(student)

# 방법 2
stu1 = [] # 빈 리스트를 만들고
stu1.append(name)
stu1.append(kor)
stu1.append(eng)
stu1.append(math)
print(stu1)

또 다른 방법 ; 더 복잡해
학생 1명
stu1 = ["", 0, 0, 0] ; 기본값 설정 길이 설정
# stu1 = []로 설정 후 아래 사용할 경우 오류
stu1[0] = input("이름을 입력하세요. >> "); 이름을 넣을 예정
stu1[1] = int(input("국어점수를 입력하세요. >> ")); 국어
stu1[2] = int(input("영어점수를 입력하세요. >> ")); 영어
stu1[3] = int(input("수학점수를 입력하세요. >> ")); 수학
print(stu1)

두번째 학생
stu2 = []
name = input("1. 이름을 입력하세요. >> ")
kor = int(input("국어점수를 입력하세요. >> "))
eng = int(input("영어점수를 입력하세요. >> "))
math = int(input("수학점수를 입력하세요. >> "))
stu2 = [name, kor, eng, math]
stu2.append(kor+eng+math) # 총점
stu2.append((kor+eng+math)/3) # 평균
student.append(stu2)
print(student)

'''
