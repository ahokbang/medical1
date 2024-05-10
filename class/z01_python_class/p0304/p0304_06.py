students = [
            [1, "홍길동", 90, 100, 99, 299, 99.97], 
            [2, "유관순", 80, 100, 99, 299, 99.97], 
            [3, "이순신", 100, 100, 99, 299, 99.97] 
                                                   ]

# 찾고자 하는 학생 찾기
while True : # 무한 반복
    # 멈춤
    search = input("검색하고 싶은 학생 이름을 입력하세요(0. 취소).")
    chk = 0 # 찾는 정보 확인
    if search == "0" :
        break # True를 빠져 나오는 break
    for stu in students : # 기존 했던 방법
        if stu [1] == search :
            print("{}의 학생정보를 찾았습니다." .format(search))
        else : 
            print("찾는 학생 정보가 없습니다. ")
        
