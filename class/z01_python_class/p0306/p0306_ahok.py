students = [
            [1, "홍길동", 100, 100, 99, 299, 99.67, 1], 
            [2, "유관순", 99, 99, 998, 296, 98.67, 1], 
            [3, "이순신", 80, 80, 81, 241, 80.33, 1],
            [4, '김구', 100, 100, 90, 290, 96.67, 1],
            [5, '강감찬', 90, 70, 50, 210, 70.0, 1]
                                                ]
# 학생성적프로그램
for stu in students :
    for s in stu :
        print(s, end='\t')  # => 리스트의 모든 요소 값 출력(리스트의 리트값도 다 출력)
    print()
kors = 0
engs = 0
maths = 0
totals = 0
avgs = 0    
for j, stu in enumerate(students) :      
# enumerate : 리스트의 원소에 순서값을 부여해주는 함수
    kors = kors + stu[2]
    engs = engs + stu[3]
    maths += stu[4]
    totals += stu[5]
    avgs += stu[6]/len(students)
print('\t')
print('--\t합계\t{}\t{}\t{}\t{}\t{:.2f}' .format(kors, engs, maths, totals, avgs))

''' 출력 
[학생성적 출력]
1       홍길동  100     100     99      299     99.67   1
2       유관순  99      99      998     296     98.67   1
3       이순신  80      80      81      241     80.33   1
4       김구    100     100     90      290     96.67   1
5       강감찬  90      70      50      210     70.0    1

--      합계    469     449     1318    1336    267.20
'''

# 학생검색