# 학생 성적 입력

# 변수를 사용합니다.
# stu_name = '홍길동'
# kor = 100
# eng = 100
# math = 100

# 입력을 받아서 총점과 평균을 계산하고, 출력해보세요.
# print(''.format) # format 사용
# 홍길동 100 100 100 300 100.0

stu_name = input("학생의 이름을 입력하세요. >> ")
kor = int(input("국어 점수를 입력하세요. >> "))
eng = int(input("영어 점수를 입력하세요. >> "))
math = int(input("수학 점수를 입력하세요. >> "))
total = kor + eng + math
avrg = total / 3

print('번호\t이름\t국어\t영어\t수학\t합계\t평균\t등수')
print('{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}' .format(1, stu_name, kor, eng, math, total, avrg, 1))

# list를 사용한 방법
stu = [1, '홍길동', 100, 100, 100, 300, 100.0, 1]
stu1 = [1, stu_name, kor, eng, math, total, avrg, 1]

print(stu)
print(stu1)