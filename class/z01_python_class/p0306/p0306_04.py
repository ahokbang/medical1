
fruit = {"peach" : "복숭아", "orange" : "오렌지", "apple" : '사과', "pear" : "배", 
         "grape" : "포도", "mango" : '망고', "kiwi" :"키위"}

# 한글을 출력해서 
# 예) 복숭아 영어로 입력하시오. 순차적으로 출력
count = {}

for f in fruit :
    eng_in = input("{}를 영어로 입력하세요. >> " .format(fruit[f]))
    print("입력한 단어 : {}" .format(eng_in))
    # 프로그램 만들기
    # 맞는지 틀린지는 비교
    if eng_in == f :
        print("정답입니다.")
    else :
        print("정답이 아닙니다.")


''' 선생님 설명 ********** 꼭 기억하세요!! **********
for f in fruit : 
    print("키 : ",f) # 영어만 찍혀
    # value 찍고 싶으면
    print("value : ", fruit[f]) 

'''
# 정답이 몇개 인지
answer = 0
wrong = 0

for f in fruit :
    eng_in = input("{}를 영어로 입력하세요. >> " .format(fruit[f]))
    print("입력한 단어 : {}" .format(eng_in))
    if eng_in == f :
        print("정답입니다.")
        answer += 1
    else : 
        print("오답입니다. 정답 : {}" .format(f))
        wrong += 1
print("[ 문제 체크 ]")
print("총 문제: ", len(fruit))
print("정답 : ", answer)
print("오답 : ", wrong)