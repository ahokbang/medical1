class Card :
    kind = ""
    number = ""
    
    def __init__(self,kind, number):
        self.kind = kind
        self.number = number


# 클래스를 이용해서 52장의 카드 생성: 비교적 보안이 좋음
c_list = []
kind = ["SPADE", "DIAMOND", "HEART", "CLOVER"]
number = [1,2,3,4,5,6,7,8,9,10,11,12,13]
for i in range(4) :
    for j in range(13) :
        c = Card(kind[i], number[j]) # 클래스를 생성해서 리스트에 추가
        c_list.append(c)
        
for i in range(52) :
    print("카드 출력 : ", c_list[i].kind, c_list[i].number)


'''
# 리스트를 이용해서 52장의 카드 생성 
c_list = []
kind = ["SPADE", "DIAMOND", "HEART", "CLOVER"]
number = [1,2,3,4,5,6,7,8,9,10,11,12,13]
for i in range(4) :
    for j in range(13) :
        c = [kind[i], number[j]] # 리스트를 생성해서 리스트에 추가
        c_list.append(c)
        
    
for i in range(4) :
    for j in range(13) :
        print("카드 : ", kind[i], number[j])

'''

'''
# 1개 변수로 선언 -------------------------------
kind = "SPADE"
number= "1"

kind2 = "HEART"
number = "1"

'''

'''
c1 = Card("SPADE", "1")
# c1의 숫자를 5로 변경하시오.
c1.number = "5"
# c1을 출력하시오.
print("c1 : ", c1.kind, c1.number)


# c2 "HEART", "A" 생성 후
# 모양을 "DIAMOND" 변경하여 출력하세요.
c2 = Card("HEART", "A")
c2.kind = "DIAMOND"
print("c2 : ", c2.kind, c2.number)
'''