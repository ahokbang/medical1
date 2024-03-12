
today_list = ['2024', '03', '08']

# today_list[0] = int(today_list[0]) + 10
# print(today_list[0])

# map : 문자열을 정수형으로 모두 변환해서 리스트 저장

# list(map()) today_list에 있는 모든 값을 한번에 int로 바꾼 후 t_list에 넣어줌
t_list = list(map(int, today_list))
print(t_list)

# 5개의 숫자를 입력하시오.
list = []
for i in range(5) :
    list.append(int(input("숫자를 입력하세요. >> ")))
print(list)


# 또는 아래와 같이 표현 가능: 선생님 확인하고 알려주실 예정 [ <class 'list'> ]로 출력돼.

# list = [] 삭제하고

# for i in range(5) :
#     list(map(int,(input("숫자를 입력하세요. >> "))))
# print(list) 

# input의 데이터 int 변경해서 list 저장
a_list = list(map(int, input("숫자입력: ")))
print(a_list)


# map : 정수형을 문자열로 모두 변환해서 리스트 저장
int_list = [10, 20, 30, 40, 50]
str_list = list(map(str, int_list))
print(str_list)

# 함수를 사용해서 리스트값을 *10 변경 map : 함수배울 때 

# 리스트의 데이터 타입 : int
list = []
for i in range(5) :
    list.append(i) # 데이터타입 : int
print(list)

# 리스트의 데이터 타입 str로 변환
a_list = list(map(str, range(10)))
print(a_list)

