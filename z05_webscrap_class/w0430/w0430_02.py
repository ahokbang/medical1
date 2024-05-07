import oracledb

# sql
conn = oracledb.connect(user="ora_user",password="1111", dsn="localhost:1521/xe")
cursor = conn.cursor() # db와 연결되어 지시자 생성

# board 테이블 id 포함 모든 컬럼, member 테이블의 name 컬럼을 가져와 출력하시오.
# board 테이블에는 id만 있고, name은 member 테이블에 있음
'''
sql = "select bno, a.id, name, btitile, bcontent, bdate, bgroup, bstep, bindent, \
bhit, bfile from board01 a, member b where a.id = b.id"
cursor.execute(sql) # cursor에 select한 결과값을 저장(결과값 : list)
data = cursor.fetchall() # fetchall() : 모든 데이터 가져옴. 
# ftechone() : 1개의 데이터 가져옴.

print("[ 모든 데이터 출력 ]")
for d in data:
    print(d)
    print('-'*20)
print('-')
print("타입 : ", type(data))
conn.close() # 데이터베이스 연결해제 꼭 해주기!


'''

# stu_score에서 avg가 90점 이상 A, 80점 이상 B, 70점 이상 C, 60점 이상 D, 60점 미만 F
# 학번, 이름, 합계, 평균, 학점 출력하시오. 

# sql = '''select no, name, total, avg,
# case
# when avg >= 90 then 'A'
# when avg >= 80 then 'B'
# when avg >= 70 then 'C'
# when avg >= 60 then 'D'
# else 'F' end as grade 
# from stu_score'''  # '''로 할 수 있어. ""쓸 경우 역슬래시(\) 사용 필요
# cursor.execute(sql)
# data = cursor.fetchall()
# print('-'*50)
# for d in data:
#     print(d)
#     print('-'*50)

# sql = "select * from stu_score"
# # 평균을 가지고 파이썬에서 프로그램하여 학점을 출력하시오.
# # 학번, 이름, 합계 평균, 학점
# cursor.execute(sql)
# data = cursor.fetchall()
# print('-'*50)
# # 선생님 코드
# for d in data:
#     print(d)
#     # print("학번 : ", d[0])
#     # print("이름 : ", d[2])
#     # print("합계 : ", d[5])
#     print("평균 : ", d[6])
#     if d[6] >= 90:
#         print("학점 : ", "A")
#     elif d[6] >= 80:
#         print("학점 : ","B")
#     elif d[6] >= 70:
#         print("학점 : ","C")
#     elif d[6] >= 60:
#         print("학점 : ","D")
#     else :
#         print("학점 : ","F")
#     print('-'*50) 

#  # 내 코드   
# for d in data:
#     print(d[0])
#     print(d[2])
#     print(d[5])
#     print(d[6])
#     if d[6] >= 90:
#         print("A")
#     elif d[6] >= 80:
#         print("B")
#     elif d[6] >= 70:
#         print("C")
#     elif d[6] >= 60:
#         print("D")
#     else :
#         print("F")
#     print('-'*50)


# salary 평균을 출력하시오. 
sql = "select round(avg(salary),2) from employees"
cursor.execute(sql)
data = cursor.fetchone()
# print("salary의 평균 : ", data) # (6461.8317757009345, ) 이렇게 출력되니까 아래 처럼 코드 작성
print("salary의 평균 : ", data[0])


conn.close() # 데이터베이스 연결해제 꼭 해주기!