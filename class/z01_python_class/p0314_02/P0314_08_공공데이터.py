# ********** 메모장으로 저장할 때 파일형식은 모든파일, 인코딩은 UTF-8로 저장!! **********


# medical_1.csv 파일을 읽어와서 출력하시오.
# 1. 파일열기
f = open("medical_1.csv", "r", encoding='utf8')

# 2. 파일읽기
cnt = 0
sum = 0
while True :
    content = f.readline()
# 첫번재 줄 날리기
    if cnt == 0 :
        cnt += 1
        continue
    if content == "" : break
# 2012-2019년도 기초생활보장수급자 총합 구하기
    c_list = content.split(',')
    c_list[1] = int(c_list[1])
    sum += c_list[1]
    print(c_list, len(c_list))
    
    # print(content, end="")
    print("기초생활수급대상자 전체 수 : ", sum)

# 3. 파일닫기
f.close()








''' 내가 한 거
# 2012-2019년도 기초생활보장수급자 총합 구하기
    f_list = content.split(',')
    # print(f_list)       
    print(f_list[1]) # 타입이 문자
    for i in f_list :
        for j in i :
            sum = 0
            sum += f_list[i][1]
    print(sum)

'''