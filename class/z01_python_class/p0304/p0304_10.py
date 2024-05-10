a = 10
b = 20
a_list = [1, 2, 3]

print(a) # 값이 저장돼
print(b) # 값이 저장돼
print(a_list) # 주소값이 저장 돼

a = 10
# 변수 복사
b = a
b = 100 
print(a)
print(b)
print("-"*40)


# 리스트 복사
a_list = [1, 2, 3]
b_list = a_list
b_list[0] = 200
print(a_list[0]) # 1이 아니라 200, a_list와 b_list는 같은 주소값이야. 주소값 복사
                 # => 얕은 복사라고 하며, 따로따로 놓으려면 깊은 복사를 해야해. 
                 # ********** 중요한 개념. **********

print(b_list[0])

print(a_list)
