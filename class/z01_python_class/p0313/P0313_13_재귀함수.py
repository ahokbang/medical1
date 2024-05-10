# 재귀함수
def count(num) :
    if num >= 1 :
        print(num, end=' ')
        count(num-1) # 자신의 함수를 다시 호출: 재귀함수
    else :
        return 

count(10)



print()

# 이렇게 하는 게 더 빨라서 재귀함수 잘 안써
for i in range(10,0,-1) :
    print(i, end=' ')