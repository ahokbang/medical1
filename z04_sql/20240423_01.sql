select * from students;

-- ��������
select * from students
order by name asc;

-- drop table students;

-- column �߰�
alter table students add rank number(3);
select * from students;
update students set rank=0;
select * from students;
commit;

select total, rank() over(order by total desc) rank
from students;

update students set total=0; 

select * from students;
select total, rank from students
order by total desc;

update students set total=(kor+eng+math);

update students s1 set rank = (select ranks from 
(select no, rank() over(order by total desc) as ranks from students) s2
where s1.no=s2.no);

-- 1. update ����
update students a set rank = (rank);

-- 2. no, rank() ����
(select no, rank() over(order by total desc) ranks from students) b);
-- ���� ������ �ϳ��� table �̸����� �ʹ� ��ϱ� b�� ��Ī

-- 3. update ������ rank() ������ no �÷����� ��, rank �÷��� �˻�
update studenst a set rank=(
select ranks from (students) b
where a.no = b.no);

-- 4. students ���̺��� ranks�� �� �ִ� ���̺��� �־���. 
update students a set rank = (
select ranks from (select no, rank() over(order by total desc) ranks from students) b
where a.no = b.no);

select no, total, rank from students
order by total desc;

update students a set rank=(select rank() over(order by total desc) rank
from students b where a.no = b.no);

-- update students a set rank = (select ranks from (select no, rank() over(order by
total desc) ranks from students) s2 where s1.no =s2.no);

-- ���� ����
select no, total, rank from students
order by total desc;

-- no ��������
select no, total, rank from students
order by no;

select no, kor, eng, math, total, rank from students 
order by kor desc, eng asc;

select manager_id from employees
order by manager_id desc;

select hire_date from employees
order by hire_date;

-- �ִ밪
select max(hire_date) from employees
order by hire_date;

-- �ּҰ�
select min(hire_date) from employees
order by hire_date;

-- �ִ밪 - �ּҰ�
select max(hire_date)-min(hire_date) from employees
order by hire_date;
select max(kor)-min(kor) from students;

select max(kor), max(eng), max(math) from students;

-- ���� 1.
-- hire_date�� ��������, �÷� �����ȣ, �����, job_id-����, �Ի���, ���� �÷� ���
select * from employees;
select employee_id, emp_name, job_id, hire_date, salary from employees
order by hire_date;

-- ���� 2.
-- �޿��� ���� �޴� ��� ������ ����ϵ�, ������ ������ ��������� ���������Ͻÿ�.
select * from employees
order by salary, emp_name;


-- �����Լ�
-- abs: ���밪
-- dual�� ���� ���̺� 
select -10, abs(-10) from dual;
-- floor�� �Ҽ��� ���� �� ���� 
select 34.789, floor(34.789) floor, round(34.789) round from dual;

-- round(���, �ڸ���) ex) round(34.718,2) �Ҽ��� 2�ڸ����� ǥ��
select 34.178, round(34.178) round, round(34.178, 2) round2 from dual; 

select avg from students;
select round(avg,2) avg from students;

-- -1���� �ݿø��� 1�� �ڸ����� �ݿø��� �ǹ�. -2�� �����ڸ����� �ݿø�, ...
select 34.567, round(34.5678, -1) from dual;

-- trunc: ������ �ڸ��� ���� ����
select trunc(34.5678, 2) from dual;
select trunc(34.5678, -1) from dual;
select trunc(34.5678) from dual;

-- ceil: �Ҽ��� �ڸ����� �ø�
select ceil(34.123) from dual;


-- �������� �ϴ��� �����ؼ� ���
select trunc(kor,-1) from students
order by kor
;

-- kor, eng, math �ϴ��� �����ؼ� kor, eng, math �հ� ���
select trunc(kor,-1) + trunc(eng,-1) + trunc(math,-1) as trunc_total from students;
-- k+e+m �����ϸ� �ȳ��� trunc(kor,-1) + trunc(eng,-1) + trunc(math,-1) as trunc_total�� ���־�� ��.
select trunc(kor,-1) k, trunc(eng,-1) e, trunc(math,-1) m, 
(trunc(kor,-1) + trunc(eng,-1) + trunc(math,-1)) total from students;

-- mod : ������
select round(10/7,2) from dual;
select mod(10,7) from dual;
-- ������� �׳�
select 10/7 from dual;

-- ����. �����ȣ�� ¦���� ���� ����Ͻÿ�.
-- ���̽� employee_id%2 = 0
select employee_id from employees
where mod(employee_id,2)=0;

-- �� 
select floor(10/7) from dual;
-- ��������, �������� 0�̸� ¦��, 1�̸� Ȧ��
select mod(10,7) from dual;

-- ����. �й��� 3�� ����ΰ͸� ����Ͻÿ�. students ���̺�
select * from students
where mod(no,3)=0;


