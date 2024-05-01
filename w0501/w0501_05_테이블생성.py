import oracledb

# DB 연결
conn = oracledb.connect(user="ora_user", password="1111", dsn="localhost:1521/xe")
cursor = conn.cursor()

sql = "create table mem(id varchar2(30) primary key, pw number, name varchar2(30), mdate date)"
cursor.execute(sql)

# ddl 명령어 : create, alter, drop, trunate ==> commit 없음
# dml 명령어 : select, insert, update, delete ==> commit 있음

print("테이블 생성 완료")

# DB 연결해제
cursor.close()
conn.close()