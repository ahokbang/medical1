# 변수 3개를 만들어서 name, city, fruit
# 아래와 같이 출력해보세요.
# 저의 이름은 name 입니다.
# 저는 city시에서 태어났습니다
# 저는 fruit를 좋아합니다.

# p0221_04.py 파일 참고 github

# name = "alana"
# city = "서울"
# fruit = "복숭아"
# # 그냥 출력하기
# print("저의이름은 alana 입니다.")
# print("저는 서울에서 태어났습니다.")
# print("저는 복숭아를 좋아합니다.")

# # ,로 나누기
# print('저의 이름은' + 'alana' + '입니다.')
# print('저는 ' + '서울' + '시에서 태어났습니다.')
# print('저는 '+ '복숭아'+ '를 좋아합니다.')

# # 변수 사용
# # , 사용하기
# print("저의 이름은", name, "입니다.")
# print("저는",city,"에서 태어났습니다.")
# print("저는",fruit,"를 좋아합니다.")

# # + 사용하기
# print("저의 이름은 "+name+"입니다.")
# print("저는 "+city+"에서 태어났습니다.")
# print("저는 "+fruit+"를 좋아합니다.")

# # %s 사용하기
# print("저의 이름은 %s 입니다"%(name))
# print("저는 %s에서 태어났습니다"%(city))
# print("저는 %s를 좋아합니다"%(fruit))

# # format 사용하기
# print("저의 이름은 {}입니다".format(name))
# print("저는 {}에서 태어났습니다.".format(city))
# print("저는 {}를 좋아합니다." .format(fruit))

# input 사용하기
# name = input("이름을 입력하세요. >> ")
# city = input("태어난 도시를 입력하세요. >> ")
# fruit = input("좋아하는 과일을 입력하세요. >> ")

# # %s
# print("저의 이름은 %s 입니다."%(name))
# print("저는 %s에서 태어났습니다."%(city))
# print("저는 %s를 좋아합니다."%(fruit))

# # .format
# print("저의 이름은 {}입니다.".format(name))
# print("저는 {}에서 태어났습니다".format(city))
# print("저는 {}를 좋아합니다.".format(fruit))

#선생님 답
#input(): 내가 입력한 값을 변수로 사용한다.
# inputVal = input("입력하시오. >> ")
# # inputVal = "비"
# print("입력하신 글자는 " +inputVal)

name = input("이름을 입력하세요. >> ")
city = input("태어난 도시를 입력하세요. >> ")
fruit = input("좋아하는 과일을 입력하세요. >> ")

print("저의 이름은 "+name+" 입니다.")
print("저는 "+city+"에서 태어났습니다.")
print("저는 "+fruit+"를 좋아합니다.")