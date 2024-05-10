'''
딕셔너리
- 쌍 2개(키와 밸류)가 하나로 묶인 자료 구조
- 중괄호 사용
'''
students = {"stuNo":1, "stuName":"홍길동", "kor":100}
#              키   밸류    키      밸류     키    밸류
students["eng"] = 100 # 딕셔너리에서의 추가, 없는 키를 넣으면 추가
print(students)
students["kor"] = 50 # 딕셔너리에서의 수정, 있는 키를 넣으면 기존 값이 수정됨
print(students)
del students["stuName"]  # 딕셔너리에서의 삭제
print(students) 
print(students.keys()) # 딕셔너리의 키 값만 추출
print(students.values()) # 딕셔너리의 밸류값만 추출
print(students.items()) # 딕셔너리의 키, 밸류값을 토플 형태로 추출, 
# 토플형태 : 리스트 형태로 추출해주며 수정 및 삭제가 불가능


print(list(students.keys())) # 리스트로 뽑고 싶으면 리스트로 형변환 후 출력 

# 타입(형) 변환 : list, dict, int, float, str ********** 중요 **********

list = [1, 2, 3]
list.append(4) # list에서 추가 방법
print(list)
del list[0] # list에서 삭제 방법,list의 0번째 요소 삭제
print(list)
list[0] = 100 # list에서 수정 방법, list의 0번째 요소를 100으로 수정
list[3] = 1000 # 출력하면 error, 현재 list는 요소가 0, 1, 2까지 밖에 없으므로.


