
num = [[10, 20], [30, 40], [50, 60]]

for i in range(len(num)) : # i = 0, 1, ...
    for j in range(len(num[i])) : # j = 0, 1, ...
        print(num[i][j]) # num[0][0] num[0][1]
        
i = 0 # 조건문에 사용하는 i는 while 바깥에!
while i < len(num) :
    j = 0 # j도 while 바깥에!
    while j < len(num[i]) : 
        print(num[i][j])
        j = j + 1
    i += 1