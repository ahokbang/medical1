# import random

from random import choice # ==> 이렇게하면 random 모듈명을 안붙여도 됨. print(random())과 같이

# 0.0000000 - 0.9999999 랜덤으로 float 결과값 리턴
print(random())
# 10과 20사이의 랜덤 float 결과값 리턴
# print(random.uniform(10,20))
# 1에서부터 (3-1, 2)까지의 랜덤 숫자 리턴
# print(random.randrange(1, 3))

# 리스트 내에 랜덤 선택(1개)
# print(random.choice([1,2,3,4,5]))
# 리스트의 요소를 랜덤으로 섞음
# a_list = [1,2,3,4,5]
# random.shuffle(a_list) # 출력을 하는 것이 아니라, a_list 결과를 저장시켜 줌
# print(a_list)
# 랜덤으로 k갯수 만큼 선택, 단 리스트 개수 (요소의 크기)보다 k가 크면 에러
# print(random.sample([1,2,3,4,5], k=2))

# 1-10 범위(10 포함) 내랜덤 int를 1게 선택
# print(random.randint(1,10))


# import math
# print(math.sin(1))
# print(math.cos(1))
# print(math.tan(1))
