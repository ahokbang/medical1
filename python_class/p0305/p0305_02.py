# 1부터25까지 2차원 리스트 생성 ********** 다시 풀어보기 ********** 풀이는 여러가지가 있어
# [[1,2,3,4,5], [6,7,8,9,10], ..., [21,22,23,24,25]]

# 선생님 풀이
b = []
b_i = []
for i in range(0,25) :
    if (i+1)%5 == 0 :
        b_i.append(i) # [1,2,3,4,5 ]
        b.append(b_i)
        b_i = []
        pass
    else :
        b_i.append(i+1) # [1,2,3,4]
        pass
    b.append(i+1)
print(b)
print('-'*40)