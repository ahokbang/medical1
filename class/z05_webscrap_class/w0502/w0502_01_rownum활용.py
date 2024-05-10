# port : 컴퓨터 상의 사용하고 있는 프로그램의 주소
# IP : 네트워크상의 내 주소

import oracledb
import math

conn = oracledb.connect(user="ora_user", password="1111", dsn="localhost:1521/xe")
cursor = conn.cursor()
# cursor는 오라클 프로그램이 열리면 나타나는 커서


# 최초 번호 : 데이터 가져오는 방법
num = 0
perCount = 10  # 20개씩 들고오려면 (num-1)*20+1, perCount 숫자 변경
# startrow = (num-1)*perCount+1 #  1, 11, 21, 31, ..., 
# endrow = startrow+perCount-1  # 10, 20, 30, 40, ..
startrow = 1
endrow = 10
limit = 0

# 학생 성적표 가져오기
# 먼저 학생의 이름으로 검색
search = input("찾고자하는 학생 이름을 입력하세요. >> ")

sql = f'''select count(*) from (select row_number() over(order by no) rnum,
        a.* from stu_score a where id like '%{search}%')
        '''
cursor.execute(sql)
all_count = cursor.fetchone() # 튜플로 넘어와 
limit = math.ceil(all_count[0]/perCount) # 나눈 값이 3.1인 경우 4번 돌아야 해

# 무한반복
while True:
    if num != 0:
        print("1. < 이전 ", end=' ')
        print("2. 다음 > ")
        no = input("원하는 번호를 입력하세요. >> ")
        if no ==  "1": 
            if num == 1 : 
                num = 1
                print("첫 페이지입니다.")
            else : num -= 1
        else : 
            num += 1
            if num > limit : 
                num = limit
                print("마지막 페이지 입니다.")
            
        # print("현재번호 : ", num)
        
        # 데이터 가져오는 방법 (개수로 끊기)
        startrow = (num-1)*perCount+1 #  1, 11, 21, 31, ..., 
        endrow = startrow+perCount-1  # 10, 20, 30, 40, ...
    else : num += 1 # 최초 실행 시
        
    
    sql = f'''select * from (select row_number() over(order by no) rnum, a.* 
            from stu_score a where id like '%{search}%')
            where rnum>={startrow} and rnum<={endrow}
            '''
    cursor.execute(sql)
    data = cursor.fetchall()

    # 10개씩 나워서 보여주도록 구성
    print('[ 학생 검색 데이터 ]')
    for d in data:
        print(d)
    
    print('-'*30)
    print("검색된 페이지 수 : ", (num-1), " / 검색된 데이터 수 : ", all_count[0])
    


