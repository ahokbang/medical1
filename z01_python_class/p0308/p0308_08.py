import random
first_num = random.randint(1,9) # a
last_num = random.randint(0,999999) # b

# lotto = "1조740042"
lotto = str(first_num)+"조"+"{:6d}".format(last_num)
print(lotto)


a = "123456"
b = "777456"
cnt = 0
# for i in range(len(a),0,-1) :
#     print(a[i-1])
   
# for i in range(len(a)) :
#     print(a[len(a)-1-i])
    
# 6번째자리가 맞으면 1만원
# 5,6번째자리 10만원
# 4,5,6번째자리 100만원
# 3456번째자리 1000만원
# 23456번째자리 1억원
# 123456번째자리 10억
# 1조 100억원

for i in range(len(a), 0, -1) :
    if a[i-1] != b[i-1] :
        break
    else :
        cnt += 1 # 맞는 횟수 1 증가
if cnt == 0 :
    print("완전 꽝입니다.")
elif cnt == 1:
    print("6번째 자리가 맞았습니다. 당첨금액 : 1만원")
elif cnt == 2:
    print("5, 6번째 자리가 맞았습니다. 당첨금액 : 10만원")
elif cnt == 3:
    print("4, 5, 6번째 자리가 맞았습니다. 당첨금액 : 100만원")
elif cnt == 4:
    print("3, 4, 5, 6번째 자리가 맞았습니다. 당첨금액 : 1000만원")
elif cnt == 5:
    print("2, 3, 4, 5, 6번째 자리가 맞았습니다. 당첨금액 : 1억원")
elif cnt == 6:
    print("1, 2, 3, 4, 5, 6번째 자리가 맞았습니다. 당첨금액 : 10억원")

# 조까지 들어간다면,
a = "1조123456"
#     12345678   8자리숫자이고, 뒤에서부터 앞으로 가니까 조의 자리수는 2
b = "9조777456"
cnt = 0

for i in range(len(a), 0, -1) :
    if i == 2 : continue # 조는 무조건 맞으니까 넘어가
    if a[i-1] != b[i-1] :
        break
    else :
        cnt += 1 # 맞는 횟수 1 증가
if cnt == 0 :
    print("완전 꽝입니다.")
elif cnt == 1:
    print("6번째 자리가 맞았습니다. 당첨금액 : 1만원")
elif cnt == 2:
    print("5, 6번째 자리가 맞았습니다. 당첨금액 : 10만원")
elif cnt == 3:
    print("4, 5, 6번째 자리가 맞았습니다. 당첨금액 : 100만원")
elif cnt == 4:
    print("3, 4, 5, 6번째 자리가 맞았습니다. 당첨금액 : 1000만원")
elif cnt == 5:
    print("2, 3, 4, 5, 6번째 자리가 맞았습니다. 당첨금액 : 1억원")
elif cnt == 6:
    print("1, 2, 3, 4, 5, 6번째 자리가 맞았습니다. 당첨금액 : 10억원")
elif cnt == 7:
    print("1, 2, 3, 4, 5, 6번째 자리가 맞았습니다. 당첨금액 : 10억원")

# 조까지 들어간다면,