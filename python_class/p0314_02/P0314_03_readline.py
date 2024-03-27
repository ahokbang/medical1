# stu.txt 파일을 출력하시오.
# 리스트 형식으로 출력
file = open("stu.txt", "r", encoding='utf8')
stu_list = []

while True :
    txt = file.readline()
    if txt == "" : break
    print(txt)
    
    f_list = txt.split(",")
    f_list[0] = int(f_list[0].strip())
    f_list[1] = f_list[1].strip()
    f_list[2] = int(f_list[2].strip())
    f_list[3] = int(f_list[3].strip())
    f_list[4] = int(f_list[4].strip())
    f_list[5] = int(f_list[5].strip())
    f_list[6] = float(f_list[6].strip())
        
    print(f_list)
    # stu_list[0] = int(stuNo)
    # stu_list[1] = name
    # stu_list[2] = int(kor)
    # stu_list[3] = int(eng)
    # stu_list[4] = int(math)
    # stu_list[5] = int(total)
    # stu_list[6] = float(avg)
          
    # if txt == "" :
    #     break
    # for i in range(7) :
    #     print(stu_list)

file.close()


# # 파일 읽어오기
# file = open("str.txt", 'r', encoding='utf8')
# while True: 
#     txt = file.readline() # 파일 1줄 읽어오기
#     if txt == "" :
#         break
#     print(txt, end="")

# file.close()


'''
# 파일저장
file = open("str.txt", "w", encoding='utf8')

file.write("안녕하세요. 반갑습니다.\n")
file.write("저는 홍길동입니다.\n")
file.write("파이썬 수업을 열심히 듣고 있습니다.\n")

file.close()
print("파일이 저장되었습니다.")
'''