# 컴프리헨션의 구성
# 리스트 = [수식 of 항목 in range() if 조건식]
# append 하는 기능
# numList = [num*num for in range()]

# zip() : 리스트를 튜플이나 딕셔너리로 짝지을 때 사용

list = [1,2,3]
alist = list # 동기화. 얕은 복사. 이렇게 복사하면 안돼
alist = [*list] # 깊은복사 1. 깊은 복사로 복사해야 해.
alist = list[:] # 깊은복사 2
list[0] = 100

print(alist)

list[0] = 100
print(alist) 

a = 100
b = a 
a = 10
print(b) # 100

# 리스트는 공간을 같이 써 