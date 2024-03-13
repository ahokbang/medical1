import random

# 카드 종류 : SPADE, DIAMONE, HEART, CLOVER ==> 4종류
# 카드 숫자 : A, 2, 3, 4, 5, 6, 7, 8, 9, 10, J, Q, K ==> 13장
# 카드 총 수 : 52장

card_list = [[0]*2 for i in range(52)] # ********** 위치가 card_creat 안에 있으면 안돼! **********
card_shape = ["SPADE", "DIAMOND", "HEART", "CLOVER"]
card_num = [0]*13
for i in range(1,14) :
    card_num[i-1] = i
card_num[0] = "A"
card_num[10] = "J"
card_num[11] = "Q"
card_num[12] = "K"


def card_creat(card_list, card_shape, card_num) :   
    cnt = 0
    for i in card_shape :
        for j in range(13) :
            card_list[cnt] = [i, card_num[j]]
            print(card_list[cnt])
            cnt += 1

def card_shuffle(card_list) :
    random.shuffle(card_list)

    print(card_list)
def card_share(card_list) :
    arr_num = 0 # 카드 뽑은 숫자
    print("현재 남은 카드 : ", len(card_list)-arr_num)

def card_print() :
    pass

while True : 
    print("[ 카드 프로그램 ]")
    print("1. 카드생성")
    print("2. 카드섞기")
    print("3. 카드5장 나눠주기")
    print("4. 카드5장 확인하기")
    print('-'*40)
    choice = int(input("원하는 번호를 입력하세요. >> "))

    if choice == 1 :
        card_creat(card_list, card_shape, card_num)
        
    elif choice == 2 :
        card_shuffle(card_list)
        
    elif choice == 3:
        card_share(card_list)
                
    elif choice == 4:
        card_print()

    else :
        print("프로그램을 종료합니다.")
        break
