# k001.csv 파일에서 전국 인원수를 출력하시오. 

# 1. 파일 열기
f = open("k001.csv", "r", encoding='utf-8')

cnt = 0
sum = 0
# 2. 파일 읽기
while True :
    content = f.readline()
    if cnt == 0 :
        cnt += 1
        continue
    if content == "" : break
    
    k_list = content.split(',')
    k_list[4] = int(k_list[4])
    sum += k_list[4]
print("전국 인원수 : ", sum)
  
# 3. 파일 닫기
f. close()