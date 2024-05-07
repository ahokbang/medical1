-- [ ����Ŭ ���� ]
-- [ 1 ] �������(employees) ���̺���
-- �����ȣ, �̸�, �޿�, �μ�, �Ի���, ����� �����ȣ�� ����Ͻÿ�.
-- �� �� �̸��� �̸��� ������ �����Ͽ� Name�̶�� ��Ī���� ����Ͻÿ�.

select * from employees;
select * from departments;
select employee_id, emp_name, salary, department_name, hire_date, a.manager_id 
from employees a, departments b
where a.department_id = b.department_id;

select employee_id, emp_name||'/'||job_id "Name", salary, department_name, hire_date, a.manager_id 
from employees a, departments b
where a.department_id = b.department_id;
-- [tc �߰� Ǯ��]
select employee_id, emp_name||'/'||job_id "Name", salary, department_id, hire_date, manager_id 
from employees;


-- [ 2 ] �������(employees) ���̺���
-- ����� �̸��� ���� Name, ������ Job, �޿��� Salary, 
-- ������ $100 ���ʽ��� �߰��Ͽ� ����� ���� Increase Ann_Salary,
-- �޿��� $100 ���ʽ��� �߰��Ͽ� ����� ������ Increase Salary��� ��Ī�� �ٿ� ����Ͻÿ�.

select emp_name "Name", job_id "Job", salary "Salary", 
(salary*12)+100 "Increase Ann_Salary", salary+100 "Increase Salary"
from employees;
-- [tc �߰� Ǯ��]
select emp_name "Name", job_id "Job", salary "Salary", 
(salary*100)*12 "Increase Ann_Salary" from employees;


-- [ 3 ] H R �μ����� ���� �� ������ �޿� ���� ������ �ۼ��Ϸ��� �Ѵ�. 
-- �������(Employees) ���̺��� �޿��� $7,000~$10,000 ���� �̿��� ����� 
-- �̸��� ��(Name���� ��Ī) �� �޿��� �޿��� ���� ������ ����Ͻÿ�(75��).
select emp_name "Name", salary from employees
where salary<7000 or salary>10000
order by salary;

-- [tc �߰� Ǯ��]
-- ������ 7000~10000 ������ �ִ� ���
select emp_name "Name", salary from employees
where salary between 7000 and 10000
;
-- ������ 7000~10000 ���� �ܿ� �ִ� ��� : not between
select emp_name "Name", salary from employees
where salary not between 7000 and 10000
;


-- [ 4 ] ����� ��(last_name) �߿� ��e�� �� ��o�� ���ڰ� ���Ե� ����� ����Ͻÿ�. 
-- �̶� �Ӹ����� ��e or o Name���̶�� ����Ͻÿ�(8��).
select emp_name as "e or o Name" from employees
where emp_name like '%e%' or emp_name like '%o%';

-- [tc �߰� Ǯ��]
-- - emp_name�� ���� first name�� last name�� ù ���ڰ� �빮���̱� ������ emp_name�� �ҹ��ڷ� ��ȯ �� �˻�
select emp_name as "e or o Name" from employees
where lower(emp_name) like '%e%' or lower(emp_name) like '%o%'
;


-- [ 5 ] �̹� �б⿡ 60�� IT �μ������� �ű� ���α׷��� �����ϰ� �����Ͽ� ȸ�翡 �����Ͽ���. 
-- �̿� �ش� �μ��� ��� �޿��� 12.3% �λ��ϱ�� �Ͽ���. 
-- 60�� IT �μ� ����� �޿��� 12.3% �λ��Ͽ� ������(�ݿø�) ǥ���ϴ� ������ �ۼ��Ͻÿ�. 
-- ������ �����ȣ, ���� �̸�(Name���� ��Ī), �޿�, �λ�� �޿�(Increase Salary�� ��Ī)������ ����Ͻÿ�(5��).
select employee_id, emp_name "Name", salary, salary+round(salary*0.123,-1) "Increase Salary"
from employees
where department_id = 60
;

-- [tc �߰� Ǯ��]
select employee_id, emp_name "Name", department_id, salary, round(salary+(salary*0.123)) "Increase Salary"
from employees
where department_id = 60
;


-- [ 6 ] ��� ����� ������ ǥ���ϴ� ������ �ۼ��Ϸ��� �Ѵ�. 
-- ������ ����� �̸��� ��(Name���� ��Ī), �޿�, ���翩�ο� ���� ������ �����Ͽ� ����Ͻÿ�. 
-- ���翩�δ� ������ ������ ��Salary + Commission��, ������ ������ ��Salary only����� ǥ���ϰ�, 
-- ��Ī�� ������ ���̽ÿ�. ���� ��� �� ������ ���� ������ �����Ͻÿ�(107��).
select emp_name "Name", salary,
case
when commission_pct is null then 'Salary only'
else 'Salary + Commission'
end as "Commission"
from employees
order by salary desc
;

