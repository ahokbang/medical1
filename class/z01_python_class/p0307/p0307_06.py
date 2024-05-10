import random

# random.random() :  0에서 1 사이의 실수를 랜덤으로 생성 0.0000000 ~ 0.9999999
print(random.random())

# random.randint() : 정수형 랜덤숫자 생성
# 예) 0 ~ 3까지의 랜덤숫자 생성
print(random.randint(0, 3))

# 1부터 2까지의 랜덤숫자 생성
print(random.randrange(1, 3))

# 리스트의 요소들을 랜덤으로 섞기
list = [ 1, 2, 3, 4, 5, 6, 7 ]
random.shuffle(list)
print(list)

# 리스트에서 1개를 램덤으로 추출
print(random.choice(list))

# 리스트에서 2(해당되는 개수, n)만큼 랜덤으로 추출. 중복 불가능
# print(random.sample(list, n))
print(random.sample(list, 2))


w_list = ["토마토", "바나나", "사과", "배", "수박", "멜론", "복숭아" ]
print(random.sample(w_list, 3))

