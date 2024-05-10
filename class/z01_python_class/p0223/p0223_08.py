# 점수를 입력 받아서 90점 이상이면 A, 80점 이상이면 B, 70점 이상이면 C, 나머지는 F를 출력해보세요. (elif)

score = int(input("점수를 입력하세요. >> "))

if score >= 90:
    print("A")
elif score >= 80:
    print("B")
elif score >= 70:
    print("C")
else:
    print("F")
    

# 98 점 이상: A+, 90~93점: A-, B+, B-, C+, C-
if score >= 90:
    if score >= 98:
        print("A+") # 99
    if 90 <= score <= 93: # ********** elif를 써야 98점 이상이 제외돼! **********
        print("A-") # 91
    else:
        print("A") # 95
elif score >= 80:
    if score >= 88:
        print("B+")
    if 80 <= score <= 83: # ********** elif를 써야 98점 이상이 제외돼! **********
        print("B-")
    else:
        print("B")
elif score >= 70:
    if score >= 78:
        print("C+")
    if 70 <= score <= 73: # ********** elif를 써야 98점 이상이 제외돼! **********
        print("C-")
    else:
        print("C")
else:
    print("F")

# 선생님 답
num = int(input("점수를 입력하세요. >> "))

if num >= 90:
    print("90점 이상입니다.")
    if num >= 98:
        print("A+")
    elif num > 93:
        print("A")
    else: 
        print("A-")
elif num >= 80:
    print("80점 이상입니다.")
    if num >= 88:
        print("B+")
    elif num > 83:
        print("B")
    else:
        print("B-")
elif num >= 78:
    print("70점 이상입니다.")
    if num >= 78:
        print("C+")
    elif num > 73:
        print("C")
    else:
        print("C")
else:
    print("F")



if score >= 90:
    if score >= 98:
        print("A+") # 99
    elif 90 <= score <= 93: # ********** elif를 써야 98점 이상이 제외돼! **********
        print("A-") # 91
    else:
        print("A") # 95
elif score >= 80:
    if score >= 88:
        print("B+")
    elif 80 <= score <= 83: # ********** elif를 써야 98점 이상이 제외돼! **********
        print("B-")
    else:
        print("B")
elif score >= 70:
    if score >= 78:
        print("C+")
    elif 70 <= score <= 73: # ********** elif를 써야 98점 이상이 제외돼! **********
        print("C-")
    else:
        print("C")
else:
    print("F")
    