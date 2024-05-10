# 리스트
# 대괄호로 감싸서 나타내며 0개 이상의 원소가 저장될 수 있습니다.
num = 1
num = 2
print(num) # 2가 출력됨.

listA = [1,2]
listB = []

n1 = 1
n2 = 2
n3 = 3
n4 = 4
n5 = 5
list1 = [1,2,3,4,5]
list2 = ['사과', '복숭아', '딸기', '배', '포도', '수박', '파인애플', '멜론']
# 각 문자가  0       1       2       3      4       5        6       7   번째 들어있다고 인식해.
# 음수 표현 -8      -7      -6      -5      -4      -3      -2      -1
# python의 경우 여러 형태의 변수를 섞어서 사용할 수 있다.
list3 = [1, '홍길동', 99.1] # 정수, 문자, 실수

print(list1)
print(list2[1]) # list2의 1번째 들어있는 과일은 [복숭아]이므로 [복숭아]가 출력

# list1에 4를 출력
print(list1[3])
# list3에 99.1을 출력
print(list3[2])

# 대괄호에 음수를 넣으면 뒤 요소부터 출력
print(list2[-1]) # 끝에서 첫번째에 있는 [멜론]이 출력 

# 리스트의 길이 출력
a = len(list2)
print(a) # list2는 8개의 과일이 들어있으므로 [8]이 출력

# print(list3[5]) # error; 요소가 3개이므로 5를 넣으면 error 발생

# list2에서 딸기를 출력해보세요.
print(list2[2])
print(list2[-6])
# 선생님답
print(list2[len(list2)-1])

# 리스트 슬라이싱
aa = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(aa)
# 1 이상 4 미만 출력하고 싶을 때 슬라이싱 사용
print(aa[1:4]) # 1 이상 4 미만 출력: [1, 2, 3]
print(aa[3:8]) # 3이상 8미만: [3, 4, 5, 6, 7]
print(aa[2:]) # 2번 부터 끝까지
print(aa[:7]) # 처음부터 7미만까지
print(aa[:]) # 처음부터 끝까지 
print(aa)
print(aa[1:-1]) # 처음부터 끝에서 마지막 자리는 미포함, 1이상 끝 바로 앞까지 : [1, 2, 3, 4, 5, 6, 7, 8, 9]

# 요소 확인 : 내부에 포함되어 있는지 확인하는 방법을 제공해줌.
# in, not in
print('포도' in list2)
print(11 in aa)
print(0 not in aa)

listC = [1, 2, 3, ['a', 'b', 'c'], [4,5]]
#        0  1  2          3          4
print(listC[0])
print(listC[3])
print(listC[4])
print( 1 in listC) # True
print( 4 in listC) # False
print([4,5] in listC) # True

