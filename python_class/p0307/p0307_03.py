students = {"stuNo" : 1, "stuName" : "홍길동", "tel" : "010-0000-0000",
            "gender" : "male", "id" : "aaa", "pw" : 1111}

# nickname : 길동스

students["stuNo"] = students["stuNo"] + 1
print(students["stuNo"]) # 2가 출력 
print(students["studentNo"]) # error 없는 키
# 키 값이 없는 데이터를 가져오려고 할 때는 에러
# - 키가 있는지 없는지 확인 필요
if "studentNo" in students :
    print("key가 있습니다.")
    students["studentNo"] = students["student"] + 1
    print(students["studentNo"])
else : 
    print("key가 없습니다.")