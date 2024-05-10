print("안녕하세요 제 이름은 홍길동입니다.")
print("저는 21살입니다.")

# 홍길동 대신 이순신으로 21대신 30으로 바꾸고 싶을 경우
# 우리가 아는 방법은, 다시 다 작성하는 것(지금까지 배운 것으로 할 수 있는)
print("안녕하세요 제 이름은 이순신입니다.")
print("저는 30살입니다.")

# 먼저, 문장 쪼개기
print("안녕하세요 제 이름은", "홍길동", "입니다.")
print("저는", 30, "살입니다.")

# 그 다음, 하나의 그릇을 만들어
name = "홍길동" # 홍길동을 이순신으로 바꾸면 돼
age = 21 # 21을 30으로 바꾸면 돼
print("안녕하세요 제 이름은", name, "입니다.")
print("저는", age, "살입니다.")

# 변수 입력
str1 = "hello" # true의 경우 색이 달라. 즉 파이썬에서 이미 변수로 사용하고 있어
print(str1)
var1 = 2
print(var1)
str2 = "world"

print(str1, str2)
print(str1+str2)
print(str1+' '+str2) # 공백 넣고 싶을 때; 따옴표 사이 공백

var4 = 100
var3 = var4 # var4=100이므로 var3=100
var2 = var3 # var2=100
var1 = var2 # var1=100 
print(var1)
print("var1 :", var1)
var4 = 200
print("var4:", var4)
print("var1:", var1) # 순차적으로 바뀌므로 var1은 변하지 않음

# 변수를 이용해서 다음 문장을 출력해보세요.
# 변수명: fruit
# "포도", "딸기", "수박" 순으로 입력
# 출력문장 >> 나는 포도를 좋아합니다.
fruit = "포도"
fruit = "딸기"
fruit = "수박"

fruit = "포도"
print("나는",fruit,"를 좋아합니다.") 
# 띄어쓰기가 거슬린다면,
print("나는 "+fruit+"를 좋아합니다.")
print("%s"%"나는", fruit, "%s"%"를 좋아합니다.")

# 변수명: city
# 출력할 문장: 나는 (서울시)에 살고 있습니다.
city = "서울시"
print("나는 "+city+"에 살고 있습니다.")

# 변수명: animal
# 출력할 문장: (판다)가 제일 좋아요.
animal = "판다"
print(animal+"가 제일 좋아요")

