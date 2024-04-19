import P0315_02

member = P0315_02.idpw()
print(member)

# mem.txt 파일에 
# aaa, 1111 저장하시오.

# 1. 파일열기
f = open("mem.txt", "w", encoding="utf-8")

# 2. 파일쓰기
# f.write("aaa, 1111\n")
# f.write("bbb, 2222\n")
# f.write("ccc, 3333\n")

# member 저장하기
for m in member :
    f.write("{},{} \n".format(m[0], m[1]))

# 3. 파일닫기
f.close()
