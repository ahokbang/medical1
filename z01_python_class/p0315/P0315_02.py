# 
import random
def idpw () :
    eng = "abcdefghijklmnopqrstuvwxyz"
    pw = "1234567890"
    e_list = []
    p_list = []
    member = [['aaa', '1111']]
    for i in range(10) :
        temp1 = random.choice(eng)
        temp2 = random.choice(eng)
        temp3 = random.choice(eng)
        temp4 = random.choice(pw)
        temp5 = random.choice(pw)
        temp6 = random.choice(pw)
        temp7 = random.choice(pw)
        member.append([temp1+temp2+temp3, temp4+temp5+temp6+temp7])
    return member
'''
# 랜덤함수를 사용하여 3자리 아이디 10개 생성해서 e_list에 추가하시오.
for i in range(10) :
    # sample 사용 : 단어배열에 중복 없어
    a = random.sample(eng, k=3) 
    e_list.append(a[0]+a[1]+a[2])
    
    # choice 사용: 단어 배열에 중복 있어
    a1 = random.choice(eng)
    a2 = random.choice(eng)
    a3 = random.choice(eng)
    e_list.append(a1+a2+a3)  
    '''
'''
print(e_list)

# 랜덤함수를 사용하여 4자리 패스워드를 10개 생성해서 p_list에 추가하시오.
for j in range(10) :
    n = random.sample(pw, k=4) 
    # print(n)
    p_list.append(n[0]+n[1]+n[2]+n[3])
print(p_list)
'''
'''
# member에 넣고 싶어.
for i in range(10) :
    temp1 = random.choice(eng)
    temp2 = random.choice(eng)
    temp3 = random.choice(eng)
    temp4 = random.choice(pw)
    temp5 = random.choice(pw)
    temp6 = random.choice(pw)
    temp7 = random.choice(pw)
    member.append([temp1+temp2+temp3, temp4+temp5+temp6+temp7])
print(member)
'''