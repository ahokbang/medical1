select * from stu_score;

select * from students; -- ������ ���� �޾Ҵµ� �����԰� �޶�

-- drop table students;

-- ù���� ��� �ٲٱ� (students ���̺�)
update students set id = 'aaa',name='ȫ�浿',gender='M' where id='Timothee' and pw='4120';
update students set id = 'bbb',name='������',gender='F' where id='Finley' and pw='5745';
update students set id = 'ccc',name='�̼���',gender='M' where id='Adela';
update students set id = 'ddd',name='������',gender='M' where id='Augustine';
update students set id = 'eee',name='�豸',gender='M' where id='Thaine';
update students set id = 'fff',name='������',gender='M' where id='Torr';
update students set id = 'ggg',name='ȫ����',gender='F' where id='Khalil' and pw='7280';
update students set id = 'hhh',name='ȫ���',gender='F' where id='Tiena' and pw='4310';

select * from students where name ='������';
-- commit;
-- rollback;

-- ��ȣ �ο� (rownum) ==> ���Ӱ� ������ ��ȣ ����
select rownum, a.* from students a
order by grade
;

-- 1. select ����
select a.* from students a;

-- 2. rownum �Լ� ����
select rownum, a.* from students a;

-- 3. order by ���� ����
select rownum, a.* from students a
order by grade
;

-- ������ ������ ���� �����ؾ� ��.
-- 1. select 2. order by ����, 3. rownum
select * from students a
order by grade
; -- �� ������ rownum ����

select rownum, a.*  -- rownum�� ���������� �����.
from (
select * from students -- ù��°�� ����ǰ�
order by grade -- �ι�°�� ����� ������
) a
;

select * from stu_score;
-- ����� 85�� �̻��̸鼭 no�� 500���� ū ���� ����Ͻÿ�.
select * from stu_score
where avg>=85 and no>=500
;
-- ���� �ڵ�� �Ʒ��� ����
select * from 
(select * from stu_score where avg>= 85)
where no >= 500
;

select * from stu_score
where avg>=85;


select name, s_amount, rank from (select name, sum(amount) s_amount from shop_product where pdate>='2024/03/01'
group by name), customer_rank
where s_amount between low_amount and high_amount;

-- ���̺�� shop_product
select name, amount, pdate from shop_product
where pdate>='2024/03/01';

-- �̸��� ���ų��� �հ踦 ���Ͻÿ�.
-- sum(amount) : �������� ������� �÷�
select name, sum(amount) from shop_product
where pdate>= '2024/03/01'
group by name
;

select name, sum(amount), rank from shop_product, customer_rank
where pdate>= '2024/03/01' and
sum(amount) between low_amount and high_amount
group by name
; -- error  ORA-00934: �׷� �Լ��� �㰡���� �ʽ��ϴ� ==> group by�� rank �߰��ؾ� ��.

select name, sum(amount), rank from shop_product, customer_rank
where pdate>= '2024/03/01' and
sum(amount) between low_amount and high_amount
group by name, rank 
; -- error ORA-00934: �׷� �Լ��� �㰡���� �ʽ��ϴ� 

select name, sum(amount) as s_amount from shop_product
where pdate>='2024/03/01'
group by name -- group by ������ error
; -- �긦 ���� shop_product ���̺� �ڸ��� �־���, �Ʒ��� ���� �ڵ尡 ��.

-- equi join : ���� �÷��� 2���� ���̺� �����Ͽ� 2�� �÷��� �̿��� �˻��ϴ� ���
-- non-equi join : ���� �÷� �����鼭 �ΰ��� ���̺��� ����ؼ� �˻��ϴ� ���
select name, s_amount, rank from (
select name, sum(amount) as s_amount from shop_product
where pdate>='2024/03/01'
group by name), customer_rank
where s_amount between low_amount and high_amount
;

-- shop_product, customer_rank ==> non-equi join 
select name, avg, grade from stu_score, stu_grade
where avg between low_score and high_score
;

select * from customer_rank;

-- non-equi join
select name, avg from stu_score;

select name, sum(amount), rank
from shop_product a, customer_rank b
where sum(amount) between low_amount and high_amount
;

select * from stu_grade;

select rownum, a.* from students a
order by id;

select rownum, a.* from 
(
select * from students order by id
) a
where rownum >= 11 and rownum<= 20
; -- ������ ����. rownum�� 1������ �Ű����µ� 11���� �����̶� ã���� ���� �������� �Ѿ�� ���� �����Ͱ� �ٽ� 1������ �ż� �� ã�� �� ����. �̰� ��� �ݺ���. where ���Ǿ����� ����� ��.
-- �׷��� 123�࿡ �̸� ��ȣ�� �ٿ��� �ڵ带 �־���
select * from
(
select rownum rnum, a.* from
(select * from students order by id) a
)
where rnum>=11 and rnum<=20
;

