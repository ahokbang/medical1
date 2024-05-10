# 돈을 입력 받아 5만원권, 만원권, 오천원권, 천원권으로 교환해서 출력

money = int(input("교환할 금액을 입력하세요. : "))

c50000, c10000, c5000, c1000 = 0, 0, 0, 0

c50000 = money//50000
c10000 = (money%50000)//1000
c5000 = ((money%50000)%10000)//5000
c1000 = (((money%50000)%10000)%5000)//1000

print('교환할 금액: {:,}' .format(money)) # :, 넣으면 천의 자리 구분해줘
print('50000원 : {}' .format(c50000))
print('10000원 : {}' .format(c10000))
print('5000원 : {}' .format(c5000))
print('1000원 : {}' .format(c1000))

# 누적을 이용해서 출력할 수도 있어. 

money = int(input("교환할 금액을 입력하세요. : "))
print("교환할 금액: {}" .format(money))
money = money//50000
print("'50000원 : {}" .format(money))
money = (money%50000)//1000
print("'10000원 : {}" .format(money))
