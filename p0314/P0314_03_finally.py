# 예외구문 : try, except, else, finally

a_list = [1,2,3,4,5,6,7,8,'9',10]

'''
for i in a_list :
    print(i+1) # error 발생. 9가 str이니까
'''    
# 그래서 try except 구문 사용하면,

for i in a_list :
    try :
        print(i+1)
    except :
        print("데이터 오류가 있습니다.") # <= 대신 pass 넣어도 돼.

''' [출력 내용]
2
3
4
5
6
7
8
9
데이터 오류가 있습니다.
11
'''


print("[ 프로그램 실행 ]")
try : 
    print(1)
    print(2)
    print(1/0) # error 발생
    print(3)
except :# 예외가 발생하면 실행
    print(4)
    print(5)
else : # 예외가 발생하지 않으면 실행
    print(6)
finally : # 예외가 발생하거나 하지 않거나 무조건 실행
    print(7) 
print("[ 프로그램 종료 ]")


'''
try : 
    예외가 발생할 가능성이 있는 코드
except :
    예외가 발생했을 때 실행할 코드
else :
    예외가 발생하지 않았을 때 실행할 코드
finally :
    무조건 실행할 코드

'''