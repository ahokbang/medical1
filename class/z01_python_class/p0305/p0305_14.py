# 똑같은 수가 몇 번 나왔는지 알고 싶어
import operator

numbers = [1,2,4,6,4,3,6,7,1,3,4,3,4,7,7,7,7,1,1,1,7]
counter = {}
# counter에 넣는 방법: numbers에 1이 2개 있고, 2가 1개 있어
# counter["1"] = 2
# counter["2"] = 1
# print(counter)

# ********** 요 내용 중요해! 외우기! **********
for number in numbers : # ********** 이해 안가 ********** 파이썬 튜터에 넣어서 해봐
    if number not in counter : # counter 딕셔너리에 키 값이 없으면
        counter[number] = 0 # 딕셔너리에 추가
    
    counter[number] += 1 # 딕셔너리 1을 증가
print(counter)

print('-'*50)


# 많이 나온 숫자로 정렬(오름차순)
print(sorted(counter.items(), key=operator.itemgetter(1), reverse=True))
