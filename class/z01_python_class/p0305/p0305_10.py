''' 딕셔너리 
학번 1000
이름 홍길동
학과 컴퓨터공학
'''
student = {"학번" : 1000, "이름" : "홍길동", "학과" : "컴퓨터공학"}
# key값 for문으로 뽑아올 수 있어
for key in student :
    # print(key)
    print("{} : {}".format(key, student[key]))

print("-"*50)

# print(student)

# 연락처 010-1111-1111 추가
student["연락처"] = "010-1111-1111"
print(student)

# 수정 : 수정과 추가 방법이 동일해, 값이 있으면 수정 없으면 추가
student["이름"] = "유관순"
print(student)

# 학과를 화학과로 수정
student["학과"] = "화학"
print(student)

# key의 value 값 출력하는 방법
print(student.get("이름"))
print(student["이름"])

# 문제점
# print(student["성별"]) # key값이 없는 것을 출력하면 에러 발생 
print(student.get("성별")) # 에러가 발생하지 않으며, None으로 표시

if "이름" in student:
    print("이름 키값이 있습니다.")
    print("이름 : ", student["이름"])
else :
    print("이름 키값이 없습니다.")
    

if "성별" in student :
    print("성별 키값이 있습니다.")
    print(student["성별"]) # 에러, 프로그램이 중간에 멈춤. 실제 현장에서 프로그램일 경우에는 패널티
else : 
    print("성별 키값이 없습니다.")
    
'''
출력방법
1. 
student(["이름"])
2.
student.get("이름")
'''
# student.keys() : 딕셔너리의 모든 key를 출력
print(student.keys()) # 딕셔너리 키즈의 괄호 안의 내부가 list 타입으로 출력
print(type(student.keys())) # type : class
print(list(student.keys())) # 이렇게 해야 list 타입이 돼. list로 형 변환 방법
for i in student.keys() : # for문으로도 출력할 수 있어
    print(i)
print('-'*50)

# student.values() : 딕셔너리의 모든 value를 출력
print(student.values()) # type : class
print(list(student.values()))
for i in student.values() : # for문으로도 출력 가능
    print(i)

# items() 튜플 형태로 데이터를 리턴
print(student.items()) 
# 튜플 : 딕셔너리와 똑같은데 괄호가 쳐져 있어. 수정(삭제 포함) 불가. 키와 밸류의 한 쌍으로 이루어져 있어.

# 딕셔너리 안에 해당 키가 있는지 없는지를 in을 사용해 확인. 있다면 True를 반환, 없다면 False를 반환
if '이름' in student :
    print("키값이 있습니다.")
else : 
    print("키값이 없습니다.")