import random

# 화면출력함수
def screen() :
    print("[ 로또번호 맞추기 프로그램 ]")
    print("1. 번호생성")
    print("2. 번호섞기")
    print("3. 나의로또번호입력")
    print("4. 번호확인")
    print("-"*30)
    choice = int(input("원하는 번호를 입력하세요. >> "))
    return choice
    
# 번호생성함수 ==> lotto 값을 넘겨 줄 매개변수 필요
def num_generate(lotto) : # <== 그냥 lotto를 넣어주기만 하면 돼
        print("[ 번호생성 ]")
        for i in range(45) :
            lotto[i] = i+1
        print(lotto) # <===  print는 여기에 있어도 되고 번호생성에 있어도 돼.
            
# 번호섞기함수
def num_shuffle(lotto) :
    print("[ 번호섞기 ]")
    random.shuffle(lotto)
    print(lotto)

# 나의로또번호입력 함수
def num_input(my_lotto) :
    print("[ 나의로또번호입력 ]")
    for i in range(6) :
        my_num = int(input(f"{i+1}번째 로또번호를 입력하세요. >> "))
        # my_lotto.append(my_num)
        my_lotto[i] = my_num # 주소값을 그대로 사용해서 넣으니까 리턴 안 써도 돼
    print("내가 입력한 번호 : ", my_lotto)  

# 번호확인함수
def num_check(lucky_lotto, my_lotto, win_num, win_amount) :
    # win_num = []  <== 지역변수로 인식되어서 주소값을 다시 세팅
    for i in range(6) :
        # lucky_lotto.append(lotto[i])
        lucky_lotto[i] = lotto[i]
    print("[ 번호확인 ]")
    print("로또번호 : ", lucky_lotto)
    print("내가 입력한 번호 : ", my_lotto)
    ''' 선생님 풀이
    # 번호확인함수
    def num_check(lotto, lucky_lotto, my_lotto) :
        for i in range(6) :
            lucky_lotto.append(lotto[i])
        print("[ 번호확인 ]")
        print("로또번호 : ", lucky_lotto)
        print("내가 입력한 번호 : ", my_lotto) '''
    # 몇개 맞췄는지 확인소스
    for i in my_lotto : 
        if i in lucky_lotto :
            win_num.append(i)        
    print("당첨된 번호 : " , win_num)
    # 당첨금액 출력
    # print(f"당첨금액 : {win_amount[len(win_num)]} 원")
    print("당첨금액 : {:,d}원" .format(win_amount[len(win_num)]))
        