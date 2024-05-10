
# 내일 할 거
# ...
# 변수명 : stu_no, stu_name, kor, eng, math, total, avg, rank
# 출력:
# 번호    이름    국어    영어    수학    합계    평균    등수
#   1    홍길동   100     100     100     300   100.00    1
# ...
   
print("변수명: stu_no, stu_name, kor, eng, math, total, avg, rank")
print("출력: ")
print("번호 이름  국어  영어  수학  합계  평균  등수")
print(" 1 홍길동  100   100   100   300  100.00  1")

# 변수 지정
번호 = 1
이름 = "홍길동"
국어 = 100
영어 = 100
수학 = 100
합계 = 300
평균 = 100.00
등수 = 1

print("변수명: stu_no, stu_name, kor, eng, math, total, avg, rank")
print("출력: ")
print("번호 이름  국어  영어  수학  합계  평균  등수")
print("{}   {}  {}   {}   {}   {}  {}  {}" .format(번호, 이름, 국어, 영어, 수학, 합계, 평균, 등수))

# input 사용
번호 = input("번호를 입력하세요. >> ")
이름 = input("이름을 입력하세요. >> ")
국어 = int(input("국어 점수를 입력하세요. >> "))
영어 = int(input("영어 점수를 입력하세요. >> "))
수학 = int(input("수학 점수를 입력하세요. >> "))
합계 = int(국어)+int(영어)+int(수학)
평균 = (int(국어)+int(영어)+int(수학))/3
등수 = 1

print("{}  {}  {}  {}  {}  {}  {}  1" .format(번호, 이름, 국어, 영어, 수학, 국어+영어+수학, (국어+영어+수학)/3, 등수))

