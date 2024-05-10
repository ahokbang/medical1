# ********** 외우기 **********


# card_list = [
#              {"shape" : "spade", "num" : "A"}
#              {"shape" : "spade", "num" : "2"},
#              {"shape" : "spade", "num" : "3"},
             
#              ]

card_list = []
print(card_list)
shape_list = ["spade", 'diamond', 'heart', 'clover']
num_list = [0]*13
for i in range(1,14) :
    num_list[i-1] = i
num_list[0] = "A"
num_list[10] = "J"
num_list[11] = "Q"
num_list[12] = "K"

print(shape_list)
print(num_list)

# 포커 순서
# 스페이드 > 다이아 > 하트 > 클로버
# A > K > Q > J > 10~2

# 카드 1세트를 구련해서 출력하시오.
'''내 풀이 : 실패, ********** 다시 해보기 **********
for i in range(4) :
    card_list[i][0] = shape_list[i]
    for j in range(13) :
        card_list[j][1] = num_list[j]
print(card_list)
''' 
# 선생님 풀이 ********** 꼭 이해하기! **********
card_list = [[0]*2 for i in range(52)]
cnt = 0
for i in shape_list : # spade, diamond, heart, clover
    for j in range(13) :
        card_list[cnt] = [i, num_list[j]]
        print(card_list[cnt])
        cnt += 1

print(card_list)