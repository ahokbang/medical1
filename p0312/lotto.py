# ********** 여기에 함수 부분만 들어가는지 선생님 파일 확인 필요 **********

# 1. 번호생성
# 2. 번호섞기
# 3. 나의로또번호입력
# 4. 번호확인

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
        # lotto = [i for i in range(1,45+1)]    # 얘가 더 빠르니까 얘 사용
        # print(lotto) # print가 여기에 있어서 로또번호 생성된걸로 출력되지만, 번호섞기, 번호 확인 안됨.
        # 선생님은 위 방법으로 했을 때 [] 이렇게 출력 됨. 그래서 아래 방법 알려주심.
        # 위 방법으로 했을 때, 번호섞기, 번호확인 안돼. 지역변수로 변환되어 새롭게 재정의 되었기 때문.
        # for i in range(45) :
        #     lotto.append(i+1)
        
        # lotto = [0*45]로 해주고 아래와 같이 하면 나와.
        for i in range(45) :
            lotto[i] = i+1
            # print(lotto) # <===  print는 여기에 있어도 되고 번호생성에 있어도 돼.
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
        

# ----------------------------------------------
# apped로 하면 무한대로 들어가니까 리턴을 들어가야하는데 리턴을 안 쓰려면 리스트 값을 아예 지정해줘

lotto = [0]*45 # 전체 45개 숫자
lucky_lotto = [0]*6 # 당첨번호 6개 숫자
my_lotto = [0]*6 # 내가 입력한 6개 숫자
win_num = [] # 당첨된 번호(당첨번호와 내가 입력한 번호 중 일치한 번호)
# 초기화 안 시키면 누적돼
win_amount = [0,0,1000,10000, 1000000,100000000, 10000000000]


while True : 
    choice = screen() # 함수호출
    
    if choice == 1 :
        num_generate(lotto) # 번호생성함수 호출
        print(lotto) # <== print 여기에 있어도 돼

    elif choice == 2:
        num_shuffle(lotto) # 번호섞기함수 호출
        
    elif choice == 3:
        num_input(my_lotto) # 나의 로또번호입력
        
    elif choice == 4:
        num_check(lucky_lotto, my_lotto, win_num, win_amount)
        win_num = [] # 초기화
        ''' 선생님 풀이
        num_check(lotto, lucky_lotto, my_lotto) '''
        
    # 몇개 맞췄는지 확인소스
        
        
        
    # 당첨금액 출력
        
        
