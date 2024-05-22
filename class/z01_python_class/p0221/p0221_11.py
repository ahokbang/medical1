# 숫자 하나를 입력 받아서 출력해보세요.
# 출력: 입력하신 숫자는 ()입니다.

num = input("숫자를 입력하세요. >> ")
print("입력하신 숫자는 "+num+"입니다.")
print("입력하신 숫자는",num,"입니다.")
print("입력하신 숫자는 {}입니다.".format(num))
print("입력하신 숫자는 %s입니다."%(num))

# 1. 변수 만들어서 출력하기
num = 10
# print("입력하신 숫자는 "+num+"입니다.") : 안돼. 왜냐면 문자형태로 작성해야 하기 때문
# str(num) 사용해서 출력가능

# 2. input으로 입력 받아서 출력
# 내가 푼 거랑 동일, 아래와 같이 다른 방법도 있음
# input은 무조건 문자열로 인식하므로 + 사용 가능
# print("입력하신 숫자는 ", int(num) , "입니다.")
# 아니면 num = int(num)으로 형변환 가능. num은 문자니까 숫자형으로 바꾸고 싶을 때 int 사용
# 아니면 num = int(input("숫자를 입력하세요. >> "))