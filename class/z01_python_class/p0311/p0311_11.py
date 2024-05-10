a_list = [1, 2, 3]
# 얕은 복사, 주소값 변경
b_list = a_list

b_list[0] = 100

print(a_list)
