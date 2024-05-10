students = [
["홍길동", 90, 100, 99, 299, 99.97], 
["유관순", 80, 100, 99, 299, 99.97], 
["이순신", 100, 100, 99, 299, 99.97] 
]

kors = 0 
# students 2차원배열
# stu 1차원비열
for stu in students :
    for i, stu in enumerate(students) :
        print(i)
        print(students[i][1])
        # kors += stu[i][1]
    
print(kors)
