# 요소 각각 출력하기

aa = [[1,2,3,4], [5,6], [7,8,9]]
a = [1,2,3,4,5]
for i in a :
    print(i)

# 2차원은 for문 2개
for i in aa :
    for j in i :
        print(j)

''' 일부만 3차원일 때는?         
aa = [[1,[3,4,5],3,4,], [5,6], [7,8,9]]       
for i in aa :
    for j in i :
        for k in j : # error 왜냐면 다 3차원이 아니니까
            print(k)
'''
# 2차원이 다 3차원 구조를 갖고 있을 때는 문제 없음.
aaa = [[[1,2],[3,4,5]],[[6],[7,8,9]]]
for i in aaa :
    for j in i :
        for k in j : 
            print(k)
print('-'*50)
aa = [[1,[3,4,5],3,4,], [5,6], [7,8,9]] 
for i in aa :
    for j in i :
        if isinstance(j, list) : # list인지 확인
            for k in j :
                print(k)
        else :
            print(j)

