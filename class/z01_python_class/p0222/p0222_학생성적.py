print('-'*35)
print('\t[학생성적프로그램]')
print('-'*35)
print('1. 학생성적입력')
print('2. 학생성적수정')
print('3. 학생성적삭제')
print('4. 학생성적전체출력')
print('5. 학생검색출력')
print('6. 등수처리')
print('0. 프로그램종료')
print('-'*35)

# print('번호\t이름\t국어\t영어\t수학\t합계\t평균\t등수')
# print('{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}'.format(1,'홍길동',100,100,100,300,100.0,1))


# 홍길동 100 100 100
# 유관순 90  100 90
# 두 정보를 입력을 받아서 출력해보세요.

# 내가 한 것; 선생님 답 확인 위해 주석 처리
# num1 = input("번호를 입력하세요. : ")
# name1 = input("번호 1의 이름을 입력하세요. : ")
# kor1 = int(input("번호 1의 국어 점수를 입력하세요. : "))
# eng1 = int(input("번호 1의 영어 점수를 입력하세요. : "))
# math1 = int(input("번호 1의 수학 점수를 입력하세요. : "))
# ttl1 = kor1+eng1+math1
# avg1 = ttl1/3

# num2 = input("번호를 입력하세요. : ")
# name2 = input("번호 2의 이름을 입력하세요. : ")
# kor2 = int(input("번호 2의 국어 점수를 입력하세요. : "))
# eng2 = int(input("번호 2의 영어 점수를 입력하세요. : "))
# math2 = int(input("번호 2의 수학 점수를 입력하세요. : "))
# ttl2 = kor2+eng2+math2
# avg2 = ttl2/3

# print('번호\t이름\t국어\t영어\t수학\t합계\t평균\t등수')
# print('{}\t{}\t{}\t{}\t{}\t{}\t{:.1f}\t{}'.format(num1,name1,kor1,eng1,math1,ttl1,avg1,1))
# print('{}\t{}\t{}\t{}\t{}\t{}\t{:.1f}\t{}'.format(num2,name2,kor2,eng2,math2,ttl2,avg2,2))

# print('번호\t이름\t국어\t영어\t수학\t합계\t평균\t등수')
# print('{}\t{}\t{}\t{}\t{}\t{}\t{:.1f}\t{}'.format(num1,name1,kor1,eng1,math1,kor1+eng1+math1,(kor1+eng1+math1)/3,1))
# print('{}\t{}\t{}\t{}\t{}\t{}\t{:.1f}\t{}'.format(num2,name2,kor2,eng2,math2,kor2+eng2+math2,(kor2+eng2+math2)/3,2))


# 선생님 힌트
# stu_no1, stu_no2, stu_name1, stu_nname2, kor1, ko2
# eng1, eng2, math1, math2, total1, total2, avg1, avg2
# stu_name1 = input('첫번째 학생이름을 입력하세요. >> ')
# stu_name2 = input('두번째 학생이름을 입력하세요. >> ')

# 선생님 답
stu_name1 = input('첫번째 학생이름을 입력하세요. >> ')
kor1 = int(input("첫번째 학생의 국어 점수를 입력하세요. : "))
eng1 = int(input("첫번째 학생의 영어 점수를 입력하세요. : "))
math1 = int(input("첫번째 학생의 수학 점수를 입력하세요. : "))
total1 = kor1+eng1+math1
avg1 = total1/3
# 출력
print('{}\t{}\t{}\t{}\t{}\t{}\t{:.2f}\t{}'.format(1,stu_name1,kor1,eng1,math1,total1,avg1,1))


stu_name2 = input('두번째 학생이름을 입력하세요. >> ')
kor2 = int(input("두번째 학생의 국어 점수를 입력하세요. : "))
eng2 = int(input("두번째 학생의 영어 점수를 입력하세요. : "))
math2 = int(input("두번째 학생의 수학 점수를 입력하세요. : "))
total2 = kor2+eng2+math2
avg2 = total2/3
# 출력
print('{}\t{}\t{}\t{}\t{}\t{}\t{:.1f}\t{}'.format(2,stu_name2,kor2,eng2,math2,total2,avg2,2))

