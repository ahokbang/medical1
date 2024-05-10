# 1. 숫자를 입력 받아서 양수면 양수, 아니면 음수를 출력 if else

n = -10

# 나의 답

n1 = int(input("양수 또는 음수를 입력하세요. : "))

if n1 > 0 :
    print("양수")
else :
    print("음수")
    
# 선생님 답
n = int(input("숫자를 입력하세요. >> "))

if n > 0:
    #print("양수입니다.")
    print('입력하신 숫자 {}는 양수입니다.' .format(n))
else:
    print("음수입니다.")




# 2. 숫자가 0입니다. 0이 아닙니다. if-else

# 나의 답
n2 = int(input("숫자를 입력하세요. : "))

if n2 == 0:  # == 잊지않기!!
    print("숫자가 0입니다.")
else :
    print("숫자가 0이 아닙니다.")
    
# 선생님 답
if n == 0:
    print('0입니다.')
else:
    print('0이 아닙니다.')