select * from
(select rownum rnum, b.* from
(select * from students a
order by id) b)
where rnum >=11 and rnum <= 20
;

-- row_number()
select * from(
select row_number() over(order by id) rnum, a.*
from students a)
where rnum>=1 and rnum<= 10
;

-- [self join]
select employee_id, emp_name, department_id, manager_id from employees
order by department_id
;

select * from departments;
-- �μ��� ����ϱ�
select employee_id, emp_name, a.department_id, department_name, a.manager_id 
from employees a, departments b
where a.department_id = b.department_id
order by a.department_id
;

select employee_id, emp_name, manager_id, emp_name 
from employees; -- 124���� �ش��ϴ� name�� �ƴϾ� ==> employees ���̺� �ѹ� �� ����

-- cross join 107*107
-- equi join : 2���� ���̺� ���� �÷��� ������ �˻�
select a.employee_id, a.emp_name, a.manager_id, b.emp_name 
from employees a, employees b -- a�� ��ü, b�� manager_id�� �´� emp_name�� ������
where a.manager_id = b.employee_id -- a������ ���̺� ��ü ã��, b������ employee_id�� ã��
order by a.employee_id
;

-- self join,equi-join �Բ� ���
select a.employee_id, a.emp_name, a.department_id, department_name,a.manager_id, b.emp_name
from employees a, employees b, departments c
where a.manager_id = b.employee_id and
a.department_id = c.department_id
order by a.employee_id
;

-- self join
select a.employee_id, a.emp_name, a.manager_id, b.emp_name
from employees a, employees b
where a.manager_id = b.employee_id
;

-- [����] 193~214
-- Guy Himuro�� ������ �μ��� �ٹ��ϴ� ����� ����Ͻÿ�.(�μ��� �� ��)
-- �÷� : �����ȣ, �����, �μ���ȣ, �μ���, ���� �ٹ��ϴ� ����� ==> �����, �μ���ȣ, ���� �ٹ��ϴ� ��� �μ���ȣ, ���� �ٹ��ϴ� �����
-- 1. john �μ��� ���
-- 2. �μ���ȣ�� ������ ���� ����� ���
-- 3. �μ���ȣ, �μ��� ��� ==> �����ϱ� ������.

select * from employees;
select * from departments;

-- 1. Guy Himuro �μ� ���
select emp_name, department_id from employees where emp_name='Guy Himuro'; -- e1

select a.employee_id, a.emp_name, a.department_id
from employees a
where a.department_id ='30'
; -- e2

select e1.emp_name, e1.department_id, e2.emp_name
from employees e1, employees e2
where e1.department_id = e2.department_id and e1.emp_name='Guy Himuro'
;

select * from member;

insert into member values(
member_seq.nextval, 'ddd', '1111', '������', '����', sysdate
);

insert into member values(
member_seq.nextval, 'eee', '1111', '�豸', '����', sysdate
);

insert into member values(
member_seq.nextval, 'fff', '1111', '������', '����', sysdate
);

insert into member values(
member_seq.nextval, 'ggg', '1111', 'ȫ���', '����', sysdate
);

rollback;

commit;
desc member;

update member set name='ȫ�浿' where id='aaa'
;

-- employees�� �ִ� �̸����� �˻��ϴ� �κ� ���� �����Ͻÿ�.
select * from employees
-- where emp_name like '%ȫ%'
;

-- �̸��� �Է��ϸ� �Բ� �ٹ��ϴ� ����� �˻��մϴ�.
select a.department_id,c.department_name, b.emp_name from employees a, employees b, departments c
where a.department_id = b.department_id and a.emp_name='Pat Fay'
and a.department_id=c.department_id
;

select b.employee_id,a.department_id,c.department_name, b.emp_name from employees a, employees b, departments c
where a.department_id = b.department_id and a.emp_name='Pat Fay'
and a.department_id=c.department_id
;

select * from member order by id;
-- hhh, 1111, ȫ����, ����, sysdate

select * from member where id = 'aaa'
;

-- ���̺� ����
create table mem(id varchar2(30) primary key, pw number, name varchar2(30), mdate date)
;

select * from mem;

-- drop table mem;

create table yeogi(
yno number(4) primary key, 
title varchar2(100) not null,
region varchar2(30),
score number,
member number,
image varchar2(100),
price number
);

select * from yeogi;