# 파일의 보안, 관리의 용이성을 위해 클래스 사용.

import random

# 클래스 선언: 설계도
class Card :
    
    def __init__(self, kind, number) : # init로 지정해두면 위의 kind, number 변수 지정한 거 지워도 돼
        self.kind = kind
        self.number = number
    
    def __str__(self) :
        return f"{self.kind}, {self.number}"
    

# 52장의 카드
# SPADE, DIAMOND, HEART, CLOVER
# 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13
kind_list = ["SPADE", "DIAMOND", "HEART", "CLOVER"]
number_list = [1,2,3,4,5,6,7,8,9,10,11,12,13]
card_list = [] # 리스트의 주소? 0에서 51

def random_one() :
    num = random.randint(0,51)
    # print("랜덤카드 1장 : ", num, card_list[num].kind, card_list[num].number)
    return card_list[num]

# 52장 카드 생성
for i in range(4) :
    for j in range(13) :
        card_list.append(Card(kind_list[i], number_list[j])) # 카드 객체 선언, 클래스 내 생성자 호출
        
# 52장 카드 출력
for i in range(52):
    print("card :", card_list[i].kind, card_list[i].number)

# 랜덤으로 1장 뽑기 출력
random_one()

# 중복을 하지 않고 랜덤카드 5장을 뽑으시오.
nums = []

def random_five() :
    n = random.sample(card_list,5)
    nums.append(n)

random_five()

print(nums)

# for i in nums : 
#     print(i.kind, i.number) # ***** 확인하기 ****** 주소값이 나와

''' 선생님 풀이
1. 0-51 순차적인 것을 랜덤 섞기 후, 순차적으로 뽑으면 됨.
2. 5장을 랜덤으로 뽑으면 됨.
3. 1장 뽑고 기존에 있는 카드와 비교해서 다시 뽑는 방법

print("-"*40)
1. card_list shuffle
print("1. card_list shuffle")
random.shuffle(card_list)
for i in range(5) :
    print("랜덤섞기 카드 : ", card_list[i].kind, card_list[i].number)

print("-"*40)   
2. card_list sample 5
print("2. card_list sample 5")
ran_list = random.sample(card_list, 5)
for i in ran_list :
    print("랜덤sample섞기 카드 : ", i.kind, i.number)

print("-"*40)   
3. temp_list 저장소를 1개 만들고, 랜덤뽑기 1장의 카드를 저장장소의 리스트와 비교
temp_list = [0]*5
# print("개수 : ", len(temp_list))
cnt=0
while True :
    if cnt ==5 : break # 랜덤뽑기 카드가 5장일 경우 종료
    c = random_one() # 랜덤카드 1장 뽑기
    for i in temp_list :
        if c.kind == i.kind and c.number == i number : # 같은 카드가 있으면 다음으로 진행
            continue
        
    # 중복카드가 없으면 추가
    temp_list.append(c)
    cnt += 1

for i in temp_list :
    print("랜덤1장 뽑기 카드 : ", i.kind, i.number)

'''