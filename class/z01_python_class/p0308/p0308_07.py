import random
# 연금복권 맞추기. 
# 당첨번호 : 1조 740
# a조 b 일때,
# a : 1 - 9
# b : 0 - 999999

first_num = random.randint(1,9) # a
last_num = random.randint(0,999999) # b

# lotto = "1조740042"
lotto = str(first_num)+"조"+"{:6d}".format(last_num)
print(lotto)
# 예) 1조10 -> 자릿수 맞추기

# 2조 711 입력하면, 7 한개 맞추는 거
l_input = input("복권 번호를 입력하세요(예: 1조111). >> ")
# 비교하는 프로그램을 구현하시오.
# 자리수를 활용하세요.

# for l in lotto : 
#     print(l)

''' 내가 한 거 : 틀림
for i in range(len(lotto)) :
    print(len(lotto[i]))

for m in l_input :
    print(m) 
    
if lotto[i]   :
    pass
'''

cnt = 0

for i in range(len(lotto)) :
    if lotto[i] == l_input[i] :
        cnt += 1
        
print("맞는 개수 : ", cnt-1) # "조"는 항상 맞으니까 -1

'''
당첨번호 : 1조123456
6번째자리 1개 맞으면 1만원
5!6번째자리 2개 맞으면 10만원
4~6번째자리 3개 맞으면 100만원
3~6번째자리 4개 맞으면 1000만원
2~6번째자리 5개 맞으면 1억
1~6번째자리 6개 맞으면 10억
조 + 1~6번째자리 모두 맞으면 100억
'''

# 6번째자리 맞으면 1만원 출력

# for i in range(len(lotto),0, -1) :
#     print(lotto[])

