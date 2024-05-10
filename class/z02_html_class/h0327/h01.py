# ********** 매우 중요! 이 정도는 그림을 그릴 수 있어야 해! 무조건 외워! ********** # 
while True:
    print("[ 로그인 ]")
    print('-'*20)
    id = input("ID : ")
    pw = input("PW : ")
    print('-'*20)
    
    # 파일에서 ID와 PW 확인 
    # ==> 지금은 파일이랑 연결했지만, 나중에 데이터베이스에서 확인하고 웹으로 만들거야.
    chk = 0
    with open("member.csv", "r", encoding='utf8') as f:
        while True:
            str = f.readline()
            if str == "" : break
            str = str.strip()
            mem = str.split(',')
            # ID, PW 비교
            if id == mem[1] and pw == mem[2] :
                chk = 1
                break            
    # ID, PW가 없으면 chk == 0, ID, PW가 있으면 chk == 1        
    if chk == 1:
        print("로그인이 되었습니다.")
        break
    else :
        print("ID 또는 PW가 일치하지 않습니다. 다시 입력하세요.")
        
while True:
    print("[ 학생성적 프로그램 ]")
    print('-'*30)
    print('1. 학생성적입력')
    print('0. 종료')
    print('-'*30)
    choice = int(input("원하는 번호를 입력하세요. >> "))
    
    if choice == 1 :
        print("학생성적입력을 진행합니다.")
    elif choice == 0 :
        print("프로그램을 종료합니다. ")
        break
