import operator

# numbers에 있는 숫자들이 몇번 나왔는지 딕셔너리로 출력하시오. 

numbers = [1,2,4,6,4,3,6,7,1,3,4,3,4,7,7,7,7,1,1,1,7]
counter = {}

for num in numbers :
    if num not in counter :
        counter[num] = 0
    counter[num] += 1
print(counter)

''' 선생님 풀이
counter = {}
for n in numbers :
    if n not in counter :
        counter[n] = 0
    counter[n] += 1
'''
# 정렬
print(sorted(counter.intems(), key=operator.itemgetter(0)))


# 알파벳들이 몇번 나왔는지 딕셔너리로 출력하세요.
array = ["F", "D", "A", "C", "A", "C", "F", "B", "C", "E", "C", "C", "F", "A", "B", "E", "F", "E"]
cnt = {}

for arr in array :
    if arr not in cnt :
        cnt[arr] = 0 
    cnt[arr] += 1
print(cnt)

''' 선생님 풀이
a_dic = {}
for array in arrays :
    if array not in a_dic :
        a_dic[array] = 0
    a_dic[array] += 1
print(a_dic)

'''

t_dic = {"peach" : "복숭아", "orange" : "오렌지", "apple" : '사과', "pear" : "배", 
         "grape" : "포도", "mango" : '망고', "kiwi" :"키위"}