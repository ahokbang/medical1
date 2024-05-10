# ********** count, find 외우기 **********

ss = "파이썬 공부는 즐겁습니다. 공부가 모두 재미있지는 않습니다."
# 존재하는 문자가 몇번 나왔는지 확인: .count()

print(ss.count("공부")) # 2
print(ss.count("자바")) # 0 ; 없을 때는 0으로 출력

# 존재하는 문자열의 위치값 출력: .find()
print(ss.find("공부")) # 4 : 공부의 위치값 
'''
"파이썬 공부는 즐겁습니다. 공부가 모두 재미있지는 않습니다."
 0 1 2 34
'''
print(ss.find("자바")) # -1; 없을 때는 -1으로 출력
print(ss.find("공부", 7)) # 15; 문자열 7번째자리 이후부터 검색 시작해서 위치값 출력
print(ss.rfind("공부")) # 우측부터 카운팅, 역순
print("-"*20)
# .index()
print(ss.index("공부"))
# print(ss.index("자바")) # error ; 없을 때는 error
print(ss.index("재미")) 
print(ss.rindex("재미")) # 우측부터 카운팅, 역순

# .startswith()
print(ss.startswith("파이썬")) # 시작하는 문자열이 맞으면 True
print(ss.startswith("자바")) # 시작하는 문자열이 틀리면 False

# .endswith()
print(ss.endswith("않습니다")) # 끝나는 문자열이 맞으면 True
print(ss.endswith("재미")) # 끝나는 문자열이 틀리면 False