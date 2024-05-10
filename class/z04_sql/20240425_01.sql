-- ********** [�ϱ�] ********** -- 
-- ����, ����, ���� 
select sysdate-1, sysdate, sysdate+1 from dual;
-- ����, �̴��� ù��, �̴��� ��������
select sysdate, trunc(sysdate,'month'), last_day(sysdate) from dual;
-- �� ��¥�� �ϼ�, �� ��¥�� �޼�
select round(sysdate-hire_date,3), trunc(months_between(sysdate, hire_date),2) from employees;
-- trunc �ϴ��� ����, group by �׷��Լ�
select trunc(kor,-1) kor, count(trunc(kor,-1)) from stu_score
group by trunc(kor,-1)
order by kor
;
-- ****************************** --

-- [����] hire_date ��¥���� ���� ����Ͻÿ�.
-- 2008-01-01 �������� ���� ���
select hire_date, to_char(hire_date,'yyyy-mm-dd') from employees;
select hire_date, to_char(hire_date, 'mm') from employees;

select to_char(hire_date, 'mm') hire_date, count(to_char(hire_date,'mm')) from employees
group by to_char(hire_date, 'mm')
order by hire_date
;

-- [����] hire_date yyyy�⵵, �⵵�� �ο����� ����Ͻÿ�.
select to_char(hire_date, 'yyyy') hire_date, count(to_char(hire_date,'yyyy')) from employees
group by to_char(hire_date, 'yyyy')
order by hire_date
;

-- ����ȯ, number, character, date
-- number : ��Ģ���� ����, ��ǥ, ��ȭ ǥ�� �Ұ�
-- char : ��Ģ����(+, -) �Ұ�, ��ǥ, ��ȭ ǥ�� ����
-- date : ��Ģ����(+, -) ����, ��¥������´� ���� �Ұ� ==> to_char�� ��ȯ �� ��� ���� ���� ����

-- [����] [�ϱ�] ������(stu_seq), ��¥�� �⵵�� �й� �ο��ÿ�. �й� 5�� ���(kor+2024+0001)

select 'ko'||to_char(sysdate,'yyyy')||trim(to_char(stu_seq.nextval,('0000'))) from dual;
--                                                                   9999  : ������ �״�� ��. 0000�� ������ 0���� ǥ��

-- [����] 123,456,789, 156,788 ���ϱ� ��
select to_number(replace('123,456,789',',','')+replace('156,789',',','')) from dual;

-- [����] (123,456,789) + (100,000) = 123556789 ���
select to_number(replace('123,456,789',',',''))+to_number(replace('100,000',',','')) from dual;
-- �Ʒ� ����� replace ��ü
select to_number('123,456,789','999,999,999') from dual;
select to_char(to_number('123,456,789','999,999,999')+to_number('100,000','999,999'),'999,999,999') from dual;


select to_char(salary, '999,999') from employees;


-- ���� Ÿ���� ��¥ Ÿ������ ����
select 20240425 from dual;
select to_char(20240425) from dual;
select to_date(20240425) from dual; -- 24/04/25

-- ���� Ÿ���� ��¥ Ÿ������ ���� +3 �غ���
select 20240425+3 from dual; -- 20240428
select to_char(20240425)+3 from dual; -- 20240428
select to_char(20240425+3) from dual; -- 20240428
select to_char(20240425+3)+3 from dual; -- 20240431
select to_date(20240425+3) from dual; -- 24/04/28

-- ����Ÿ���� ��¥Ÿ������ ����
select emp_name, hire_date from employees
where hire_date > 20070101; -- error hire_date�� �����̱� ������
select emp_name, hire_date from employees
where hire_date > '20070101';  -- ���ڷ� ���� �Ǵ� to_date ����Ͽ� ����ȯ
select emp_name, hire_date from employees
where hire_date > to_date(20070101)
order by hire_date
; 

-- [����] 08���� �Ի��� ����̸��� 2��° ���ڿ� a�� �� �ִ� ����� ����Ͻÿ�. 
select emp_name, hire_date from employees
where to_char(hire_date,'mm')='08' and emp_name like '_a%'
;