-- [tc �߰� Ǯ��]
-- ���1 : case when then
select emp_name, salary,salary+nvl(salary*commission_pct,0) comm_salary, commission_pct ,
-- case when then
case 
when commission_pct is null then 'Salary only' -- then �ڿ��� ', "�� ����
when commission_pct is not null then 'Salary + Commission'
end as "commission_isNull"
from employees
order by salary desc
;
-- ���2 : decode
select emp_name, salary,salary+nvl(salary*commission_pct,0) comm_salary, commission_pct ,
-- decode(salary
-- '3000', 'A',         ==> salary�� 3000�̸� A, 4000dlaus B
-- '4000', 'B',
-- '5000', 'C',
-- )
-- decode(department_id
-- '10', 'A',       
-- '20', 'B',
-- '30', 'C',
-- ) as dept
-- nvl2: nvl2(commission_pct,'null�� ��� ����', 'null�� �ƴ� ��� ����')
-- nvl2(commission_pct, 'Salary + Commission','Salary only')
 decode(commission_pct, null,'Salary only','Salary + Commission')
from employees
order by salary desc
;
select emp_name, salary,salary+nvl(salary*commission_pct,0) comm_salary, commission_pct ,
decode(department_id,
'10', 'A',     
'20', 'B',
'30', 'C')
as dept
from employees
order by salary desc
;
-- ���3: nvl2
select emp_name, salary,salary+nvl(salary*commission_pct,0) comm_salary, commission_pct ,
-- nvl2: nvl2(commission_pct,'null�� ��� ����', 'null�� �ƴ� ��� ����')
nvl2(commission_pct, 'Salary + Commission','Salary only')
from employees
order by salary desc
;


-- [ 7 ] �� ����� �Ҽӵ� �μ����� �޿� �հ�, �޿� ���, �޿� �ִ�, �޿� �ּڰ��� �����ϰ��� �Ѵ�. 
-- ���� ��°��� ���� �ڸ��� �� �ڸ� ���б�ȣ, $ ǥ�ÿ� �Բ� �Ʒ��� ���� ����Ͻÿ�. 
-- ��, �μ��� �Ҽӵ��� ���� ����� ���� ������ �����ϰ�, ��� �� �Ӹ����� ���� �׸�ó�� ��Ī(alias) ó���Ͻÿ�(11��).
-- ��� �� �Ӹ����� "�׷��Լ���"�� ��Ī(alias) ó���Ͻÿ�(11��).
select department_id, to_char(sum(salary),'$999,999') sum, to_char(avg(salary),'$999,999') avg, 
to_char(max(salary),'$999,999') max ,to_char(min(salary),'$999,999') min from employees
where department_id is not null
group by department_id;

-- [tc �߰� Ǯ��]
select department_id, 
to_char(sum(salary),'$000,999,999') sum_sal, 
to_char(round(avg(salary),2),'$000,999,999') 
avg_sal, to_char(max(salary),'$000,999,999') max_sal, 
to_char(min(salary),'$000,999,999') min_sal 
from employees
group by department_id
;


-- [ 8 ] ������� ������ ��ü �޿� ����� $10,000���� ū ��츦 ��ȸ�Ͽ� ������ �޿� ����� ����Ͻÿ�. 
-- �� ������ ���(CLERK)�� ���Ե� ���� �����ϰ� ��ü �޿� ����� ���� ������� ����Ͻÿ�(7��).
select job_id, avg(salary) from employees
where job_id not in ('CLERK')
group by job_id 
having avg(salary) >10000 
order by avg(salary) desc
;
-- [tc �߰� Ǯ��]
-- ������ --> ���޺�, job_id
select avg(salary) from employees
;
select job_id, avg(salary) from employees
-- where : �Ϲ� �÷��� ������ �ִ� ��
where job_id not like '%CLERK%'
group by job_id
-- having : �׷��÷��� ������ �ִ� ��
having avg(salary)>10000
;


-- [ 9 ] �� ����� ���� ������ ���踦 �̿��Ͽ� ������ ���� ������ ������ �ۼ��ϰ��� �Ѵ�.
-- (��) ȫ�浿�� ��տ��� �����Ѵ� �� Eleni Zlotkey report to Steven King
-- � ����� �������� �����ϴ��� �� ���� �����Ͽ� ����Ͻÿ�.
-- ��, ������ ��簡 ���� ����� �ִٸ� �� ������ �����Ͽ� ����ϰ�, ����� �̸��� ���� �빮�ڷ� ����Ͻÿ�(107��).
select * from employees;
select a.employee_id, a.emp_name, a.manager_id, upper(b.emp_name) "manager_name" from employees a, employees b
where a.manager_id = b.employee_id 
order by a.employee_id
;

-- [tc �߰� Ǯ��]
-- - ��, ������ ��簡 ���� ����� �ִٸ� �� ������ �����Ͽ� ����ϰ�, ====> outer join ���
select a.employee_id, a.emp_name, a.manager_id, b.emp_name
from employees a, employees b
where a.manager_id=b.employee_id(+) -- null�� ���� �ʿ� (+) �߰�
order by a.employee_id
;


