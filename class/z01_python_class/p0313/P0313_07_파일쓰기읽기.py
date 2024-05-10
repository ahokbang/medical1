import os

# print("현재 폴더 내 파일들 표시 : ", os.listdir())

# 1. 파일 쓰기
# 파일 생성 방법1
f = open ("student.txt", "w", encoding="utf-8")
f.write("1,'홍길동',100,99,87,286,95.33,2\n")
f.write("2,'유관순',98,93,87,278,92.67,3")
f.close() # 파일닫기 꼭!

# # 파일 생성 방법2 : with 사용하면 f.close() 사용하지 않아도 됨.
# with open ("student.txt", "w") as f :
#     f.write("1,'홍길동',100,99,87,286,95.33,2")
    
# 파일 읽기    
t_list = []
out_f = open("student.txt", "r", encoding="utf-8")    
while True : 
    txt = out_f.readline() # 1줄씩 읽어오기
    # print(type(txt))
    if txt == "" :
        break
    print(txt, end="")
    t_list.append(txt)
print()
print(t_list)    

out_f.close()

# 3. 파일 삭제
os.remove("student.txt")

    
# 폴더 존재 확인
# if not os.path.exists("hello") :
#     print("폴더가 존재하지 않습니다. 폴더를 생성합니다.")
#     os.mkdir("hello")
# else : 
#     print("폴더가 존재합니다. 폴더를 삭제합니다. ")
#     os.rmdir("hello")
