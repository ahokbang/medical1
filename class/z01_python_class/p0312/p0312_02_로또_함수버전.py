import lotto

lotto = [0]*45 # 전체 45개 숫자
lucky_lotto = [0]*6 # 당첨번호 6개 숫자
my_lotto = [0]*6 # 내가 입력한 6개 숫자
win_num = [] # 당첨된 번호(당첨번호와 내가 입력한 번호 중 일치한 번호)
win_amount = [0,0,1000,10000, 1000000,100000000, 10000000000]


while True : 
    choice = lotto.screen() # 함수호출
    
    if choice == 1 :
        lotto.num_generate(lotto) # 번호생성함수 호출
        print(lotto) # <== print 여기에 있어도 돼

    elif choice == 2:
        lotto.num_shuffle(lotto) # 번호섞기함수 호출
        
    elif choice == 3:
        lotto.num_input(my_lotto) # 나의 로또번호입력
        
    elif choice == 4:
        lotto.num_check(lucky_lotto, my_lotto, win_num, win_amount)
        win_num = [] # 초기화
        