-- [ 10 ] Employees, Departments ���̺��� ������ �ľ��� �� 
-- ��� ���� �ټ� �� �̻��� �μ��� �μ��̸��� ��� ���� ����Ͻÿ�. �̶� ��� ���� ���� ������ �����Ͻÿ�(5��).
select department_id from employees;
select * from departments;

select a.department_id, department_name, count(a.department_id) from employees a, departments b
where a.department_id = b.department_id
group by a.department_id
having count(a.department_id)>= 5
order by count(a.department_id)
;

-- [tc �߰� Ǯ��]
-- 1. �μ���ȣ, �����
-- 2. ����� >= 5
-- 3. ������� ����
-- �μ��� �ο�
select department_id, count(department_id) from employees
group by department_id
having count(department_id)>=5
order by count(department_id) desc
;


--[�߰� ����1] HR �μ��� � ����� �޿������� ��ȸ�ϴ� ������ �ð� �ִ�.
-- Tucker ������� �޿��� ���� �ް� �ִ� ����� �̸��� ��(Name���� ��Ī), ����, �޿��� ����Ͻÿ�(15��).
select emp_name, salary from employees
where emp_name like '%Tucker%'
;
select emp_name, job_id, salary from employees
where salary >= (select salary from employees
where emp_name like '%Tucker%')
;

-- [tc �߰� Ǯ��]
select salary from employees
where emp_name like '%Tucker%'
;
select salary from employees
where salary >10000
;
select salary from employees
where salary >(select salary from employees
where emp_name like '%Tucker%')
;
-- ��ü ��� ���� �̻��� ����� ���� ��´� ����� ����
select salary from employees
where salary > (select avg(salary) from employees)
order by salary desc
;


-- [�߰� ����2] ��� ����� �ҼӺμ� ��տ����� ����Ͽ� ������� �̸��� ��(Name���� ��Ī), ����,
-- �޿�, �μ���ȣ, �μ���տ���(Department Avg Salary�� ��Ī)�� ����Ͻÿ�(107��).
-- ���� Ǭ �Ŵ� Ʋ��. �μ���տ����� �����ϰ� ����, �� ���ؾȰ� �����ϱ�
select department_id, round(avg(salary),-1) from employees
group by department_id
;

select emp_name, job_id, salary, department_id, round((select avg(salary) from employees),-1) 
"Department Avg Salary" from employees;

select emp_name, job_id, salary, department_id, round(avg(salary),-1) "Department Avg Salary" 
from employees, (select department_id, round(avg(salary),-1) from employees
group by department_id)
;

-- [tc �߰� Ǯ��]
select avg(salary) from employees;
select emp_name, job_id, salary, department_id from employees;
-- ��
select emp_name, job_id, salary, department_id,
(select round(avg(salary),2) from employees a
where a.department_id = e.department_id) "Department Avg Salar"
from employees e
;

select department_id, round(avg(salary),2) from employees
group by department_id;

-- department_id�� 50���� �μ��� ��� ������ ����
select department_id, round(avg(salary),-1) from employees
where department_id = 50
group by department_id
;

-- department_id = 50�� ������ ��� ������
select round(avg(salary),-1) from employees
where department_id = 50
; -- ==> ���� 50�� e.department_id�θ� ����� ��.

-- join
select salary, a.department_id, b.round_salary
from employees a,
(select department_id, round(avg(salary),2) round_salary from employees
group by department_id) b
where a. department_id = b.department_id
;

select emp_name from employees
where emp_name like '%a%'
;
-- ���� �ڵ忡 ������ ��� �̻��� ���� �߰�
-- - ���� ������ ��� �̻��� ��� ����
select * from employees
where salary>(select avg(salary) from employees);
-- - ���� �ڵ带 ���̺� �־���
select emp_name from 
(select * from employees
where salary>(select avg(salary) from employees))
where emp_name like '%a%'
;

-- equi join 
select salary, a.department_id, department_name
from employees a, departments b
where a.department_id = b.department_id
;

-- [�� ��ũ���� ����]
-- # ���������
-- # �̹���, ����, ����������, ������ 
-- # �̹��� ������� �ؾ� ��.
-- # 2023, 2022, 2021, 2020

-- # �ܼ�â�� ����ϰ� DB�� ����

-- DB
-- ���̺� �� : daum_movie
-- dno : ������
-- title ����Ÿ��(100)
-- img ����Ÿ��(100)
-- audience ����Ÿ��(10)
-- ddate ��¥Ÿ��

create table daum_movie(
dno number primary key,
title varchar2(100),
img varchar2(100),
audience number(10),
ddate date
);

create table coupang(
cno number primary key,
title varchar2(100),
img varchar2(100),
price number(10),
grade number(10),
eval_num number(10)
);

create table flight(
fno number(4),
airline varchar2(100),
departure_time date,
arrival_time date,
flight_time varchar2(20),
price number(10)
);