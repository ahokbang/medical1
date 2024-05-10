fruits = ['딸기', '사과', '자몽', '포도', '수박','자몽']
                                                  # 이 자몽을 삭제하고 싶어
# 만약에 자몽을 삭제하고 싶다.
# 리스트명.remober('요소명')
print(fruits)
# fruits.remove('자몽')
print(fruits) # 첫번재 자몽이 삭제 돼 ['딸기', '사과', '포도', '수박', '자몽']
# del(리스트명[번호]) : 위치 지정해서 그 위치의 요소 삭제
del(fruits[5])
print(fruits)

for i, f in enumerate(fruits) :
    print('{}는 {}번째에 있습니다.' .format(f, i))
    