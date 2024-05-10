'''
# 빈 리스트 생성
cont = []

c1 = input('1. 나라를 입력해주세요. >> ')
c2 = input('2. 나라를 입력해주세요. >> ')
c3 = input('3. 나라를 입력해주세요. >> ')
c4 = input('4. 나라를 입력해주세요. >> ')

# [미국, 영국, 일본, 중국] 출력
# cont.appent(변수)
#print(cont)

cont.append(c1)
cont.append(c2)
cont.append(c3)
cont.append(c4)
print(cont)

# 선생님 답
# 1.
cont = [c1, c2, c3, c4]
print('방법1 : ', cont)

# 2.  : 내가 푼 답이랑 동일
contA = []
contA.append(c1)
contA.append(c2)
contA.append(c3)
contA.append(c4)
print('방법 2: ', contA)
'''

# 미국 - 영국 - 프랑스 - 이탈리아
# 1.
country = []
country.append('미국') # ********** 문자에 '' 하는 거 잊지 않기! **********
country.append('영국')
country.append('프랑스')
country.append('이탈리아')
print(country)

print('{}-{}-{}-{}' .format(country[0], country[1], country[2], country[3]))

# 2.
c1 = '미국'
c2 = '영국'
c3 = '프랑스'
c4 = '이탈리아'
print('{}-{}-{}-{}' .format(c1,c2,c3, c4))

# 3.
ctr = ['미국', '영국', '프랑스', '이탈리아']
print('{}-{}-{}-{}' .format(ctr[0], ctr[1], ctr[2], ctr[3]))



# 과일리스트 f = []에 내가 입력한 과일들로 리스틀르 채워보세요. 과일 3개 이상
f = []

# 1. 
'''
f.append(input("1. 과일을 입력하세요. >> "))
f.append(input("2. 과일을 입력하세요. >> "))
f.append(input("3. 과일을 입력하세요. >> "))
f.append(input("4. 과일을 입력하세요. >> "))
print(f)
print('내가 좋아하는 과일은 {}, {}, {}, {}입니다.' .format(f[0], f[1], f[2], f[3]))
'''

# 2. 
'''
f1 = input("1. 과일을 입력하세요. >> ")
f2 = input("2. 과일을 입력하세요. >> ")
f3 = input("3. 과일을 입력하세요. >> ")
f4 = input("4. 과일을 입력하세요. >> ")

f = [f1, f2, f3, f4]
print(f)
print('내가 좋아하는 과일은 {}, {}, {}, {}입니다.' .format(f[0], f[1], f[2], f[3]))
'''

#3. 
f1 = input("1. 과일을 입력하세요. >> ")
f2 = input("2. 과일을 입력하세요. >> ")
f3 = input("3. 과일을 입력하세요. >> ")
f4 = input("4. 과일을 입력하세요. >> ")

f.append(f1)
f.append(f2)
f.append(f3)
f.append(f4)
print('내가 좋아하는 과일은 {}입니다.' .format(f))
print('내가 좋아하는 과일은 {}, {}, {}, {}입니다.' .format(f[0], f[1], f[2], f[3]))


