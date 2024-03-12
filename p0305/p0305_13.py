import operator

foods = {"떡볶이" : '오뎅', '짜장면' : '단무지', '라면' : '김치', "피자" : '피클', 
         '맥주' : '땅콩', '삼겹살' : '상추'}

# 키의 값을 출력하시오. 
print(foods.keys()) 

''' 선생님 풀이
방법 1. 
print(foods.keys())
방법 2. 
for key in foods :
    print(key, end="\t")
'''
# 키 값으로 정렬하시오.
print(sorted(foods.items(), key=operator.itemgetter(0)))

# Value 값을 출력하시오.
print(foods.values())
''' 선생님 풀이
방법 1. 
print(foods.values())
방법 2. 
for key in foods :
    print(food[key], end="\t")
'''  
# key:value 형태로 모두 출력하시오.
print(foods)
''' 선생님 풀이 ********** 다시 풀어보기 *********
for key in foods :
    print(f"{key} : {foods[key]}")
'''