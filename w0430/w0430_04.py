import oracledb

conn = oracledb.connect(user="ora_user", password="1111", dsn="localhost:1521/xe")
cursor = conn.cursor()

# 프로그램을 반복하는 형태로 구성하고, -1을 입력하면 종료되도록 하시오.
while True:
    # 검색어 입력부분
    search = input("찾고자하는 이름을 입력하세요(-1 : 종료). >> ")
    # 홍길동
    # 홍에 관련된 이름 모두 검색되도록  구현하시오.
    if search == '-1':
        print("프로그램을 종료합니다.") 
        conn.close()   
        break
    else : 
        # 검색부분
        sql = f"select * from stu_score where name like '%{search}%'"
        cursor.execute(sql)
        data = cursor.fetchall()

        for d in data:
            print(d)       
        print('-'*40) 
        print("검색된 데이터 개수 : ", len(data))