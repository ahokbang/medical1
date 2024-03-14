# 콜백함수 : 함수를 다시 부른다. 함수에서 함수를 부를 수 있다.

# 함수선언
def callback_func(h_print) :
    for i in range(10) :
        # print("안녕하세요.")
        h_print(i)


# 함수선언
def h_print(num) :
    print("안녕하세요.", num)


# 함수호출 - 매개변수로 함수를 넘겨주는 것을 콜백함수
callback_func(h_print)

# ----------------------------------------------------
# 함수호출
# h_print()

    
# 함수도 변수선언 할 수 있어, 이렇게
# 함수를 변수에 저장
# func = h_print() # <= ()가 있어야 함수 실행을 저장하는 것. ()가 없으면 저장만 함.