-- [����] 01, 05, 08���� �Ի��� ����̸��� 2��° ���ڿ� a�� �� �ִ� ����� ����Ͻÿ�.  ===> or ���
select emp_name, hire_date from employees
where to_char(hire_date,'mm')='01' or to_char(hire_date,'mm')='05' or to_char(hire_date,'mm')='08'
and emp_name like '_a%'
;

-- [����] 01, 05, 08���� �Ի��� ����̸��� 2��° ���ڿ� a�� �� �ִ� ����� ����Ͻÿ�.  ===> in ���
-- 1. �Ի���
select hire_date from employees
where to_char(hire_date,'mm') in('01','05','08')
;
-- 2. �̸�
select emp_name from employees
where emp_name like '_a%'
;
-- 3. �Ի���, �̸� ��ġ��
select emp_name, hire_date from employees
where emp_name like '_a%' and to_char(hire_date,'mm') in ('01','05','08')
;

 -- [����] 20070101 ���� �Ի��� ����̸��� a�� �� �ִ� ����� ����Ͻÿ�. 
 select emp_name, hire_date from employees
 where hire_date>'20070101' and emp_name like '%a%'
 ;
-- + ��
select sysdate+'20240401' from dual;
-- - �ȵ�. ���� �߻�
select sysdate-'20240401' from dual;
-- ����Ÿ���� ��¥Ÿ������ ����
select sysdate-to_date('20240401') from dual; 

select sysdate, '2024-04-01', sysdate-to_date('2024-04-01') from dual;

select * from m_date;

insert into m_date(m_no, m_yesterday) values(
m_no.nextval, '2024-04-01'  -- m_yesterday�� Ÿ���� ��¥���� ���ڷ� �־ �ڵ����� ��¥�� ��ȯ��
);

-- insert into m_date(m_no, m_yesterday, m_today, m_tommorow) values(
-- m_no.nextval, '2024-04-01',sysdate, sysdate-to_date('2024-04-01')
-- );

create table eventDate(
eno number,
e_today date,
e_choice_day date,
e_period number
);

-- �Է� �� ��¥ Ÿ�Կ� ����(����-��¥����)�� �Է��ص� �����.
-- ��¥�� ���ڸ� ����� �Ұ���, �׷��� ���ڸ� ��¥Ÿ������ �����ؾ� ��.
insert into eventDate values(
m_no.nextval, sysdate, '2024-04-01', sysdate-to_date('2024-04-01')
);

select * from eventDate;

-- ����Ÿ���� ����Ÿ������ ����
select to_number('20,000','99,999')-to_number('10,000','99,999') from dual;

-- null�� 0���� ġȯ nvl()
select salary, commission_pct, salary+(salary*nvl(commission_pct,0)) from employees;

-- manager_id null ceo
select manager_id from employees
order by manager_id desc
;

-- ����Ÿ���� ����Ÿ������ ����
select nvl(to_char(manager_id),'ceo') from employees
order by manager_id desc
;

-- [�׷��Լ�]
-- �׷��Լ� : sum, avg, count(), count(*), min, max
-- count(*) : null�� �����Ͽ� count
-- - �� ���̺� ��ü, �Ǵ� �Ϻ�
-- count : ����
select count(emp_name) from employees; -- ����� : 107��
-- null�� ������ count���� ����
select count(manager_id) from employees; -- ����� : 106��
select emp_name, manager_id from employees;

-- sum : ����
select to_char(sum(salary),'999,999') from employees;

-- avg : ���
select avg(salary) avg_sal from employees;

-- min : �ּҰ�, max : �ִ밪
select min(salary), max(salary) from employees;

-- [����] salary�� 6461�޷� ���� ���� ��� ����Ͻÿ� 
select emp_name, salary from employees
where salary > 6461
;

-- [����] salary�� ��պ��� ���� ��� ��� ==> �������� ��� 
select emp_name, salary from employees
where salary > (select avg(salary) avg_sal from employees)
;
-- �ּ� ������ ����� �˰� �;�
select min(salary), emp_name from employees; -- ==> error, ORA-00937: ���� �׷��� �׷� �Լ��� �ƴմϴ�

-- [����] �ּ� ������ �޴� ����� ���, �̸��� ����Ͻÿ�.
select employee_id, emp_name from employees
where salary = 2100
; 
select employee_id, emp_name from employees
where salary = (select min(salary) from employees)
; 

