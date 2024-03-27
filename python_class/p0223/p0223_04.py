# 중첩 if

a = 97
if a > 90:
    print('a가 90보다 큽니다.')
else:
    print('a가 90보다 작습니다.')
    
if a > 90:
    print('90보다 큽니다.')
    if a < 95:
        print("95보다 작습니다.")
    else:
        print("95보다 큽니다.")
else:
    print("90보다 작습니다.")
    

# 만약 사과의 상태가 good이며 1000원 이하이면 [10개 구매], 1000원보다 비싸면 [3개 구매]를 출력
# 사과의 상태가 'good'이 아니면 [사과를 구매하지 않습니다.]
# and나 or 사용하지 않음

apple = 'good'
price = 500

if apple == 'good':
    if price <= 1000:  # ********** if 다음 절에 바로 if가 와도 돼! **********
        print("사과 10개 구매")
    if price >= 1000:
        print("3개 구매")
else:
    print("사과를 구매하지 않습니다.")


# 선생님 답
if apple == 'good':
    if price <= 1000:
        print("10개 구매")
    else:
        print("3개 구매")
else:
    print('사과를 구매하지 않습니다.')
    
    
    
# 숫자를 하나 입력 받아서 100보다 큰 수면서 짝수면 [짝수], 홀수면 [홀수] 출력
# 100보다 작은 경우 [100보다 작다] 출력

num = int(input("숫자를 하나 입력하세요. : "))  # ********** 계산하니까 int로 바꿔줘야지!!!! **********

if num > 100 :
    if num % 2 == 0 :
        print("짝수")
    else:
        print("홀수")
else:
    print("100보다 작다")
    
# 선생님 답: 동일
