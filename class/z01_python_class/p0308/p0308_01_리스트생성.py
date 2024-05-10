# 튜플은 리스트랑 똑같다. 단 수정(삭제 포함)이 안된다.

list = []
# 1 - 10까지 입력해보세요.
# 리스트 기본 문법 : 속도 제일 느려
for i in range(10) :
    list.append(i+1)
print(list)
print()
# 컴프리헨션 방법: 속도 제일 빨라
list = [i for i in range(1,11)]
print(list)
print()
# 3. 공간 미리 만들기 
list = [0] * 10 # 공간 미리 10개 만들어 놓기. ********** 0 넣는 거 중요! **********
for i in range(10) :
    list[i] = i+1
print(list)