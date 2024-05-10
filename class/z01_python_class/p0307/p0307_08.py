import random

fruit = {"peach" : "복숭아", "orange" : "오렌지", "apple" : '사과', "pear" : "배", 
         "grape" : "포도", "mango" : '망고', "kiwi" :"키위"}

'''
# fruit 밸류값 = 변수에다가 키 값을 넣어주면 밸류값이 나와.
print(fruit['peach'])
print(fruit['kiwi'])

f_list = ["peach", "pear", "kiwi"]

print(fruit[f_list[0]])

for f in f_list :
    print(fruit[f])

'''

# 키 값 랜덤으로 돌리기
# 랜덤은 리스트 형식이므로 딕셔너리를 리스트로 바꿔주어야 해!
# 딕셔너리는 키 값으로, 리스트는 주소값으로 데이터/값/value을 찾아.

f_list = list(fruit.keys())
print(f_list)

f_list_ran = random.sample(f_list, 4)
print("랜덤추출 : ", end = ' : ')
for f in f_list_ran :
    print(fruit[f], end = ",")
    