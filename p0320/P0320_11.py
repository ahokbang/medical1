def func(n, *val, a=2) :  # 키워드 변수는 가변변수 뒤에!
                          # 기본-가변-키워드변수 순서!! 중요 아니면 에러
    for i in range(n) :
        for v in val :
            print(v)

func(1, "안녕", "안녕하세요.", '반갑습니다.')

print(1, 2, 3, 4, 5, sep = ",", end =" ") 
# 함수 가변매개변수             키워드매개변수





print(range(10))
a = range(10)
print(a)

# 리스트 만드는 법
print(list (range(10))) # 첫번째 방법
print([ i for i in range(10) ]) # 두번째 방법


# for반복문: 반대로 반복하기
for i in range(1,10+1,2) :
    print(i)
    
for i  in range(10,1-1,-1):
    print(i)
    
# 딕셔너리의 items()함수
a_dic = {"a":"홍길동", "b":'유관순', 'c':'이순신'}
for key in a_dic :
    print(a_dic[key])
for key in a_dic.keys():
    print(key)
for val in a_dic.values():
    print(val)
for k,v in a_dic.items():
    print(k,v)