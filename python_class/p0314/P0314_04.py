'''    
# 파일1개 저장

# file open
file = open("memo.txt", 'w', encoding='utf8')
try: 
    # file write
    file.write("안녕하세요1. \n")
    file.write("안녕하세요2. \n")
    print(1/0)
    file.write("안녕하세요3. \n")
    file.write("안녕하세요4. \n")
except :
    print("저장 시 에러가 났습니다.")
finally : # 예외 발생해도, 발생하지 않아도 무조건 실행
    # file close 
    file.close() 
'''
'''
아래 두 조합 가장 많이 사용됨.
try +except 구문
try + except + finally 구문
그 외 아래의 구문이 더 있음.
try +except + else 구문
try +except + else + finally 구문
'''
# 에러 확인하는 방법
file = open("memo.txt", 'w', encoding='utf8')
try: 
    # file write
    file.write("안녕하세요1. \n")
    file.write("안녕하세요2. \n")
    print(1/0)
    file.write("안녕하세요3. \n")
    file.write("안녕하세요4. \n")
except Exception as e : # 예외에 대한 설명 출력
    print("저장 시 에러가 났습니다.")
    print(e) # 어떤 에러가 인지 설명해줘.
finally : # 예외 발생해도, 발생하지 않아도 무조건 실행
    # file close 
    file.close() 