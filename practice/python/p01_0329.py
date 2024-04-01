# 로또 프로그램

import random

nums = [i for i in range(1,45+1)]
print(nums)

my_nums=[]
for i in range(6):
    my_nums.append(int(input("로또번호 6개를 입력하세요. >> ")))

print(my_nums)
# lotto_nums = random.shuffle(nums, 6)
# print(lotto_nums)


