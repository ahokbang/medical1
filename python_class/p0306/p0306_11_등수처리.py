
students = [{'stuNo': 'S001', 'name': '홍길동', 'kor': 100, 'eng': 99, 'math': 87, 'total': 286, 'avg': 95.33}, 
            {'stuNo': 'S002', 'name': '유관순', 'kor': 98, 'eng': 93, 'math': 87, 'total': 278, 'avg': 92.67}, 
            {'stuNo': 'S003', 'name': '이순신', 'kor': 88, 'eng': 76, 'math': 30, 'total': 194, 'avg': 64.67}, 
            {'stuNo': 'S004', 'name': '김구', 'kor': 100, 'eng': 100, 'math': 100, 'total': 300, 'avg': 100.0}, 
            {'stuNo': 'S005', 'name': '강감찬', 'kor': 98, 'eng': 85, 'math': 44, 'total': 227, 'avg': 75.67}]


# 등수처리는 합계를 가지고 처리.
for i, s_dic in enumerate(students) : # i 없어도 되지 않나? for s_dic in students로 해도 나와
    rank_cnt = 1 # 등수 처리 변수
    # print(s_dic["total"]) # total 다 출력하기
    for i_dic in students :
        # print(s_dic["total"])
        if s_dic["total"] < i_dic["total"] : # 두 수를 비교
            rank_cnt += 1 # 현재 학생의 합계보다 크면 1 증가
    s_dic["rank"] = rank_cnt

print(students)
    
