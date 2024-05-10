# 변수사용
# 변수 bool, int, float, srt 형이 있다.
# 변수는 대소문자를 구분한다. 대문자는 주로 클래스에서 사용
myVar = 10
MyVar = 20
# 변수는 언더바를 포함할 수 있고, 숫자로 시작하면 안된다.
number1 = 10
my_number = 20
# 1number = 20 : 오류 발생

# 변수는 예약어를 사용할 수 없다. 예약어: 파이썬에서 이미 지정한 언어
#if = 100 # 색이 달라짐(빨간색) -> 에러
#True = 100 # 색이 달라짐(파란색)

# 변수는 마지막으로 입력된 값을 저장한다. 
a = 10
a = 30
print(a) # a는 30으로 출력

a = 1
b = 2
c = 3
print(1+2+3)
print(a+b+c)

var2 = 200
var1 = var2 + 100
print(var1, var2)

a = 1
b = 2
a, b = 1, 2 # , 사용해서 출력 가능

# 입력 받기
#input() # 괄호가 있으니까 input도 파이썬에서 제공하는 입력을 받기 위한 함수
# name = input("당신의 이름을 입력하세요. : ")
# print('당신의 이름은 '+name+'입니다.')

# # input()은 문자열로 입력이 된다.
# age = input("나이를 입력하세요. : ")
# print('당신은 내년에 {}살입니다.' .format(age)+1) # age는 문자열로 숫자로 바꿔주어야 해

# 숫자로 바꿔주기
# 1. age = int(input("나이를 입력하세요. "))
# 2. age = int(age)
# 3. print('당신은 내년에 {}살입니다.' .format(int(age)+1))

# 연습문제
# 숫자 하나를 입력 받아서 구구단을 출력해보세요.
# 2를 입력 받으면 
# 2 * 1 = 2
# 2 * 2 = 4
# 2 * 3 = 6

# 문자열로 출력해보기
print("2 * 1 = 2\n2 * 2 = 4\n2 * 3 = 6")

# 변수를 만들어서 출력
num = 2
print(num,"* 1 =",num*1)
print(num,"* 2 =",num*2)
print(num,"* 3 =",num*3)

# 입력을 받아서 출력
num = int(input("숫자 2를 입력하세요. : "))

print(num, "* 1 = {}" .format((num)*1))
print(num, "* 2 = {}" .format((num)*2))
print(num, "* 3 = {}" .format((num)*3))

#print(num, "* 1 = {}" .format((num)*1), \n num, {} \n {}" .format((num)*1,(num)*2,(num)*3))



