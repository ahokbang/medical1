import random

fruit = {"peach" : "복숭아", "orange" : "오렌지", "apple" : '사과', "pear" : "배", 
         "grape" : "포도", "mango" : '망고', "kiwi" :"키위"}

print("개수 : ", len(fruit))
# 랜덤으로 4개를 출력 - 랜덤으로 4개 추출
# 랜덤은 리스트
# key를 리스트 타입으로 변경
print(fruit.keys()) # 딕셔너리에서 key값 추출
print(random.sample(list(fruit.keys()), 4))
print()
# 4개의 랜덤 key를 출력하시오.
f_list = random.sample(list(fruit.keys()), 4)

f_list2 = ["kiwi", "grape", "peach", "pear"]

print(fruit[f_list2[0]])

print()
# value 값 전체 출력
for key in fruit :
    print(fruit[key])