# 명사, 동사, 형용사 10개씩 넣어서 영단어 맞추기 프로그램 만들기
# 딕셔너리에서 5개 랜덤으로 추출하여 퀴즈 내기
# 1. words[choice]에서 key값을 추출해서 list 타입으로 변경
#    words[choice].keys() : class
#    w_list = list(words[choice].keys())
# 2. random 5개 list 추출
#    ran_list = random.sample(w_list, 5)
# 3. 5개 list를 퀴즈에 넣으면 됨.

import random

words = [ {},
          { "airplane" : "비행기", "apple" : "사과", "bakery" : "빵집",
          "banana" : "바나나", "bank" : "은행", "bean" : "콩",
          "bicycle" : "자전거", "boat" : "보트", "bowl" : "그릇", "bus" : "버스" },
          { "fly" : "날다", "boil" : "끓이다", "fall" : "떨어지다",
           "owe" : "빚지다", "grow" : "성장하다", "chew" : "씹다",
           "bite" : "물다", "happen" : "발생하다", "drink" : "마시다", "wash" : "씻다" },
          { "exquisite" : "고상한", "beautious" : "예쁜", "dainty" : "앙증맞은",
            "bonny" : "보기에 좋은", "trig" : "말끔한", "spruce" : "단정하고 똑똑해 보이는",
            "radiant" : "빛을 발하는", "dapper" : "옷을 잘 입는", "splendid" : "화려한",
            "elegant" : "품위 있는" } ]

w_title = ["", "명사", "동사", "형용사"]

# 함수 선언
def w_quiz(choice) :
    print("{}를 선택하셨습니다." .format(w_title[choice]))
    chk = input("퀴즈가 나갑니다. 준비되셨나요? (1. 실행 0. 취소)")
    cnt_pass = 0
    if chk == '1' :
        # 퀴즈 프로그램
        # key-영문, value-한글
        '''
        print(w_noun.keys()) # 전체 key, 아래 for 문과 동일
        for key in w_noun :
            print(key) 
        # print(w_noun.values()) # 전체 value
        ''' 
        # 선생님은 여기에 count = 0 자리 
        
        w_list = list(words[choice].keys())
        w_list_ran = random.sample(w_list,5)
        # print(type(w_list))
        # print(w_list_ran)
           
        for key in w_list_ran : # {딕셔너리} 에서 키를 뽑는 거니까 여기 words[choice]를 w_list_ran으로 바꿔주면 돼
             # print(key, ":", w_noun[key])
            answer = input("{} 단어의 뜻은?" .format(key))
            if answer == words[choice][key] :
                print("정답입니다.")
                cnt_pass += 1
            else :
                    # 내 풀이 : print("정답이 아닙니다.")
                    # 선생님 풀이 
                print("정답이 아닙니다. 정답 : {}" .format(words[choice][key]))
            # 내 풀이 : print("총 {}문제 맞추셨습니다." .format(cnt_pass))
            # 선생님 풀이
        print("정답개수 : {}, 오답 : {}" .format(cnt_pass, len(w_list_ran)-cnt_pass)) # 요기의 words[choice]가 w_list_ran으로 바뀜
    else :
        print("퀴즈를 취소하셨습니다. 메뉴로 돌아갑니다.")

while True : 
    print("[ 영단어 맞추기 프로그램 ]") 
    print("1. 명사")
    print("2. 동사")
    print("3. 형용사")
    print('-'*40)
    choice = int(input("원하는 번호를 입력하세요. >> ")) # 정수형으로 받음
    
    if choice == 1 :
        w_quiz(choice) 
        
    elif choice == 2 :
        w_quiz(choice)
    
    elif choice == 3 :
        w_quiz(choice)
    
    else :
        print("프로그램을 종료합니다.")
        break

''' 선생님 풀이
import random
words = [ {},
    { "airplane":"비행기","apple":"사과","bakery":"빵집",
      "banana":"바나나","bank":"은행","bean":"콩",
      "bicycle":"자전거","boat":"보트","bowl":"그릇","bus":"버스"},
    { "run" : "달리다","walk" : "걷다","sit" : "앉다",
      "stand" : "서다","sleep" : "자다","read" : "읽다",
      "look" : "보다","do" : "하다","feel" : "느끼다","go" : "가다"},
    { "accumulated":"누적된","additional":"추가적인","adequate":"적당한",
    "administrative":"관리의","affordable":"알맞은","alternative":"대체 가능한",
    "annual":"해마다의","different":"다른","local":"지역의","social":"사회의"}
]
w_title = ["","명사","동사","형용사"]
# 함수선언
def w_quiz(choice):
    print("{}를 선택하셨습니다.".format(w_title[choice]))
    chk = input("퀴즈가 나갑니다. 준비되셨나요?(1.실행, 0.취소)")
    if chk == "1":
        # 1. words[choice] 에서 key값을 추출
        # 2. list타입으로 변경
        w_list = list(words[choice].keys()) #리스트 타입
        # 3. random함수를 써서, 5개 list추출
        ran_list = random.sample(w_list,5)
        # 4. 5개 list를 퀴즈에 넣으면 됨.
        count = 0
        # for key in words[choice]: #{딕셔너리} -> key
        for key in ran_list: #{딕셔너리} -> key
            # print(key,":",w_noun[key])
            answer = input("{} 단어의 뜻은?".format(key))
            if answer == words[choice][key]:
                print("정답입니다.")
                count += 1
            else:
                print("오답입니다. 정답 : {}".format(words[choice][key]))
        print("정답개수 : {}, 오답 : {} ".format(count,len(ran_list)-count))
    else:
        print("퀴즈를 취소하셨습니다. 메뉴로 돌아갑니다.")
while True:
    print("[ 영단어 맞추기 프로그램 ]")
    print("-"*40)
    print("1. 명사")
    print("2. 동사")
    print("3. 형용사")
    print("0. 종료")
    print("-"*40)
    choice = int(input("원하는 번호를 입력하세요.>> ")) # 정수형으로 받음.
    if choice == 1:
        w_quiz(choice)
    elif choice == 2:
        w_quiz(choice)
    elif choice == 3:
        w_quiz(choice)
    else:
        print("프로그램을 종료합니다.")
        break


'''