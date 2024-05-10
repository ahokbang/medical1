# 국어, 영어, 수학 점수를 입력 받아서 평균을 출력하세요.
# 출력: 평균은 : 95점 입니다.
# 변수: kor, eng, math

# 변수 선언해서 출력
# kor = 100, eng = 90, math = 80

# 3가지 점수를 입력 받아서 출력

kor = input("국어 점수를 입력하세요. >> ")
kor = int(kor)

eng = int(input("영어 점수를 입력하세요. >> "))
math = int(input("수학 점수를 입력하세요. >> "))

avrg = (kor+eng+math)/3

print("평균은 : {}점 입니다." .format((kor+eng+math)/3))
print("평균은 : {}점 입니다." .format(avrg))

# 선생님 답

# 변수 선언해서 출력
kor = 100
eng = 100
math = 100
avg = (kor+eng+math)/3
print("평균은 : {}점 입니다.".format(avg))

# 3가지 점수를 입력 받아서 출력
kor = input("국어점수: ")
eng = input("영어점수: ")
math = input("수학점수: ")

kor = int(kor)
eng = int(eng)
math = int(math)
print("평균은 : {}점 입니다.".format(avg))