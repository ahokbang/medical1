class Card: # 4개의 변수: kind, number, width, height
    width = 100 # 클래스 변수
    height = 200 # 클래스 변수
    
    def __init__(self, kind, number) :
        self.kind = kind
        self.number = number
        Card.width = 100
        Card.height = 200
'''        
# 52장 카드 생성
shape = ["SPADE", "DIAMOND", "HEART", "CLOVER"]
number = ["A", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
card_list = []
for i in range(4) :
    for j in range(13) :
        c = Card(shape[i],number[j]) # 객체선언
        card_list.append(c) # 리스트 추가
        
for i in range(52) :
    c = card_list[i] # c = card 객체
    print("카드 출력 : ", c.kind, c.number)
    # print("카드 출력 : ", card_list[i]) # ==> 주소값이 출력돼
    # print("카드 출력 : ", card_list[i].shape, card_list[i].number)
'''    

# 클래스 5개를 생성해서 kind = "SPADE", number = 1,2,3,4,5 클래스를 출력하시오. 
card_list = []

# 1-13까지 넣어보세요.
for i in range(13) :
    card_list.append(Card("SPADE", i+1))
    
# card_list.append(Card("SPADE", "A"))
# card_list.append(Card("SPADE", "2"))
# card_list.append(Card("SPADE", "3"))
# card_list.append(Card("SPADE", "4"))
# card_list.append(Card("SPADE", "5"))
# card_list.append(Card("SPADE", "6"))
# card_list.append(Card("SPADE", "7"))
# card_list.append(Card("SPADE", "8"))
# card_list.append(Card("SPADE", "9"))
# card_list.append(Card("SPADE", "10"))
# card_list.append(Card("SPADE", "J"))
# card_list.append(Card("SPADE", "Q"))
# card_list.append(Card("SPADE", "K"))

print("리스트 개수 : ", len(card_list))

for i in range(13) :
    print("리스트 출력: ", card_list[i].kind, card_list[i].number)
    
# print("리스트 출력 : ", card_list[0].kind, card_list[0].number)
# print("리스트 출력 : ", card_list[1].kind, card_list[1].number)
# print("리스트 출력 : ", card_list[2].kind, card_list[2].number)
# print("리스트 출력 : ", card_list[3].kind, card_list[3].number)
# print("리스트 출력 : ", card_list[12].kind, card_list[12].number)