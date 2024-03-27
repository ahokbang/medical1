stu = [
        ['홍길동', 100], ['유관순', 98], ['이순신', 100], ['김구', 50], 
        ['강감찬', 99], ['김유신', 90], ['홍길순', 80], ['홍길자', 70]
]

# 이름으로 검색, 홍이 들어가는 사람을 모두 검색해서 출력하시오. 
# 이름으로 검색, 신이 들어가는 사람을 모두 검색해서 출력하시오. 

while True :
    print("[ 학생성적 검색 ]")
    print('1. 이름으로 검색')
    print('2. 점수 검색')
    choice = int(input('원하는 번호를 입력하세요. >> '))
    
    if choice == 1 :
        search = input("원하는 이름을 검색하세요. >> ")
        search_list = []
        cnt = 0 
        # 검색어로 검색
        for s in stu :
            if s[0].find(search) != -1 :
            # if search in s[0] :
                # print("찾는 사람이 있습니다. name 리스트 위치: ", cnt)
                search_list.append(cnt)
            cnt += 1
            
        if len(search_list) == 0 :
            print("찾는 사람이 없습니다.")
        else :
            print(f"{search}(으)로 검색된 사람 : ", end=' ')
            for i in search_list:
                print(stu[i][0], end=" ")
            print()
            print()
    elif choice == 2 :
        score = int(input('몇 점 이상을 검색하시겠습니까? >> '))
        # 80 => 80점 이상인 사람의 이름이 출력되도록 해보세요.
        score_list = []
        cnt = 0
        # 검색어로 검색
        for s in stu :
            if s[1] >= score :
                print()
                search_list.append(cnt)
            cnt += 1
        # 검색된 사람들 출력
        if len(search_list) == 0 :
            print(f"{score}점 보다 큰 점수는 없습니다.")
        else :
            print(f"{score}점 이상 : ")
            for i in search_list :
                print(stu[i][0],":", stu[i][1])
            print()
            print()
 
            
            
        