
# while문과 if문을 사용
# 숫자 2개를 입력 받고(input), 연산자를 입력 받아서(input) (+-*/)
# 계산결과 출력 (if)
# 무한히 계산하는 계산기를 만드는데 (while)
# 첫번째 숫자에 0을 입력하면 프로그램이 종료가 되는 코드를 만드세요. (break)


while True :
    n1 = int(input("숫자를 입력하세요. >> "))
    if n1 == 0 :
        break
    n2 = int(input("숫자를 입력하세요. >> "))
    cal = input("연산자를 입력하세요(+ - * /). >> ")
    if cal == "+" :
        print(n1+n2)
    elif cal == '-' :
        print(n1-n2)
    elif cal == '*' :
        print(n1*n2)
    elif cal == '/' :
        print(n1/n2)
    else :
        print("잘못 입력했습니다. 다시 입력하세요.")


''' 선생님 풀이
while True : # 무조건 참이기 때문에 While 안에 있는 것 계속 반복
    n1 = int(input("첫번째 숫자 입력(종료: 0) >> "))
    if n == 0 :                # 위치 1, 1이나 2에 놓을 수 있어.
        print("종료되었습니다.")
        break
    n2 = int(input("두번째 숫자 입력 >> "))
    cal = input("연산 입력(+ - * /) >> ")
    if cal == '+' :
        print('{}+{}={}' .format(n1, n2, n1+n2))
    elif cal == '-' :
        print('{}-{}={}' .format(n1, n2, n1-n2))
    elif cal == '*' :
        print('{}*{}={}' .format(n1, n2, n1*n2))
    elif cal == '/' :
        print('{}*{}={}' .format(n1, n2, n1/n2))
    else :
        print("연산을 잘못 입력하셨습니다. 다시 입력해주세요. >> ")
    if n == 0 :                # 위치 2
        print("종료되었습니다.")   
        break


'''