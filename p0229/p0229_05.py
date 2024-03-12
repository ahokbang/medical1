# continue : 반복문에서 남은 문장을 수행하지 않고 다음 단계로 넘어감.

n = 0
while n < 100 :
    n += 1 # n = 1, 2, 3, 4, ..., 100
    if n % 2 == 0 : # 짝수일 때
        continue # skip의 개념, 건너뛰기
    print(n, end=' ')

print()

breakletter = input("중단할 문자를 입력하세요. >> ")
for letter in 'python' :
    if letter == breakletter :
        continue # break, pass 다 넣어봐
    print(letter)

# break는 문자를 만나면 프로그램이 종료되는데(반복문 종료)
# continue 같은 경우는 문자를 건너 띄고 출력이 됨.

# pass : 문법적으로 필요는 하지만 어떤 동작도 원하지 않을 경우 사용
# 즉, 어떤 것도 수행하지 않고 해당 부분을 패스

breakletter = input("중단할 문자를 입력하세요. >> ")
for letter in 'python' :
    if letter == breakletter :
        pass 
    print(letter)  # p \n y \n t \n h \n o \n n 그냥 출력돼