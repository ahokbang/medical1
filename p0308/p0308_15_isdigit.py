# isdigit
# isalpha
# isalnum
# islower

# 영문자냐 숫자냐 빈공백이냐 이런거 많이 물어봐
# - 빈공간은 0으로 생각하기 쉽지만, 
#   컴퓨터는 빈공백을 무한대로 생각해서 데이터 계산이 안돼.
# - 프로그램에는 문제가 없지만 데이터적으로 문제가 있을 때 사용

print("1234" .isdigit()) # 숫자로 치환가능한지 확인
print("1234a" .isdigit()) # 숫자인지 확인
print("abc" .isalpha()) # 영문인지 확인
print("a1bc" .isalpha()) # 영문인지 확인
print("abc" .islower()) # 소문자인지 확인
print("abcD" .islower()) # 소문자인지 확인
print("ABC" .isupper()) # 대문자인지 
print("ABaC" .isupper()) # 대문자인지 
print(" " .isspace()) # 문자열이 공백인지 확인
print("    ab   c" .isspace()) # 빈 공백이 있는지 확인

