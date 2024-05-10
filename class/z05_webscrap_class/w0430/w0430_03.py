import oracledb

# DB connect
conn = oracledb.connect(user="ora_user",password='1111', dsn='localhost:1521/xe')
cursor = conn.cursor()

# sql 실행
# employees 테이블에서 사번, 이름, 월급, 실제월급(=월급 + 월급*커미션), 월급(원화)(=월급*1410원) 출력
# 월급(원화)의 경우 천단위, 원화 표시
# sql = '''
# select employee_id, emp_name, salary, salary+(salary*nvl(commission_pct,0)),
# trim(to_char(salary*1410,'L999,999,999')) from employees
# '''
# cursor.execute(sql)
# data =  cursor.fetchall()

# print("[ 데이터 출력 ]")
# for d in data:
#     print(d)
#     print('-'*40)

# # 파이썬에서 원화 표시 붙이기
# sql = '''
# select employee_id, emp_name, salary, salary+(salary*nvl(commission_pct,0)),
# trim(to_char(salary*1410,'999,999,999')) from employees
# '''
# cursor.execute(sql)
# data =  cursor.fetchall()
    
# print("[ 데이터 출력 ]")
# print('-'*40)
# print('사원번호\t사원명\t월급\t실제월급\t월급(원화)')
# print('-'*40)
# for d in data:
#     # print(d[0]'\t'd[1]'\t'd[5])  \t 삽입 또는 end='\t\' 사용하면 옆으로 출력 가능
#     print(d[0], end='\t')
#     print(d[1], end='\t')
#     print(d[2], end='\t')
#     print(d[3], end='\t')
#     print("￦"+d[4].strip())

# 부서별 평균월급, 최대월급, 최소월급
sql = '''
select department_id, round(avg(salary),2), round(max(salary),2), round(min(salary),2) from employees
where department_id is not null
group by department_id
order by department_id
'''
cursor.execute(sql)
data =  cursor.fetchall()    
print("[ 데이터 출력 ]")
print('부서ID 평균월급 최대월급 최소월급')

for d in data:
    print(d[0], end='\t')
    print(d[1], end='\t')
    print(d[2], end='\t')
    print(d[3])

print('-'*40)

conn.close()
