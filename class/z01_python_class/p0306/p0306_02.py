# 딕셔너리의 정렬
# 딕셔너리.items() : 출력하면 튜플 형태로 출력

import operator

fruit = [ '바나나', '바나나', 
            '바나나', '딸기', '배', '사과', '딸기',
            '딸기', '딸기', '딸기', '사과', '바나나', '바나나',
            '바나나', '딸기', '배', '사과', '딸기',
            '딸기', '딸기', '딸기', '사과' ]

counter = {}  # 딕셔너리 생성
cnt = 0

for f in fruit :
    # counter[f] = 0 # e두번째 바나나가 들어오면 수정이 돼
    # counter[f] += 1 # 1을 추가하고 싶어. 근데 이렇게 되면 문제가 생겨
    # 그래서 아래와 같이 코드를 짜야해
    if f not in counter : # 딕셔너리에 키가 존재하는지 확인
        counter[f] = 0 # 딕셔너리 키가 없을 때 키 추가
    counter[f] += 1    # 키의 value값 1 증가
print(counter)

print(type(counter.keys())) # counter.keys는 class type
print(counter.values())
print(counter.items())

# 딕셔너리 정렬 - key순, 순차정렬
print(sorted(counter.items(), key=operator.itemgetter(0)))
#            토플이라는 형태로 분리 => (counter.items())
# 딕셔너리 정렬 - key순, 역순정렬
print(sorted(counter.items(), key=operator.itemgetter(0), reverse=True))
# 딕셔너리 정렬 - value순, 순차정렬
print(sorted(counter.items(), key=operator.itemgetter(1)))
# 딕셔너리 정렬 - value순, 역순정렬
print(sorted(counter.items(), key=operator.itemgetter(1), reverse=True))
