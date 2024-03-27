import datetime
now = datetime.datetime.now() # 현재를 가져옴
print(now)
# 2024-02-23 13:03:25.451676
month = now.month # 현재 월
# 현재가 봄, 여름, 가을, 겨울 중 언제인지?"
# 12, 1, 2: 겨울, 3, 4, 5: 봄, 6, 7, 8: 여름, 9, 10, 11: 가을
# elif 사용

# 내가 푼 거 1
if 1 <= month <= 2 or month == 12:
    print("현재는 겨울입니다.")
elif 3 <= month <= 5:
    print("현재는 봄입니다.")
elif 6 <= month <= 8:
    print("현재는 여름입니다.")
else:
    print("현재는 가을입니다.")
    
# 내가 푼 거 2
# 3, 4, 5: 봄, 6, 7, 8: 여름, 9, 10, 11: 가을, 12, 1, 2: 겨울
if 3 <= month <= 5:
    print("현재는 봄입니다.")
elif 6 <= month <= 8:
    print("현재는 여름입니다.")
elif 9 <= month <= 11:
    print("현재는 가을입니다.")
else:
    print("현재는 겨울입니다.")
    

# 선생님 답: 내가 푼거 2번 또는 아래와 같이 풀이
if (month == 3) or (month == 4) or (month == 5): # 이런 식으로도 가능
    print("현재는 봄입니다.")
elif (month == 6) or (month == 7) or (month == 8):
    print("현재는 여름입니다.")
elif (month == 9) or (month == 10) or (month == 11):
    print("현재는 가을입니다.")
else:
    print("현재는 겨울입니다.")
    