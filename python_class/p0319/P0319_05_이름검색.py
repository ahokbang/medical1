# 검색어가 포함이 되어 있어도 검색하는 방법
name = ["홍길동", "유관순", "이순신", "김구", "강감찬", "홍길순", "홍길자"]


while True : 
    search = input("이름을 입력하세요. >> ")
    search_list = [] # 찾은 사람의 위치 저장
    cnt = 0
    # 검색어로 검색
    for n in name :
        if n.find(search) != -1 : # 검색어가 포함이 되어 있는지 확인 
            # -1은 없냐라는 뜻인데 != 에서 !(not)이 붙어서 있냐라는 의미가 돼
            # print("찾는 사람이 있습니다. name 리스트 위치 : ", cnt)
        # if search in n : # 검색어가 포함이 되어 있는지 확인 <== 요걸로 써도 돼
            search_list.append(cnt)
        cnt += 1
    # 검색된 사람들 출력
    if len(search_list) == 0 : # 찾는 사람이 없음
        print("찾는 사람이 없습니다.")
    else :
        print(f"{search}(으)로 검색된 사람 : ", end=' ')
        for i in search_list :
            print(name[i],end=' ')
        print()
        print()



'''
정확한 이름으로 찾는 방법 
name = ["홍길동", "유관순", "이순신", "김구", "강감찬", "홍길순", "홍길자"]

while True : 
    search = input("이름을 입력하세요. >> ")
    cnt = 0
    for n in name :
        if search == n :
            print("찾는 사람이 있습니다. name 리스트 위치 : ", cnt)
            break
        cnt += 1

    if cnt >= len(name) :
        print("찾는 사람이 없습니다.")
'''