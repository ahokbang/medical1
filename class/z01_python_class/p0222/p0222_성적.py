# 학생 이름, 국어, 영어, 수학 점수를 입력 받아서 아래와 같이 출력을 하고
# 만약에 평균이 80점 이상이면 [합격입니다.]를 출력하세요.
# if (조건문) 사용

name = input("첫번째 학생의 이름을 입력하세요. : ")
kor = int(input("첫번째 학생의 국어점수를 입력하세요. : "))
eng = int(input("첫번째 학생의 영어점수를 입력하세요. : "))
math = int(input("첫번째 학생의 수학점수를 입력하세요. : "))
ttl = kor+eng+math
avrg = ttl/3

name2 = input("두번째 학생의 이름을 입력하세요. : ")
kor2 = int(input("두번째 학생의 국어점수를 입력하세요. : "))
eng2 = int(input("두번째 학생의 영어점수를 입력하세요 : "))
math2 = int(input("두번째 학생의 수학점수를 입력하세요. : "))
ttl2 = kor2+eng2+math2
avrg2 = ttl2/3

print("번호\t이름\t국어\t영어\t수학\t합계\t평균\t등수")
print("{}\t{}\t{}\t{}\t{}\t{}\t{:.2f}\t{}" .format(1, name, kor, eng, math, ttl, avrg, 1))
print("{}\t{}\t{}\t{}\t{}\t{}\t{:.2f}\t{}" .format(2, name2, kor2, eng2, math2, ttl2, avrg2, 2))

if avrg >= 80:
    print("{}님 합격입니다." .format(name))
else: 
    print("{}님 불합격입니다." .format(name))

if avrg2 >= 80:
    print("{}님 합격입니다." .format(name2))
else:
    print("{}님 불합격입니다." .format(name2))