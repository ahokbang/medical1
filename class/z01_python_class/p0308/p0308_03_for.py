
# 1차원 리스트 생성방법
# [0,0,0,0,0, ... 52개를 생성하시오. ]
# 방법 1
a_list = [0]*52
# 방법 2
b_list = []
for i in range(52) :
    b_list.append(0)
    b_list.append(i) # 0~51을 넣을 때
# 방법 3
c_list = [ 0 for i in range(52) ]   
       # [ i for i in range(52) ] # 0~51 넣을 때

print(a_list)
print(b_list)
print(c_list)


# 2차원 리스트 생성방법
# [ [0], [0], [0], ... 52개를 생성하시오. ]

# 방법 1
aa = [[0]*1]*52 # 얕은 복사이기에 쓸 수 없음
print(aa)
aa[0][0] = 1
print(aa) # 52개 요소 무두 1로 변경
aa[51][0] = 10
print(aa) # 52개 요소 모두 10으로 변경

# 방법 2
bb = [[0]*2 for i in range(52)]
print(bb)
bb[0][0] = 1
bb[51][0] = 10
print(bb)

# 방법 3
cc = []
for i in range(52) :
    dd = []
    for i in range(2) :
        dd.append(0)
    cc.append(dd)
print(cc)