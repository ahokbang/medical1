# 딕셔너리의 정렬
# 딕셔너리.items() : 출력하면 튜플 형태로 출력

import operator

fruit = [ '바나나', '바나나', 
            '바나나', '딸기', '배', '사과', '딸기',
            '딸기', '딸기', '딸기', '사과', '바나나', '바나나',
            '바나나', '딸기', '배', '사과', '딸기',
            '딸기', '딸기', '딸기', '사과' ]

counter = {}  # 딕셔너리 생성

# 딕셔너리 추가
counter["바나나"] = 4
# 딕셔너리 수정
counter["바나나"] = 1
counter["복숭아"] = 5
# print(counter["딸기"]) # 카운터(딕셔너리)에 없는 키 값을 출력하면 error
print(counter["바나나"])

if "딸기" not in counter : # 키가 존재하는지 확인
    counter["딸기"] = 0 # 카운터에 없는 키 값을 생성
else :
    print(counter["딸기"]) # 키의 value값을 출력

'''
변수 : 1개 값 저장 타입
리스트 : 복수의 값 저장 타입
딕셔너리 : 복수개를 저장 타입(key, value 형태로 저장), 제일 많이 사용하는 타입
토플 : 딕셔너리와 동일하나 수정이나 삭제가 불가능
'''

print(counter)

# 딕셔너리 삭제
del counter["복숭아"] 
print(counter)

print(type(counter.keys())) # counter.keys는 class type
print(counter.keys())
print(counter.values())
print(counter.items())

# 리스트 정렬 방법
a_list = [3, 5, 7, 4, 1, 2, 6]
print(sorted(a_list)) # 또는
print(a_list.sort()) 