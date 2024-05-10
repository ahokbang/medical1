a_list = [
    1, 2, 3, 4, [6, 7, 8, 9], [10, 11]
]

# 출력하는 방법
for a in a_list :
    print(a, end=' ') # 1 2 3 4 [6, 7, 8, 9] [10, 11] 
print()
print('-'*30)
# 이중 리스트도 풀어서 출력하고 싶을 때
for a in a_list :
    if type(a) == list : 
        for i in a :
            print(i,end=' ')
    else :
        print(a, end=' ')
print()
print('-'*30)       
# 리스트에 추가
aa_list = []
for a in a_list :
    if type(a) == list : 
        for i in a :
            aa_list.append(i)
            print(i,end=' ')
    else :
        print(a, end=' ')
        aa_list.append(a)
print()
print('-'*30) 
print(aa_list)