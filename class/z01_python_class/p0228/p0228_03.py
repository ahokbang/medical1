member = []

# 입력 : 이름, 점수 (input) ['홍길동', 90]
# 총 3명의 정보를 member 리스트에 넣으세요.
# 출력 : print(member) # [['홍길동', 90], ['유관순', 91], ['이순신', 95]]
# 추가 문제
# 60점 이상이면 홍길동님 불합격입니다. 유관순님 합격입니다.
# member 변수 사용, for, if

for i in range(3) :
    name = input("이름을 입력하세요. >> ")
    score = int(input("점수를 입력하세요. >> "))
    m = [name, score]
    member.append(m)
    if member[i][1] >= 60 :
        print("{}님 합격입니다." .format(member[i][0]))
    else :
        print("{}님 불합격입니다." .format(member[i][0]))
print(member)

''' 선생님 풀이


# 60점 이상이면 홍길동님 불합격입니다. 유관순님 합격입니다.
# member 변수 사용, for, if

# 이름들을 먼저출력해보고
print(member[0][0]) # 홍길동
print(member[1][0]) # 유관순
print(member[2][0]) # 이순신
# 점수들도 출력해보고
print(member[0][1]) # 55
print(member[1][1]) # 80
print(member[2][1]) # 90
print(member) # [['홍길동', 90], ['유관순', 91], ['이순신', 95]]

for i in range(3) : # i = 0, 1, 2
    name = member[i][0]
    score = member[i][1]
    # print("{}님 {}점입니다." . format(name, score))
    # 합격/불합격을 나타내고 싶은거니까
    if score >= 60 :
        print("{}님 합격입니다." .format(name))
    else: 
        print("{}님 불합격입니다." .format(name))

    
'''
