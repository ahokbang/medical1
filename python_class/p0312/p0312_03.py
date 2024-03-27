def first(win_num) :
    for i in range(5) :
        win_num.append(i)

win_num = []
while True :
    input("다시 실행합니다.")
    first(win_num)
    print("win_num 데이터 : ", win_num)
    win_num = []
    