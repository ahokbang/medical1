# 조건문
# 1. 키가 130 cm 이상만 놀이기구를 탑승할 수 있다. 
height = 120
# 조건문
if height >= 130:
    print("키가 {}cm로 놀이기구에 탑승할 수 있습니다." .format(height))
else:
    print("키가 {}cm로 놀이기구에 탑승할 수 없습니다." .format(height))


# 선생님 답
if height >= 130:
    print("놀이기구 탑승 가능")
else:
    print("놀이기구 탑승 불가능")

# 2. 나이가 10살 이상이고, 키가 130cm 이상만 놀이기구 탑승 가능
age = 11

if (height >= 130) and (age >= 10):
    print("놀이기구에 탑승할 수 있습니다." .format(height, age))
else:
    print("놀이기구에 탑승할 수 없습니다." .format(height, age))


# 선생님 답
if age >= 10 and height >= 130 : # [놀이기구 탑승 불가능] 출력
    print("놀이기구 탑승 가능")
else:
    print("놀이기구 탑승 불가능")
    

# 3. 비 오면 [우산을 챙겨주세요.] 아니면 [선크림 발라주세요.] 출력
weather = '비'
if weather == '비':
    print("우산을 챙겨주세요.")
else:
    print("선크림을 발라주세요.")
    
    
# 선생님 답: 동일
    
# 4. 비나 눈이 오면 [우산을 챙겨주세요.] 아니면 [선크림 발라주세요.] 출력
if (weather == '비') or (weather == '눈'):
    print("우산을 챙겨주세요.")
else:
    print("선크림을 발라주세요.")
    
    
# 선생님 답: 동일

