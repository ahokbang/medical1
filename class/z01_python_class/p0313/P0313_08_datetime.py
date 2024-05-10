# 한국시가 안나올 경우
from datetime import datetime
from pytz import timezone

now = datetime.now()
print("시간을 포맷에 맞춰 출력하기")
# Y: 년, m : 월, d : 일, H : 시, M : 분, S : 초
# 일자시간의 포맷을 설정하는 함수
output_a = now.strftime("%Y년 %m월 %d일 %H시 %M분 %S초")
output_b = now.strftime("%Y-%m-%d %H:%M:%S")
output_c = now.strftime("%Y-%m-%d")
print(output_a)
print(output_b)
print(output_c)

# print(datetime.now(timezone('Asia/Seoul')))

# import datetime
# from datetime import datetime # ==> 안 써줄 경우에 (2) : now = datetime.datetime.now(0)

# print("현재시각 출력")
# now = datetime.now() # (2)

# print(now.year,"년")
# print(now.month, "월")
# print(now.day, "일")
# print(now.hour, "시")
# print(now.minute, "분")
# print(now.second, "초")
# print()
