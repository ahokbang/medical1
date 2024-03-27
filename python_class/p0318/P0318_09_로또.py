class Lotto :
    number = 0
    shape = "circle"
    
    def __init__(self, number) :
        self.number = number
        

# Lotto 1-45까지의 숫자를 입력한 리스트를 생성한 후, 출력하시오.

l_list = []

for i in range(45) :
    # lotto_list.append(i+1)
    l = Lotto(i+1)
    l_list.append(l)

for i in range(45) :
    l = l_list[i]
    print("로또번호 : ", l.number)
