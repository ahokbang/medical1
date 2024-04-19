list = [
        [0,0,0],[0,0,0],[0,0,0]   
]

for i in list :
    print(i)
    print()
    for j in i :
        
        print(list[j])
        
list = [
        [1,2,3],[4,5,6],[7,8,9]   
]
for i in list :
    for f in i :
        print(f, end='\t')
    print()
    
    
# list = [
#         [0,0,0],[0,0,0],[0,0,0]   
# ]
# for i in list :
#     for f in i :
#         print(f, end='\t')
#     print()

# 1부터 9까지의 숫자를 1차원 리스트에 입력하시오. 
list = []
for i in range(9) :
    list.append(i+1)
print(list)

# 1부터 9까지의 숫자를 2차원 리스트에 입력하시오. 
# [ [1,2,3], [4,5,6,], [7,8,9] ]
a_lists = []
# for i in range(3) :
#     a_list = []
    
#     for j in range(3) :
#         a_list.append((j) # [0, 1, 2]
#     a_lists.append(a_list) #[ [0,1,2], [0,1,2], [0,1,2,] ]

# print(a_lists)

for i in range(3) :
    a_list = []  
    for j in range(3) :
        a_list.append((3*i)+j+1) # [0, 1, 2]
    a_lists.append(a_list) #[ [0,1,2], [0,1,2], [0,1,2,] ]
print(a_lists)

# 위의 코드가 너무 기니까 컴프리헨션의 형태를 이용해, for의 가로버전
list2 = [n+1 for n in range(9)]
print(list2)

list3 = [ [0]*3 ] # [ [0,1,2,], [0,1,2], [0,1,2] ]
print(list3)
# 또는 
list4 = [ [0]*3 for n in range(3)] # [ [0,0,0], [0,0,0], [0,0,0] ]

numList = [num*num for num in range(1,6)]        
print(numList)