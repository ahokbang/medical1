# 파일 읽어오기
# 1. 파일 열기
# read() : 모든 문자열을 가져옴.
# readline() : 1줄씩 가져옴
# readlines() : 1줄씩 리스트 타입에 입력해서 모두 가져옴.
# 3. 파일 닫기

# 파일 확인
import os
if os.path.exists("str1.txt") : # 파일 존재 확인
    with open("str1.txt", "r", encoding='utf8') as f :
        txt_list = f.readlines() 
    
    for txt in txt_list :
        print(txt, end="")
    print() 
else : 
    print("프로그램을 종료합니다.")

# readlines
with open("str.txt", "r", encoding='utf8') as f : # 변수명을 뒤에 씀.
    txt_list = f.readlines() # ==> 한 줄씩 리스트 타입으로 저장
    # print(txt_list) 또는 아래와 같이 쓸 수 있음
    
    for txt in txt_list :
        print(txt, end="")
    print()

# f.close() 생략가능

'''
# readlines # 1줄씩 리스트타입으로 가져옴
f = open("str.txt", "r", encoding='utf8')
# 1줄씩 리스트타입으로 저장
txt_list = f.readlines()
print(txt_list)
print(txt_list[0])
f.close()
'''

'''
# readline에서 읽어오기

f = open("str.txt", "r", encoding='utf8')
while True :
    txt = f.readline()
    if txt == "" : break
    
    print(txt, end='')  
'''