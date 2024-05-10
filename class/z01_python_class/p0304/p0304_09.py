# 학생 삭제

students = [
            [1, "홍길동", 100, 100, 99, 299, 99.67, 1], 
            [2, "유관순", 99, 99, 998, 296, 98.67, 1], 
            [3, "이순신", 80, 80, 81, 241, 80.33, 1],
            [4, '김구', 100, 100, 90, 290, 96.67, 1],
            [5, '강감찬', 90, 70, 50, 210, 70.0, 1]
                                                    ]

while True :
    search = input("삭제하려는 학생의 이름을 입력하세요.")
    
    # 이름 찾기
    cnt = 0 # 반복해서 나오는 걸 막기 위함, 이름을 찾는 위치(찾은 학생의 위치)
    
    # 전체 학생 검색
    for stu in students :
        if stu[1] == search :
            break
            # print("{} 학생을 찾았습니다." .format(search))
            # students.remove(search)
        # else : 
        #     print("{} 학생을 찾을 수 없습니다." .format(search))
        cnt += 1
        
    if cnt == len(students) : # 전체학생 수
        print("{} 학생을 찾을 수 없습니다." .format(search))
    else :
        print("{} 학생을 찾았습니다." .format(search))
        
    print("찾은 위치 : ", cnt)
    del students[cnt]
    print(students)
    print("-"*40)