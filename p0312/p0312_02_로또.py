# 1. 번호생성
# 2. 번호섞기
# 3. 나의로또번호입력
# 4. 번호확인

import random

lotto = [] # 전체 45개 숫자
lucky_lotto = [] # 당첨번호 6개 숫자
my_lotto = [] # 내가 입력한 6개 숫자

while True :
    print("[ 로또번호 맞추기 프로그램 ]")
    print("1. 번호생성")
    print("2. 번호섞기")
    print("3. 나의로또번호입력")
    print("4. 번호확인")
    print("-"*30)
    choice = int(input("원하는 번호를 입력하세요. >> "))
    
    
    if choice == 1 :
        print("[ 번호생성 ]")
        # for i in range(1, 45+1) :
        #     lotto.append(i)
        # 또는 
        lotto = [i for i in range(1,45+1)]    # 얘가 더 빠르니까 얘 사용
        # print(lotto)
        
    elif choice == 2:
        print("[ 번호섞기 ]")
        random.shuffle(lotto)
        print(lotto)
        
    elif choice == 3:
        print("[ 나의로또번호입력 ]")
        my_num = int(input(f"{i+1}번째 로또번호를 입력하세요. >> "))
        my_lotto.append(my_num)
        print("내가 입력한 번호 : ", my_lotto[i])   
        
    elif choice == 4:
        for i in range(6) :
            lucky_lotto.append(lotto[i])
        print("[ 번호확인 ]")
        print("로또번호 : ", lucky_lotto)
        print("내가 입력한 번호 : ", my_lotto)
        
        
        # 몇개 맞췄는지 확인소스
        
        
        
        # 당첨금액 출력
        
        
