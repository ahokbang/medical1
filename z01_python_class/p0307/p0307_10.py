
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
print(words[1]) # => 딕셔너리가 나와

choice = 1 # 일 때,
print(words[choice]) #로 쓸 수 있어.

w_list = words[choice].keys()
print(words[choice].keys()) # 리스트
