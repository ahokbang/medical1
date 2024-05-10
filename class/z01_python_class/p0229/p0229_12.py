
member = []
cnt = 0 # 변수는 밖으로!! 위치!! 
ck = 0
# 이름을 입력 받아서 [[1, 홍길동] [2, 유관순] [3, 이순신]]
while True :
    print('-'*25)
    print('1. 입력')
    print('2. 전체출력')
    print('3. 검색출력')
    print('4. 검색삭제')
    print('5. 수정')
    print('0. 종료')
    ch = input("원하는 번호를 선택하세요. >> ")
    print('-'*25)
    ch = int(ch)
    if ch == 1 :
        print("입력")
        name = input("이름을 입력해주세요. >> ")
        cnt = cnt + 1 # 위치!! 
        m = [cnt, name]
        member.append(m)
    elif ch == 2 :
        print("전체출력")
        print("번호\t이름")
        for i in range(len(member)) :
            # for j in range(len(member[i])) : # 할 필요가 없어!! 
        # print(member)
        # 번호 이름
        # 1    홍길동
        # 2    유관순
            print("{}\t{}" .format(member[i][0],member[i][1] ))
        ''' 선생님 풀이
        print('번호\t이름')
        print('-'*20)
        for i in range(len(member)) :
            print('{}\t{}' .format(member[i][0], member[i][1]))     
        '''
    elif ch == 3 :
        print("검색출력")
        srchName = input("검색할 이름을 입력하세요. >> ")
        # 검색한 이름이 리스트의 어느 위치에 있는지를? enumerate 사용!!
        print("번호\t이름")
        for j, m in enumerate(member) :
            if srchName in m :
                print("{}\t{}" .format(member[j][0], srchName))  
    elif ch == 4 : # ********** 잘 모르겟어 **********
        print("검색삭제")
        delName = input("삭제할 이름을 입력하세요. >> ")
        ck = 0 # 
        for a, m in enumerate(member) : 
            if delName in m :
                del(member[i])
                ck = 1
                print(delName, "학생이 삭제되었습니다.")
        if ck == 0 :
            print("학생이 존재하지 않습니다.")


    elif ch == 5 : # 수정
        print("수정입니다.")
        # 누구의 정보를 수정할지, 누구의 정보를 수정하시겠습니까?
        # 번호, 이름
        # 번호를 수정, 이름을 수정
        # 만약에 번호를 수정한다면, 수정될 값 1 -> 6
        # 만약에 이름을 수정한다면, 홍길동 -> 홍길자
        reName = input("수정하고 싶은 학생의 이름을 입력해주세요. >> ")
        for i, m in enumerate(member) : 
            if reName in m : # 존재한다면
                print(reName, "님을 선택하셨습니다.")
                ch_num = input("수정하고 싶은 항목을 선택하세요.(1번. 번호수정, 2. 이름수정)")
                if ch_num == '1' :
                    print(reName, "님의 번호수정을 선택하셨습니다. ")
                    print(reName, "님의 번호는", member[i][0], "입니다.")
                    stu_num = input("새로운 번호를 입력해주세요. >> ")
                    stu_num = int(stu_num)
                    member[i][0] = stu_num
                    # 수정하는 코드 입력을 받아서 수정하기
                elif ch == '2' :
                    print(reName, '님의 이름수정을 선택하셨습니다.')
                    print(reName, '님의 이름은', member[i][1], '입니다.')
                    stu_name = input("변경할 이름을 입력해주세요. >> ")
                    member[i][1] = stu_name                  
                else : 
                    print("잘못입력하셨습니다.")
                    break
    elif ch == 0 :
        print("종료")
        break
    else :
        print("다시 입력해주세요.")


 
# 선생님 풀이 
# 3. 검색출력
#     elif ch == 3 :
#         searName = input("검색하고 싶은 학생의 이름을 입력해주세요. >> ")
#         print('번호\t이름')
#         for m in member : # m = [1, 홍길동], [2, 유관순], ...
#             if searName in m :
#                 print('{}\t{}' .format(member[i][0], member[i][1]))

# 4. 검색삭제
#     elif ch == 4 : 
#         delName = input("삭제하고 싶은 학생의 이름을 입력해주세요. >> ")
            
#         for i, m in enumerate(member) :
#             if delName in m :
#                 del(memeber[i])
#                 print("{}님이 삭제되었습니다." .format(delName))