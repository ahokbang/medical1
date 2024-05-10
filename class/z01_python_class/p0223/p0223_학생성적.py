print('-'*35)
print('[학생성적프로그램]')
print('-'*35)
print("1. 학생성적입력") # 오늘의 목표 1
print("2. 학생성적수정")
print("3. 학생성적삭제")
print("4. 학생성적전체출력") # 오늘의 목표 2
print("5. 학생성적검색출력")
print("6. 등수처리")
print("0. 프로그램 종료")
print('-'*35)
choice = int(input("원하는 번호를 입력하세요. >> ")) 
# int 없어도 돼. 단, int 유무에 따라 조건문이 달라져.

# 만약에 choice가 1이면 [학생성적입력을 선택하셨습니다.] 출력

if choice == 1: 
    ''''
    ********** choice = int(input("원하는 번호를 입력하세요. >>")에서 int가 있으므로 1에 ''없어. 
    choice == input("원하는 번호를 입력하세요. >> ") 처럼 int가 없으면,
    if choice == '1' 처럼 1에 ''있어야 해. 꼭 기억해야해 **********
    '''
    print("학생성적입력을 선택하셨습니다. ")
elif choice ==2:
    print("학생성적수정을 선택하셨습니다.")
elif choice ==3:
    print("학생성적삭제를 선택하셨습니다.")
elif choice ==4:
    print("학생성적전체출력을 선택하셨습니다.")
elif choice ==5:
    print("학생성적검색출력을 선택하셨습니다.")
elif choice ==6:
    print("등수처리를 선택하셨습니다.")
elif choice ==0:
    print("프로그램 종료를 선택하셨습니다.")
else:
    print("잘못입력하셨습니다. 다시 입력해주세요.")
    
