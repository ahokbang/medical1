## 파일을 읽어와서 출력하시오. 

# 파일 열기
# 상대경로 : medical1 폴더 안 member.csv
# 상대경로 : medical1>h0327>aaa 폴더 안 h0327/aaa/member2.csv
f = open("member.csv", "r", encoding='utf8')
# with open("member.csv", "r", encoding='utf8') as f:    <== 이렇게 사용하면 f.close() 안해도 돼.

# 파일 읽기
while True:
    str = f.readline()
    if str == "" : break
    str = str.strip()
    mem = str.split(',')
    print(mem[0], mem[1])    

# 파일 닫기
f.close()
