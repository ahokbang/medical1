from random import *
# 1 - 100 사이의 랜덤한 숫자를 만들어서 내가 입력한 값이 랜덤한 숫자랑 같으면 당첨(프로그램 종료.)
# 아니면 다시 입력해주세요.를 출력하는 프로그램을 만들어보세요.

# print(randint(1,100))
# print(randint(1,100))
# print(randint(1,100))
# print(randint(1,100))

''' 내가 푼 거 : 프로그램이 종료되지 않음. 
while True :
    n = int(input("숫자를 입력하세요. >> "))
    if n == randint(1,100) :
        print("축하합니다. 당첨입니다. 프로그램을 종료합니다.")
        break # 프로그램을 종료하지 않음: randint가 계속 바뀌기 때문이야
    else :
        print("당첨 숫자는 {} 입니다. 다시 입력해주세요." .format(randint(1,100)))
'''
'''
r = randint(1, 100)
while True :
    n = int(input("숫자를 입력하세요. >> "))
    if n == r :
        print("당첨입니다.")
    else :
        print("당첨 숫자는 {}입니다. 다시 입력해주세요." .format(r))
        

randint는 계속 바뀌니까 고정시켜 준 뒤에 해야해!!

# 인하씨가 알려준 거!
while True :
    r = randint(1,100) # 얘도 while 안으로 들어와야 해! 
    # print(r)
        n = int(input("숫자를 입력하세요. >> "))
    if n == r :
        print("축하합니다. 당첨입니다. 프로그램을 종료합니다.")
        break # 프로그램을 종료하지 않음: randint가 계속 바뀌기 때문이야
    else :
        print("당첨 숫자는 {} 입니다. 다시 입력해주세요." .format(r)) # 여기도 r로 바꿔주고
'''

''' 선생님 풀이
randNum = randint(1, 100) # 랜덤한 숫자 발생
while True :
    userInput = int(input("숫자를 입력해주세요. >> "))
    if randNum == userInput :
        print("당첨")
        break
    else :
        print("다시 입력해주세요.")
'''

# 입력한 숫자가 랜덤숫자보다 작으면 작습니다. 더 큰수를 입력해주세요.
# 입력한 숫자가 랜덤숫자보다 크면 더 작은 수를 입력해주세요.

randNum = randint(1, 100) # 랜덤한 숫자 발생

''' 내가 푼 거
while True :
    userInput = int(input("숫자를 입력해주세요. >> "))
    if randNum == userInput :
        print("당첨")
        break
    if randNum < userInput :
        print("작습니다. 더 큰수를 입력해주세요.")
    else :
        print("큽니다. 더 작은 수를 입력해주세요.")
'''

''' 선생님 풀이
while True :
    userInput = int(input("숫자를 입력해주세요. >> "))
    if randNum == userInput :
        print("당첨")
        break
    elif userInput > randNum :
        print("입력하신 숫자가 랜덤숫자보다 큽니다. 더 작은 수를 입력해주세요.")
    else :
        print("입력하신 숫자가 랜덤숫자보다 작습니다. 더 큰 수를 입력해주세요.")
'''

# 1. 현재 입력한 숫자 모두를 inputlist에 넣으세요.
''' 내가 푼 거
inputlist = []
while True :
    userInput = int(input("숫자를 입력해주세요. >> "))
    if randNum == userInput :
        print("당첨")
        break
    elif userInput > randNum :
        print("입력하신 숫자가 랜덤숫자보다 큽니다. 더 작은 수를 입력해주세요.")
    else :
        print("입력하신 숫자가 랜덤숫자보다 작습니다. 더 큰 수를 입력해주세요.")
    inputlist.append(userInput)
print(inputlist)        
'''

# 2. 10회 도전 후 프로그램이 종료가 되게 해주세요.
'''
inputlist = []
while True :
    userInput = int(input("숫자를 입력해주세요. >> "))
    if randNum == userInput :
        print("당첨")
        break
    elif userInput > randNum :
        print("입력하신 숫자가 랜덤숫자보다 큽니다. 더 작은 수를 입력해주세요.")
    else :
        print("입력하신 숫자가 랜덤숫자보다 작습니다. 더 큰 수를 입력해주세요.")
    inputlist.append(userInput)
    if len(inputlist) == 10 :
        print("프로그램이 종료됩니다.")
        break
print(inputlist)        
'''

# 3. 10회 도전이 실패한 사람에게 random 숫자 알려주기
inputlist = []
while True :
    userInput = int(input("숫자를 입력해주세요. >> "))
    inputlist.append(userInput) # 당첨된 숫자도 넣고 싶을 때는 if 밖에 넣어주거나 if, elif 사이사이에 넣어주면 돼
    # 이미 위에서 입력을 했으니까 당첨된 숫자가 포함돼.
    if randNum == userInput :
        print("당첨")
        break
    elif userInput > randNum :
        print("입력하신 숫자가 랜덤숫자보다 큽니다. 더 작은 수를 입력해주세요.")
    else :
        print("입력하신 숫자가 랜덤숫자보다 작습니다. 더 큰 수를 입력해주세요.")
    # ********** inputlist.append(userInput) 인풋리스트에 넣는 코드가 왜 여기가 아니지? **********
    if len(inputlist) == 10 :
        print("실패하셨습니다. 당첨숫자는 {}입니다. 프로그램이 종료됩니다." .format(randNum))
        break
print(inputlist)    

'''' 선생님 풀이
# 2. 10회 도전 후 프로그램이 종료가 되게 해주세요.
cnt = 0
inputlist = []
while cnt < 10 :
    userInput = int(input("{}번재 도전! 숫자를 입력해주세요. >> " .format(cnt)))
    inputlist.append(userInput) 
    cnt += 1
    
    if randNum == userInput :
        print("당첨")
        break
    elif userInput > randNum :
        print("입력하신 숫자가 랜덤숫자보다 큽니다. 더 작은 수를 입력해주세요.")
    else :
        print("입력하신 숫자가 랜덤숫자보다 작습니다. 더 큰 수를 입력해주세요.")

# 3. 10회 도전이 실패한 사람에게 random 숫자 알려주기
if cnt == 0 :
    print("10회 입력을 초과하셨습니다. 정답은", randNum)
print("사용자가 입력한 숫자들은: ", inputlist)
'''