'''
입력 : 이름, 아이디, 비밀번호 (input)
5명을 입력받아서 member 리스트를 만드세요.

member 리스트를
이름    아이디  비밀번호
홍길동  aaaa    1111
이순신  bbbb    2222
유관순
김구

형식으로 출력해보세요. for문 사용
'''
member = [] # [[홍길동, aaa, 1111], [유관순, bbb, 111]]

for i in range(5) : 
    name = input("이름을 입력하세요. >> ")
    id = input("아이디를 입력하세요. >> ")
    pw = input("패스워드를 입력하세요. >> ")
    
    m = [name, id, pw] # 이름/id/pw를 리스트로 묶기 위함. 리스트로 묶지 않으면 이름-id-pw가 순서대로 계속 append 돼
    
    member.append(m)
# print(member)

# member 리스트를 사용해서 출력 
print("이름\t아이디\t비밀번호")
print("{}\t{}\t{}".format(member[0][0], member[0][1], member[0][2]))
print("{}\t{}\t{}".format(member[1][0], member[1][1], member[1][2]))
print("{}\t{}\t{}".format(member[2][0], member[2][1], member[2][2]))
print("{}\t{}\t{}".format(member[3][0], member[3][1], member[3][2]))
print("{}\t{}\t{}".format(member[4][0], member[4][1], member[4][2]))

# for문 사용해서 만들어보기; ********** 모르겠어 **********
# print("이름\t아이디\t비밀번호")
# for i in range(5) :
#     print("{}\t{}\t{}" .format(member[i][i])) # error ********** 아 다 왔는데... 아쉽 **********


'''
선생님 답
member = []
for i range(5) : 
    name = input("이름을 입력하세요. >> ")
    uid = input("아이디를 입력하세요. >> ")
    upw = input("비밀번호를 입력하세요. >> ")
    m = [name, uid, upw]
    member.append(m)
print

# n명 입력은??

print(member) # [[홍길동, aaaa, 1111], [유관순, bbbb, 2222], ... ]

# member 리스트를 사용해서 출력 
print("이름\t아이디\t비밀번호")
print("{}\t{}\t{}".format(member[0][0], member[0][1], member[0][2]))
print("{}\t{}\t{}".format(member[1][0], member[1][1], member[1][2]))
print("{}\t{}\t{}".format(member[2][0], member[2][1], member[2][2]))
print("{}\t{}\t{}".format(member[3][0], member[3][1], member[3][2]))
print("{}\t{}\t{}".format(member[4][0], member[4][1], member[4][2]))


# for문 사용
print("이름\t아이디\t비밀번호")
a = len(member) # 숫자가 나와, 5
for i in range(5) : # 또는 for i in range(len(memeber))
    print("{}\t{}\t{}" .format(member[i][0], memeber[i][1], memeber[i][2]))
    
'''