
# 파일자체 복사하기

# 1. 파일 열기
in_file = open("C:\workspace\medical1\mem.txt", 'rb') # vscode에서 사진 파일 오른쪽 버튼-copy path
out_file = open("c:/aaaa/m1.txt", 'wb') # \는 \바로 뒤 문자를 문자 그대로로 인식하는 것으로 오류 발생 시 슬래시로 바꿔서 해보기
                                        # 없는 폴더를 지정하면 error

# 2. 파일 읽기/쓰기
while True :
    bin = in_file.read(1)
    if not bin : break
    out_file.write(bin)

# 3. 파일 닫기    
in_file.close()
out_file.close()
print('복사가 완료되었습니다.')
        
