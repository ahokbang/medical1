import operator

fruits = [ '바나나', '바나나', 
            '바나나', '딸기', '배', '사과', '딸기',
            '딸기', '딸기', '딸기', '사과', '바나나', '바나나',
            '바나나', '딸기', '배', '사과', '딸기',
            '딸기', '딸기', '딸기', '사과' ]
                                        
counter = {}
    
for fruit in fruits :
    if fruit not in counter :
        counter[fruit] = 0
    counter[fruit] += 1
print(counter)

# 정렬
print(sorted(counter.items(), key=operator.itemgetter(1), reverse=True))
