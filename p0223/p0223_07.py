# 해보세요.
cal = input("수식을 입력하세요.(+,-,*,/) >> ") # 문자
n1 = 24
n2 = 5

if cal == '+': # ********** 사칙 연산은 문자니까 '' 작성해줘야 해! **********
    print(n1+n2)
elif cal == '-':
    print(n1-n2)
elif cal == '*':
    print(n1*n2)
elif cal == '/':
    print(n1/n2)
else:
    print("다시 입력하세요.")
    
# 위의 코드로 사칙연산 가능한 계산기를 만들 수 있어.

# 선생님 답: 동일
'''
else: 
    print("수식을 잘못 입력하셨습니다. 다시 입력해주세요.")
'''
