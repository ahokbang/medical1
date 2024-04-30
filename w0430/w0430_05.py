import oracledb

# 평균점수를 입력 받아 입력한 평균점수 이상의 학생을 출력하시오.
# 반복해서 진행하고 -1을 입력하면 프로그램을 종료하시오.
# while True: 
#     conn = oracledb.connect(user="ora_user", password="1111", dsn="localhost:1521/xe")
#     cursor = conn.cursor()  
#     search = input("평균 점수를 입력하세요(-1 : 프로그램 종료). >> ")
#     if search == '-1':
#         print("프로그램을 종료합니다.")
#         conn.close()    
#         break
#     sql = f"select * from stu_score where avg>={search}"
#     cursor.execute(sql)
#     data = cursor.fetchall()        
#     for d in data:
#         print(d)
#     print('-'*40) 
#     print("검색된 데이터 개수 : ", len(data))
#     print()

# 평균점수를 입력 받아 입력한 평균점수 이상, 이하를 선택해서 학생을 출력하시오.
# 반복해서 진행하고 -1을 입력하면 프로그램을 종료하시오.        
while True: 
    conn = oracledb.connect(user="ora_user", password="1111", dsn="localhost:1521/xe")
    cursor = conn.cursor()  
    search = input("평균 점수를 입력하세요(-1 : 프로그램 종료). >> ")
    if search == '-1':
        print("프로그램을 종료합니다.")
        conn.close()    
        break
    
    choice = input("평균점수 이상, 이하를 선택하세요(1: 이상, 2: 이하). >> ")
    if choice == '1':
        sql = f"select * from stu_score where avg>={search}"
        cursor.execute(sql)
        data = cursor.fetchall()
        for d in data:
            print(d)
    elif choice == '2':
        sql = f"select * from stu_score where avg <={search}"
        cursor.execute(sql)
        data = cursor.fetchall()
        for d in data:
            print(d)
    else :
        print("번호를 다시 입력해주세요.")
    print('-'*40) 
    print("검색된 데이터 개수 : ", len(data))
    print()