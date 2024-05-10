# 파일열기
file = open("memo.txt", "r", encoding='utf8')

# 파일읽기
content = file.read().strip() # <== strip 여기에 있어도 돼. 메모장에 있는 모든 글들을 읽어 옴. 
content = content.strip() # 문자열 빈공백 제거 strip()
# 1, 홍길동, 100, 100, 99  ==> split(",") : 문자열을 쉼표로 분리 -> list
print(content)
# c_list = content.split("\n")
stuNo, name, kor, eng, math = content.split("\n")  # <== 윗줄 대시 이렇게로도 쓸 수 있어
c_list = [0]*5
c_list[0] = int(stuNo)
c_list[1] = name
c_list[2] = int(kor)
c_list[3] = int(eng)
c_list[4] = int(math)
print(c_list)

# 파일닫기
file.close()

