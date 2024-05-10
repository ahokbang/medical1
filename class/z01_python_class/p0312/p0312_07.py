# 가변매개변수
# - 아래의 *이 가변매개변수라는 뜻
'''
def str_title(num, *txt) # =========(1)

def str_title(num, txt1, txt2) :
    for i in range(num) :
        print(txt1, txt2)

str_title(1, "안녕", "잘가", "안녕하세요.", "반갑습니다.") # ===> 매개변수 숫자 안맞아서 에러

그러나 (1)으로 표현하면 에러 발생하지 않음.
'''

def str_title(num, *txt) :
    print("txt타입 : ", type(txt))
    print(txt) # 튜플 타입, 리스트랑 똑같은데 수정(삭제 포함) 불가
    for i in range(num) :
        for t in txt :
            print(t, end=" ")
        print()
        
str_title(1, "안녕", "잘가", "안녕하세요.", "반갑습니다.")