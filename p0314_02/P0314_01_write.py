
# 파일열기
file = open("memo.txt", "w", encoding='utf-8')

# 파일쓰기


print("[ 메모장 실행 ]")
print('-'*40)
while True :
    txt = input()
    if txt == "0" :
        print("메모장을 저장합니다.")
        break
    print(txt)
    file.write(txt+"\n")

# 파일닫기
file.close()

print("파일이 저장되었습니다.")

'''
모드(Mode) : open()함수의 마지막 매개변수
- 생략하는 경우 r과 동일
- 읽기모드 : 변수명 = open("파일명", "r") # 읽어오기(read)
- 읽기/쓰기 겸용 모드 : 변수명 = open("파일명", "r+") 
- 쓰기모드 : 변수명 = open("파일명", "w") # 새롭게 저장(write)
- 쓰기모드(추가) : 변수명 = open("파일명", "a") # 추가로 저장(append); 기존 파일이 있으면 이어서 쓴다.
- 텍스트모드 : 변수명 = open("파일명", "t") # 텍스트 파일 처리, 기본값.
- 이진모드 : 변수명 = open("파일명", "b") # 이진파일 처리
''' 

# for i in range(10) :
#     file.write(f"안녕하세요. {i+1}\n")