-- [6�� ������]
-- �⺻ Ű: ���� �����ϱ� ���� �⺻ Ű.  null�� ����. �׻� ������ Ű�� �ߺ����� �ʾ�. ==> �ڵ���ȣ�߻���. ������ primary key
create sequence seq_no 
increment by 1 -- 1�� ����
start with 1 -- 1���� ����
minvalue 1 -- �ּҰ�
maxvalue 9999 -- �ִ밪
nocycle -- ��ȯ���� ����
nocache; -- ĳ�� ������� ����

-- nextval : ������ ��ȣ 1�� ����, ���ڰ� 1�� ī��Ʈ ��
select seq_no.nextval from dual;

-- currval : ������ ��ȣ Ȯ�� ==> ���� �� Ȯ��
select seq_no.currval from dual;

-- drop table member;
-- ���� �Ŀ��� �ּ� ó��

-- drop table mem3;

create table member (
mno number(4),
id varchar2(30),
pw varchar2(20),
name varchar2(30),
phone varchar2(15)
);

create sequence seq_mno
increment by 1
start with 1
minvalue 1
maxvalue 9999
nocycle
nocache
;

select seq_mno.nextval from dual;

insert into member values (
seq_mno.nextval, 'eee','1111','�豸','010-5555-5555'
);
select * from member;

-- ���� ��¥���� �⵵ ����
select sydate from dual;
select to_char(sysdate,'yyyy') from dual;
-- ||: ���� ��ġ��
select 's0000'||to_char(seq_mno.currval) from dual;
-- trim() : ��������
select 's0000'||trim(to_char(seq_mno.currval)) from dual;


-- ����.
-- �ѱ����б� �й� ko+���г⵵+00001(ko202400001, ko202400002, .....) ���
-- ������ seq_ko, 1-9999
create sequence seq_ko
increment by 1
start with 1
minvalue 1
maxvalue 9999
nocycle
nocache;

-- '00000': �ڸ���
select 'ko'||to_char(sysdate,'yyyy')||trim(to_char(seq_ko.nextval,'00000')) as stuno from dual;

-- �Խ���
create table board (
bno number(5) primary key,
btitle varchar2(1000),
bcontent varchar2(3000),
id varchar2(30),
bdate date,
bhit number(10)
);
-- cycle: �ߺ� ����. �ߺ� �߻� �� error

-- ����
-- ������ ����: seq_deptno, ����1001, ���� 10, �ּҰ� 1, �ִ밪 99999, cycle
-- 5�� ����
create sequence seq_deptno
increment by 10
start with 1001
minvalue 1
maxvalue 99999
cycle 
nocache;

select seq_deptno.nextval from dual;

create table emp01(
empno number(4) primary key,
ename varchar2(30),
hire_date date
);
-- ������ ����
alter sequence emp_seq
increment by 1001
;

create sequence emp_seq
increment by 1
start with 1
minvalue 1
maxvalue 9999
nocycle
nocache;

insert into emp01 values(
emp_seq.nextval, '�̼���',sysdate
);

select * from emp01;

commit;

-- ���� 1. �Ի��� �������� ����, ���, �̸�, ����, �Ի��� ���
select * from employees;

select employee_id, emp_name, job_id, hire_date from employees
order by hire_date;

--���� 2. ������� �Ի��� �ϼ��� �Բ� ���(�ݿø�)
select employee_id, emp_name, job_id, hire_date, ceil(sysdate-hire_date)||'��' from employees
order by hire_date;

select emp_name from employees;

-- Quiz
-- ���ް� ����� ���ļ� ���
select job_id||employee_id from employees;
-- �տ� ���ڸ��� ����ϰ� �;�
-- substr(���, ������ġ, ����) : ���ڿ� �ڸ��� �Լ�
select substr(job_id,0,2) from employees;

select emp_name, substr(emp_name,1,3) from employees;

select substr('abcde',2,3) from dual;

-- Quiz
-- job_id���� �տ� �� ���ڿ� ���5�ڸ� (00101)�� ����� �Բ� ����Ͻÿ�.
select substr(job_id,1,2)||'00'||employee_id from employees;
-- ������ �ڵ�
select substr(job_id,0,2),employee_id,to_char(employee_id,'00000'), 
substr(job_id,0,2)||trim(to_char(employee_id, '00000')) from employees;

-- ��¥�Լ�
select sysdate from dual;

select to_char(sysdate,'yyyy-mm-dd hh:mi:ss') from dual;

-- months_between(��¥1, ��¥2) : �� ��¥ ������ ���� �� Ȯ��
select months_between(sysdate,hire_date), sysdate-hire_date from employees;

-- add_months(���س�¥, ������) : �������� �߰�
select sysdate, add_months(sysdate, 2) from dual;

-- next_day(���س�¥,����): �Է��� ��¥�� �������� ������ ������ �˷��� ==> ���س�¥ �������� ���ƿ��� ������ ��¥�� ���
select next_day(sysdate,'������') from dual;

-- last_day(��¥) : �Է��� ��¥�� �������� ������ ���� �˷���.
select last_day(sysdate) from dual;
select last_day('2024-02-01') from dual;