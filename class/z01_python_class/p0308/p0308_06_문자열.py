# ********** 인덱싱, 슬라이싱, len 외우기 **********

# 인덱싱, 슬라이싱, len, upper, lower, swapcase, titile
# 인덱싱은 몇번째[0], 슬라이싱은 어디서부터 어디까지[0:3][:3][1:]

'''
swapcase() : 소문자는 대문자로, 대문자는 소문자로 변환
title() : 제일 첫글자 대문자로 변환
'''

shape_list = ["spade", "diamond", "heart", "clover"]
for i in shape_list :
    print(i.upper()) # 모두 대문자로 출력 
    print(i.titile()) # 첫글자만 대문자로 출력
    print(i.swapcase()) # 소문자는 대문자로, 대문자는 소문자로 출력
    print(i.lower()) # 모두 소문자로 출력
    

# ********** len과 슬라이싱은 꼭 외우기! **********

title = "안녕하세요."
# 역순 출력하고 싶어
for i in range(len(title)) :# 5
    print(title[(len(title)-1)-i], end="")


print(1,2,3,4, sep='*') # ********** sep은 각 중간에 넣어주는 거!! **********


a = [1234,11111,1,145,20,1323456547]
# 리스트의 각 숫자의 길이를 출력하시오.
for i in a :
    print("{}의 길이 : {}" .format(i, len(str(i))))
    
# 짝수만 문자길이를 출력하시오.
for i in a :
    if i%2 == 0 :
        print("짝수 {}의 길이 : {}" .format(i, len(str(i))))

# 숫자 : {} , 길이  : {}
for i in a :
    print("숫자 : {}, 길이 : {}" .format(i, len(str(i))))

# 한글자씩 출력을 해보세요.
title = "혼자공부하는파이썬수업"
for i in title :
    print(i)
# 선생님이 원하는 방법
for i in range(len(title)) :
    print(title[i])


a = 10000000 # int(숫자)의 경우 자리수를 알고 싶을 때 len 사용 할 수 없어
print(len(str(a))) # 그래서 int를 str으로 바꾼 후 len 사용해서 자리수 확인

# 인덱싱 : [] 기호 이용해 문자열의 특정 위치에 있는 문자 참조
# 슬라이싱 :  [:] 기호 이용해 문자열 일부 추출, 문자열 선택 연산자로 슬라이드해도 원본은 변하지 않음(주의).

# len() : 문자열 길이 추출
b = "안녕하세요. 반갑습니다. 저는 홍길동입니다."
print(b[0]) # 안
print(b[2]) # 하
print(b[2:5]) # 하세요; 2부터 4자리 출력

a = input("문자를 입력하세요. >> ")
print("현재 입력한 문자 길이 : ", len(a))

