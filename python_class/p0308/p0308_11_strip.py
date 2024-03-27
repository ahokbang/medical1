# strip() : 입력할 때 공백제거
s1 = " 파이썬"
s2 = "파이썬"

if s1.strip() == s2 :
    print("맞습니다.")
else :
    print("틀립니다.")

print(s1.lstrip()) # 왼쪽공백만 제거
print(s1.rstrip()) # 오른쪽공백만 제거
print(s1.strip()) # 양쪽공백 제거

s_input = input("지금 배우는 과목을 입력하세요. >> ")

if s_input == s2 :
    print("정답입니다.")
else :
    print("오답입니다.")
    


s_input = input("지금 배우는 과목을 입력하세요. >> ").strip # 추가하면 입력 시 공백(space)이 추가되어도 돼

# 단, 공백제거는 양쪽만 가능. 파이   썬의 경우에는 공백제거 안돼
s3 = "       파이   썬       "

# replace : 문자열을 다른 문자열로 대체
print(s3.replace("파" , "자")) # '파'를 '자'로 바꿔서 [자이썬]으로 출력
ss = "apple은 당도가 높고, apple의 생상은 빨강, 녹색이 있습니다."
# ctrl + F 하면 나와
print(ss.replace("apple", "사과"))
print(s3.replace(" ", "")) # " " (띄어쓰기 있음)을 "" (띄어쓰기 없음)으로 바꿔줌.
# 자바, C 에도 똑같아.

news = "정용진 신세계그룹 총괄부회장이 8일 회장 자리에 올랐다. 2006년 부회장에 오른 후 18년 만에 이뤄진 승진 인사다. \
       지난해 이마트 창립 이후 적자를 기록했고, 신세계그룹 매출이 감소하는 등 사업 환경이 악화하면서 위기 극복을 위한 새로운 리더십을 내세웠다."
# 빈문자 제거 
print(news.replace(" ", ""))

# 그룹 -> group 변경
print(news.replace("그룹", "group"))
# 얘네들은 비파괴. 그래서 앞에 빈문자 제거한 게 그룹 변경한 거에 반영이 안되어 있어.
