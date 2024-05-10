# 명사, 동사, 형용사 10개씩 넣어서 영단어 맞추기 프로그램 만들기

w_noun = { 
          "airplane" : "비행기", 
          "apple" : "사과",
          "bakery" : "빵집",
          "banana" : "바나나",
          "bank" : "은행",
          "bean" : "콩",
          "bicycle" : "자전거",
          "boat" : "보트",
          "bowl" : "그릇",
          "bus" : "버스"  
}

w_verb = {
           "fly" : "날다",
           "boil" : "끓이다",
           "fall" : "떨어지다",
           "owe" : "빚지다",
           "grow" : "성장하다",
           "chew" : "씹다",
           "bite" : "물다",
           "happen" : "발생하다",
           "drink" : "마시다",
           "wash" : "씻다"    
}

w_ad = {
         "exquisite" : "고상한",
         "beautious" : "예쁜",
         "dainty" : "앙증맞은",
         "bonny" : "보기에 좋은",
         "trig" : "말끔한",
         "spruce" : "단정하고 똑똑해 보이는",
         "radiant" : "빛을 발하는",
         "dapper" : "옷을 잘 입는",
         "splendid" : "화려한",
         "elegant" : "품위 있는"    
}

w_title = ["", "명사", "동사", "형용사"]

while True : 
    print("[ 영단어 맞추기 프로그램 ]") 
    print("1. 명사")
    print("2. 동사")
    print("3. 형용사")
    print('-'*40)
    choice = input("원하는 번호를 입력하세요. >> ")
    
    if choice == "1" :
        print("{}를 선택하셨습니다." .format(w_title[int(choice)]))
        choice = input("퀴즈가 나갑니다. 준비되셨나요? (1. 실행 0. 취소)")
        cnt_pass = 0
        if choice == '1' :
            # 퀴즈 프로그램
            # key-영문, value-한글
            '''
            print(w_noun.keys()) # 전체 key, 아래 for 문과 동일
            for key in w_noun :
                print(key) 
            # print(w_noun.values()) # 전체 value
            ''' 
            # 선생님은 여기에 count = 0 자리 
            for key in w_noun :
                # print(key, ":", w_noun[key])
                answer = input("{} 단어의 뜻은?" .format(key))
                if answer == w_noun[key] :
                    print("정답입니다.")
                    cnt_pass += 1
                else :
                    # 내 풀이 : print("정답이 아닙니다.")
                    # 선생님 풀이 
                    print("정답이 아닙니다. 정답 : {}" .format(w_noun[key]))
            # 내 풀이 : print("총 {}문제 맞추셨습니다." .format(cnt_pass))
            # 선생님 풀이
            print("정답개수 : {}, 오답 : {}" .format(cnt_pass, len(w_noun)-cnt_pass))
        else :
            print("퀴즈를 취소하셨습니다. 메뉴로 돌아갑니다.")
            break
        
    if choice == "2" :
        print("{}를 선택하셨습니다." .format(w_title[int(choice)]))
        choice = input("퀴즈가 나갑니다. 준비되셨나요? (1. 실행 0. 취소)")
        cnt_pass = 0
        if choice == "1" :
            for key in w_verb :
                answer = input("{} 단어의 뜻은?" .format(key))
                if answer == w_verb[key] :
                    print("정답입니다.")
                    cnt_pass += 1
                else : 
                    print("정답이 아닙니다. 정답 : {}" .format(w_verb[key]))
            print("정답개수 : {}, 오답 : {}" .format(cnt_pass, len(w_noun)-cnt_pass))
        else :
            print("퀴즈를 취소하셨습니다. 메뉴로 돌아갑니다.")
            break
    
    if choice == "3" :
        print("{}를 선택하셨습니다." .format(w_title[int(choice)]))
        choice = input("퀴즈가 나갑니다. 준비되셨나요? (1. 실행 0. 취소)")
        cnt_pass = 0
        if choice == "1" :
            for key in w_ad :
                answer = input("{} 단어의 뜻은?" .format(key))
                if answer == w_ad[key] :
                    print("정답입니다.")
                    cnt_pass += 1
                else : 
                    print("정답이 아닙니다. 정답 : {}" .format(w_ad[key]))
            print("정답개수 : {}, 오답 : {}" .format(cnt_pass, len(w_noun)-cnt_pass)) 
        else :
            print("퀴즈를 취소하셨습니다. 메뉴로 돌아갑니다.")
            break