-- [����] �ִ� ������ �޴� ����� ���, �̸��� ����Ͻÿ�.
select employee_id, emp_name from employees
where salary=(select max(salary) from employees)
;

select department_id, salary from employees;
-- �μ���ȣ�� 50���� ����� ��ü ����
select sum(salary) from employees
where department_id = 50
;


select count(*) from stu_score;

-- [quiz] kor ������ 80�� �̻��� �л� ���
select no, name, kor from stu_score
where kor >= 80
order by no
;
-- [quiz] kor���� kor ���� ����̻�, eng���� eng ���� ��� �̻��� �л� ���
select no, name, kor, eng from stu_score
where kor >= (select avg(kor) avg_kor from stu_score) and 
eng >= (select avg(eng) avg_eng from stu_score)
order by no
;

create table s_info(
sno number,
s_count number
);

insert into s_info values(
stu_seq.nextval, 2000
);

select*from s_info;

insert into s_info values(
stu_seq.nextval, (select count(*) from stu_score
where kor >= (select avg(kor) from stu_score) and 
eng >= (select avg(eng) from stu_score) )
);

-- [quiz] �������� �ְ����� �л�, �������� �ְ����� �л�, �������� �ְ����� �л� ���
select name, kor, eng, math from stu_score
where kor = (select max(kor) from stu_score) 
or eng = (select max(eng) from stu_score) 
or math = (select max(math) from stu_score)
;

-- [quiz] employees���� ������ �ִ�, �ּ�, ����� ����� ����Ͻÿ�.
select emp_name, salary from employees
where salary = (select max(salary) from employees)
or salary = (select min(salary) from employees)
or salary = (select avg(salary) from employees)
;

-- �ִ밪
select emp_name, salary from employees
where salary = (select max(salary) from employees)
;

-- select max(salary) from (���̺�)

-- ��պ��� ���� �� : 56��, 56�� �� �ִ� ���� : 6400
select emp_name, salary from employees
where salary <= (select avg(salary) from employees)
order by salary desc
;
-- ��պ��� ���� ���� ���̺�� ���ž�. ==> 6400 ��µ�
select max(salary) from (select emp_name, salary from employees
where salary <= (select avg(salary) from employees)
order by salary desc)
;

-- ��հ����� ���� ��� �߿� �ִ밪�� ����Ͻÿ�.
-- 1. ��հ����� ���� ����� �˻�
-- 2. �˻��� ��� �߿� �ִ밪�� �˻�
select emp_name, salary from employees
where salary = 6400
;
-- 6400�� ã�ƾ� ��. 6400 ã�� ����� 6400�� �־��� 
select emp_name, salary from employees
where salary = (select max(salary) from (select emp_name, salary from employees
where salary <= (select avg(salary) from employees)
order by salary desc))
;

-- [���� �Լ�] : ceil(a), floor(a), round(a), trunc(a) ==> ��״� �ܿ�
-- [�����Լ�] 
-- to_char : yyyy,mm,dd(ddd),hh,mi,ss,am/pm,day(dy) ==> �ܿ�
-- inicap(a): ù���ڸ� �빮��, upper(a): ��� �빮��
-- lpad(������, �ڸ���, ä�� ����)
select emp_name, lpad(emp_name, 15, '#') from employees; -- ==>  ���ʿ� �ڸ� �� ��ŭ ����鿡 # �־���
-- rpad(������, �ڸ���, ä�� ����)
select emp_name, rpad(emp_name, 20, '@') from employees; -- ==> �����ʿ� �ڸ� �� ��ŭ ����鿡 @ �־���
-- ltrim(������, �߶�� ����) : ������ ���ڸ� �߶󳻰� ���
select emp_name, ltrim(emp_name,'Do') from employees; -- ==> 'Do'���� �߶��
-- rtrim(������, �߶�� ����) : ������ ���ڸ� �߶󳻰� ��� 

-- ko20240001
select 'ko20240001', ltrim('ko20240001','ko2024') from dual;

-- substr(������, ©��� �ڸ�(�����ϴ�)��, ������ �ڸ��������� ������ ����)
-- substr(������, ����, ����) ex) substr('abcdegf', 3, 3) - > cde 
select emp_name, substr(emp_name, 3, 4) from employees;


