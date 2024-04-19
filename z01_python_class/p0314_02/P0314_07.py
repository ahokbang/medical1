# str.txt 파일의 내용을 모두 출력하시오.
# str2.txt에 저장하세요.

# 파일열기
f = open("str.txt", "r", encoding='utf8')

# 파일읽기
while True :
    content = f.readline()
    if content.strip() == "" : break # 빈공백/enter키 사라지게하는 방법 .strip()
    print(content, end='')

# 파일닫기
f.close()

print('-'*50)

# str.txt 파일 내용을 읽어와서 str1.txt에 그 내용을 추가 해보세요.

f = open("str.txt", "r", encoding='utf8')
ff = open("str1.txt", 'a', encoding='utf8')

while True :
    contett=f.readline() # 파일내용 읽어오기
    if content.strip() == "" : break
    ff.write(content) # 파일내용 추가하기
f.close()
ff.close()

f = open("str1.txt", 'r', encoding='utf8')    
while True :
    content = f.readline()
    if content.strip() == "" : break
    print(content, end="")
f.close()

fff = open("str1.txt", 'r', encoding='utf8')    
while True :
    content = fff.readline()
    if content.strip() == "" : break
    print(content, end="")
fff.close()

    
    
''' 내가 한 거
# 파일 열기
f = open("str.txt", "r", encoding='utf8')
ff = open("str1.txt", 'a', encoding='utf8')
fff = open("str2.txt", 'w', encoding='utf8')

# 파일 쓰기
while True :
    content = f.readline()
    if content == "" : break
    content1 = ff.readline()
    if content1 == "" : break
    # print(content, end='')

    # ff.write(content)
    
    # content = ff.readline()
    # if content == '' : break
    # print(content, end='')
    fff.write(content1)

# 파일 닫기
fff.close()
'''