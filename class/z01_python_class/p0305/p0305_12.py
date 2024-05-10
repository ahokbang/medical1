import operator 
# operator : class 정렬

# 딕셔너리 정렬
t_dic = {}
t_list = []

t_dic = {"peach" : "복숭아", "orange" : "오렌지", "apple" : '사과', "pear" : "배", 
         "grape" : "포도", "mango" : '망고', "kiwi" :"키위"}

print(t_dic.keys()) # 딕셔너리의 키들만 출력
print(t_dic.values()) # 딕셔너리의 값들만 출력
print(t_dic.items()) # 튜플 형태로 출력
print('-'*50)
print(sorted(t_dic.items(), key=operator.itemgetter(0)))
# item이 이런식으로 나와: (peach, 복숭아), (orange, 오렌지), ...
#                           0      1         0      1
# itemgetter(0)으로 한 경우 영문 이름 순으로 정렬 
print('-'*50)
# 영문 이름 역순
print(sorted(t_dic.items(), key=operator.itemgetter(0), reverse=True))
print('-'*50)
# itemgetter(1)로 한 경우 한글 이름 순으로 정렬
print(sorted(t_dic.items(), key=operator.itemgetter(1)))       
# 한글이름 역순
print('-'*50)
print(sorted(t_dic.items(), key=operator.itemgetter(1), reverse=True))



# 3개의 숫자를 입력받아 순서대로 출력하시오.
# 17, 50, 12 를 입력받았을 경우 12, 17, 50 으로 출력
# if문을 사용할 경우 다 비교해야되서 복잡해. 오래 걸려.
# number = []
# for i in range(3) :
#     num = int(input("{}번째 숫자를 입력하세요. >> " .format(i+1)))
#     number.append(num)
#     number.sort()
# print(number)
# # 제일 큰 수 하나를 입력하세요.
# print(number[i])
 
''' 선생님 풀이
num = [0, 0, 0]
for i in range(3) :
    num[i] = int(input(f"{i+1} 숫자를 입력하세요.")) # f = format ********** 리스트에 넣기 쉬운 방법 **********
            # input("{}번째 숫자를 입력하세요." .formta(i+1)) ; 얘랑 같은 거야
num.sort()
# 최대값
max(num[0], num[1], num[2])
print("최대값 : ", max(num[0], num[1], num[2])) # 자바는 2개 비교 가능, 파이썬은 3개도 가능
print("최소값 : ", min(num[0], num[1], num[2]))
# 전개연산자를 사용해서도 가능
print("최대값 : ", max(*num) # Q) 리스트의 요소들이 3개 이상일 때도 이렇게 써도 되는지? A) 3개 이상이어도 돼!
print("최대값 : ", min(*num)
'''


'''
a = [5, 7, 4, 8, 1, 9, 3, 2]
a.sort() # 순차정렬
print(a)
print('-'*50)
b = [5, 7, 4, 8, 1, 9, 3, 2]
b.sort(reverse = True) # 역순정렬
print(b)
'''

