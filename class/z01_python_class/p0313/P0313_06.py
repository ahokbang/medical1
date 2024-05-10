import os

print("현재 운영체제 : ", os.name)
print("현재 폴더위치 : ", os.getcwd())
print("현재 폴더 내 파일들 표시 : ", os.listdir())

# 폴더 생성
# os.mkdir("hello") # C:\workspace\medical1 에 hello 폴더 생성됨.
# 폴더 삭제
# os.rmdir("hello") 

# 파일 생성
with open ("student.txt", "w") as f :
    f.write("1,'홍길동',100,99,87,286,95.33,2")

# ********** 17-18줄 꼭 기억하기 csv -> 리스트로 바꾸는 법 **********
str1 = "1,'홍길동',100,99,87,286,95.33,2" # csv 타입, 서로간의 공유를 위해 
s_list = str1.split(",") # 리스트로 바꾸는 법 

for i in s_list :
    print(i)


# 제이슨 타입, xml 타입, csv 타입 3가지가 있어(공공데이터)