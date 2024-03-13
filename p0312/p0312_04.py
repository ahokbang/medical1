# 매개변수 순서 중요, 매개변수 타입도 중요

def str_print(txt, num) :  # (1) <==== 매개변수 순서, 타입 중요해, (1)과 (2) 동일해야 해!
    for i in range(num) :
        print(txt, end='\t')
    return txt, num

txt = input("출력하고 싶은 글자를 입력하세요. >> ")
num = int(input("출력하고 싶은 글자 반복횟수를 입력하세요. >> "))
str_print(txt, num) # (2) <==== 매개변수 순서, 타입 중요해, (1)과 (2) 동일해야 해!