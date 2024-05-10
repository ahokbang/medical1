# 해보세요.
# 성별, 키를 입력 받아서
# 남자일 경우 (m) 172.5 이상이면 [평균 이상] 이하면 [평균 이하]
# 여자일 경우 (f) 159.6 이상이면 [평균 이상] 이하면 [평균 이하]
# 그외는 [잘못입력하셨습니다.] 라고 출력해보세요.

gender = input("성별을 입력하세요.(m / f) >> ")
height = float(input("키를 입력하세요. >> ")) 
# ********** 키는 소수점으로 표현하니까 float 변환!! 숫자만이 부등호로 계산되잖아!! **********

if gender == "m" : # ********** m은 문자니까 '' 필요해! **********
    if height >= 172.5 :
        print("평균 이상")
    else :
        print("평균 이하")
elif gender == "f" :
    if height >= 159.6 :
        print("평균 이상")
    else :
        print("평균 이하")
else:
    print("잘못 입력하셨습니다.") # ********** 성별을 잘못 입력했을 때만, 키는 아니야 **********

# 선생님 답
# 성별 먼저 보면,
if gender == 'm' : # 대문자 M도 쓰고 싶을 경우 : if gender == 'm' or gender == 'M'
    print("남자")
    # 남자일 경우만
    if height >= 172.5 :
        print("평균 이상입니다.")
    else :
        print("평균 이하입니다.")
elif gender == 'f' :
    print("여자")  
    if height >= 159.6 :
        print("평균 이상입니다.")
    else :
        print("평균 이하입니다.")
else:
    print("잘못입력하셨습니다.")