select job_id from employees;
-- [����] job_id�� �ִ� SH�� �����ȣ�� �����ؼ� ����Ͻÿ�.
select substr(job_id, 1, 2)||employee_id from employees;

-- length
select emp_name, length(emp_name) from employees
where length(emp_name) >15;

-- [��¥�Լ�]
-- ��¥�� ��¥�� ���ϸ� ���� �߻� ==> ��¥+��¥ �Ұ���
select sysdate + hire_date from employees; -- ==> error ORA-00975: ��¥�� ��¥�� ������ �� �� �����ϴ�
-- ��¥�� ��¥�� ���� �� ������ �ϼ��� ���´�. ==> ��¥ - ��¥ ����
select sysdate - hire_date from employees;
-- ��¥�� ���ڸ� ���ϰų� ���� ��¥�� ���´�.
select sysdate+1 from dual;
select sysdate-1 from dual;
-- �� 
select sysdate, trunc(sysdate, 'month'), round(sysdate, 'month') from dual;
-- ��
select round(sysdate, 'year') from dual;

-- add_months(������, �߰�/��� �� �� ��) : ���� �� �߰�/���
select sysdate, add_months(sysdate, 3) from dual; -- ==> ���翡�� 3���� ��
select sysdate, add_months(sysdate, -3) from dual; -- ==> ���翡�� 3���� ��

-- ceil(�ø�), floor(����), mod(������), power(����)
select ceil(-4.2), floor(-4.2), mod(8,3), power(2,10) from dual;

-- [����] �л� ���̺��� �̸��� ������ "������ 1979��09��19�� ������" ���·� ���
select * from employees;
select emp_name||to_char(hire_date, ' yyyy"��" mm"��" dd"��" day') from employees;

select emp_name||' '||to_char(hire_date, 'yyyy')||'�� '||to_char(hire_date, 'mm')||'�� '
||to_char(hire_date, 'dd')||'�� '||to_char(hire_date, 'day') from employees;

-- [����] �����, �ڸ��� 9�ڸ� ����� 0���� ǥ��
-- ����*1400 �տ� ��ȭǥ�ÿ� ��ǥ�� �־� ���
select emp_name, to_char(salary*1400,'L000,000,000') from employees;

-- [����] �ڽ��� ���ϰ� �ڽ��� ������ ���� ���� ������ ���� ���Ͻÿ�.
select to_date(20101010), last_day(to_date(20101010)) from dual;
select '2010-10-10', last_day('10/10/10') from dual;
select trunc(to_date('2010-10-10'),'month'), '2010-10-10', last_day('2010-10-10') from dual;

-- [8��. DB ��ü Ÿ��]

-- [9�� alter table]
-- alter table : table ����
-- drop table: table ����
-- DDL : ������ ���Ǿ�(data definition language), create, alter, drop, truncate(���̺� �ʱ�ȭ)
-- DML : ������ ���۾�(data manipulation language), select, insert,update,delete
-- DCL : �����ͺ��̽��� �����ϰų� ��ü�� ������ �ִ� ���� ������ �ϴ� ���(data control language), grant, revoke, commit, rollback

-- [alter table]

select * from member;

desc member;

-- DDL(Data Definition Language) : coloumn �߰�, ����, ����
-- DDL�� commit, rollback ����. �ٷ� �����.
alter table member add gender varchar2(6) default 'female' not null;
desc member;
select * from member;

update member set gender='male';
select * from member;
commit;

-- �÷� ���� 
-- - �÷��̸�����
alter table member rename column name to stu_name;
-- - Ÿ�� ����
alter table member modify(stu_name varchar2(50));
-- ������ �����Ͱ� �����Ϸ��� ũ�⺸�� ���� ���� ����.
update member set stu_name = '';
alter table memebr modify(stu_name varchar2(6));
-- �÷��� Ÿ���� �����Ϸ��� �÷������Ͱ� ������̰ų� null�� �� ���� 
alter table memebr modify(stu_name varchar2(3));
alter table memebr modify(stu_name number(4 ));
select stu_name from member;
alter table member modify(stu_name number(100)); -- error, ORA-01727: ��ġ�� ���� ����(38 �ڸ� �̳�)�� �ʰ��߽��ϴ�


desc member;



-- �÷����� : commit, rollback�� ����
alter table member drop column phone;
desc member;

select * from member;


