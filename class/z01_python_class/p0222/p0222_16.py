import datetime # 날짜 관련 기능을 가져옴
now = datetime.datetime.now() # 오늘 날짜 시분초 가져옴

# print(now) # 2024-02-22 17:06:53.323195
# print(now.year) # 연도
# print(now.month) # 월
# print(now.day) #일

# print(now.hour)
# print(now.minute)
# print(now.second)

# year = now.year

# 연습 문제 1
# 시간을 사용해서 지금이 오전이면, [오전입니다.] 오후면 [오후입니다.] 출력
# [현재는 17시로 오후입니다.]

import datetime
now = datetime.datetime.now()
hour = now.hour

if now.hour < 12:
    print("오전입니다.")
else: 
    print("현재는 {}시로 오후입니다." .format(hour))

# 선생님 답
h = now.hour # 시간
# 오전
if h < 12:
    print("현재는 {}시로 오전입니다." .format(h))
else:
    print("현재는 {}시로 오후입니다." .format(h))
    

# 연습 문제 2
# 짝수 달입니다. 홀수 달입니다.
m = now.month

if m%2 == 0 :
    print("현재는 {}월로 짝수 달입니다." .format(m))
else:
    print("현재는 {}월로 홀수 달입니다." .format(m))

# 선생님 답 동일


# 연습 문제 3
# 월
# 겨울입니다. 겨울이 아닙니다.

# 내 정답
if (m == 12) or (1 <= m <= 2):
    print("지금은 겨울입니다.")
else:
    print("지금은 겨울이 아닙니다.")

# 선생님 정답
if 3 <= m <= 11:
    print("지금은 {}월로 겨울이 아닙니다." .format(m))
else:
   print("지금은 {}월로 겨울입니다." .format(m))

# **type 알아보는 방법**
print(type(m)) # <class 'int'>
