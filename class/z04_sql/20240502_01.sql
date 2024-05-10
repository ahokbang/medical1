-- 2�� ���̺� : department_id

select * from employees;
select * from departments;

select employee_id, emp_name, a.department_id, department_name 
from employees a, departments b
where a.department_id = b.department_id
;

select * from stu_score
order by no;

select count(*) from stu_score;

desc stu_score;

select count(*) from students;

select * from students;

alter table students add no number(38);

insert into students(no) select no from stu_score
;

-- insert into students(no) set no=

-- rownum ���� ������� ��ȣ�� no�� �ְ� �;�.
update students b set no=
(select rnum from (select rownum rnum, id from students) a)
where a.id = b.id
;

update students b set no = a.rnum
from (select rownum rnum, id from students) a
where b.id = a.id
;


select rnum from 
(select rownum rnum, a.* from students a 
)
;
-- select * from students;



select rownum rnum, a.* from students a 
;

-- ȫ�浿 �л��� �л������� �ִ� ��� ����� ��ȭ��ȣ, �̸���, ��, �г��� ���� �;�.
select no, name, kor, eng, math, total, avg, rank, c_date from stu_score
where name = 'ȫ�浿';

select id, name, phone, email, major, grade from students
where name = 'ȫ�浿'
;

select no, id, a.name, phone, major, grade, kor, eng, math, total, avg, rank, c_date
from stu_score a, students b
where a.name ='ȫ�浿' and a.name=b.name
;

-- drop table students;
-- drop table stu_score;

-- equi join
-- - 2���� ���̺� join �� 1���� ������ �÷� �־�� ��.
-- - �� ��, ������ �÷��� �ߺ��� ����� ��. 
-- - �� ���̺� �� �ϳ��� ���̺����� primary key�� �� ���Ǿ�� ��.


select a.id, a.name, phone, total, avg 
from students a, stu_score b
where a.id = b.id
order by name
;


-- self join
-- - ������ ���̺� 2���� ������ ���� join
select employee_id, department_id, job_id, manager_id from employees
order by department_id
;

select a.employee_id, a.department_id, a.job_id, a.manager_id, b.emp_name 
from employees a, employees b
where a.manager_id = b.employee_id -- where ���� �ݴ�� ¥�� �ʰ� ����!! ���� a.employee_id = b.manager_id�� �߾�̤�
order by department_id;
;

desc stu_score;

desc students;

-- drop table students;

select * from students;

select * from stu_score;

-- rank �ϴ� ��� : rank() �Լ� ���
select no, id, rank() over(order by total desc) ranks, rank, total from stu_score a
;

-- ranks�� ����
select ranks from (select no, id, rank() over(order by total desc) ranks, rank, total from stu_score) b
;

-- [����] stu_score�� rank �ֱ�
update stu_score a
set rank = 
(select ranks from (select no, id, rank() over(order by total desc) as ranks, rank, total from stu_score) b
where a.no = b.no)
;

select * from stu_score;


select * from students;

select * from member;

alter table member add no number;

select * from member;

select rownum, a.* from member a;

--id�� no�� �ֱ�
update member a
set no = (select rnum from (select rownum rnum, id from member) b 
where a.id = b.id)  -- rnum�� ã������ b
;

select * from member;

-- rank�� id�� ����������
select rownum rnum, id from member;
-- rnum�� ����������
select rnum from (select rownum rnum, id from member);

select rnum from (select rownum rnum, id from member) b
where id = b.id;

-- rank �־��ָ�
select no, id, rank() over(order by total desc) as ranks, rank, total from stu_score;

update stu_score set rank=0;

commit;

select total, rank from stu_score
order by total desc
;


-- rank ���̷���: ��ŷ�ؼ� ��ȣ �ο�
select total, rank() over(order by total desc) ranks from stu_score;
-- ���� ��ȣ �ο�
select row_number() over(order by total desc) rnum from stu_score; 


-- [����] stu_score�� rank ������ update �Ͻÿ�. 
select * from stu_score;

-- [��Ʈ] update ���� : update �ϴ� ���
update stu_score set rank = 1; -- => ��� rank ���� 1 �Էµ�
-- update ������ where ���� �־��ָ� �� ���ǿ��� rank=1 �Է�
update stu_score ser rank=1
where no=1;

update stu_score a set rank = 
(select ranks from (select no, rank() over(order by total desc) ranks from stu_score) b
where a.no = b.no)
;

select * from stu_score
order by rank
;

-- row_number() over()
select * from stu_score;

select rownum rnum, a.* from
(select * from stu_score order by total desc) a
;

select row_number() over(order by total desc) rnum, a.* from stu_score a
;

select row_number() over(order by total desc) rnum, a.* from stu_score a
where rnum>=1 and rnum<= 10
;

select rownum rnum, a.* from
(select * from stu_score order by total desc) a
where rownum>=11 and rownum<= 20 -- ����
; -- rownum>=1 and rownum<= 10�� ��� ���� �ȳ�

-- rownum �ϱ��ϱ�
select * from
(
select rownum rnum, a.* from
(select * from stu_score order by total desc) a
)
where rnum>=11 and rnum<=20
; 
-- row_number �ϱ��ϱ�
select * from (
select row_number() over(order by total desc) rnum, a.* from stu_score a
)
where rnum>= 11 and rnum<= 20
;

-- [ outer join ]
select employee_id, emp_name, manager_id from employees
order by employee_id
;

select * from employees; -- ��� ���� �˻����� ���� 107�� �˻���

-- self join���� manager_id, �̸� ����Ͻÿ�.
select a.employee_id, a.emp_name, a.manager_id, b.emp_name
from employees a, employees b
where a.manager_id = b.employee_id
;  -- ��� 106�� �˻���. null�� �˻����� ����. ==> outer join ������� ����
-- �ܺ� ������ ���� ���ǿ� �������� ���Ͽ����� �ش� �ο츣 ��Ÿ���� ���� �� ���
-- ���� �������� �ʾƵ� ��µǵ��� �ϴ� ���� outer join
-- null ���� �ִ� �� �ݴ��� �׸� (+)��ȣ�� ������ ��.
select a.employee_id, a.emp_name, a.manager_id, b.emp_name
from employees a, employees b
where a.manager_id = b.employee_id(+)
; -- �ܺ������� null ���� �ִ� manager_id �ݴ����� employee_id�� (+) �߰���.

select manager_id, emp_name from employees
where emp_name = 'Diana Lorentz'
;

-- equi join, outer join      
-- employees ���̺��� �μ���ȣ 10~110
select department_id from employees
order by department_id;

select emp_name, a.department_id, department_name
from employees a, departments b
where a.department_id = b.department_id
order by department_id
;

select emp_name, a.department_id, department_name
from employees a, departments b
where a.department_id(+) = b.department_id
order by department_id
;

select emp_name, b.department_id, department_name
from employees a, departments b
where a.department_id(+) = b.department_id
order by department_id
;

-- departments ���̺��� �μ���ȣ 10~270
select department_id from departments;

-- [ ANSI Join - inner join]
select * from employees cross join departments;
-- ���� �ڵ�� �Ʒ��� ����
select * from employees, departments;

-- equi join
select a.department_id, department_name 
from employees a, departments b
where a.department_id = b.department_id
;

-- ansi inner join
select a.department_id, department_name from employees a inner join departments b
on a. department_id = b.department_id
;
-- ansi inner join - using
select employee_id, emp_name, department_id, department_name
from employees join departments 
using (department_id)
;
-- equi join
select a.*, b.*
from employees a, departments b
where a.department_id = b.department_id
;

select * from employees a, departments b
where a.department_id = b.department_id
;

-- [ ANSI Join - natural join ]
-- natural join
select * from employees a natural join departments b 
;

-- ansi outer join : left outer join, right outer join, full outer join
select * from employees a
left outer join employees b
on a.manager_id = b.employee_id
;
-- null���� �ִ� ��ġ(left) �ۼ� ==>  null �� ���
select a.manager_id, a.emp_name from employees a
left outer join employees b
on a.manager_id = b.employee_id
;
select a.manager_id, a.emp_name, b.emp_name from employees a
left outer join employees b
on a.manager_id = b.employee_id
;
-- �⺻ sql left outer join, right outer join, full outer join �Ұ�
select a.emp_name, a.manager_id, b.emp_name 
from employees a, employees b
where a.manager_id = b.employee_id(+)
;
-- (+) ���ʿ� �ϸ� error������, outer join�� full�� ���� ǥ�� ����
select a.manager_id, a.emp_name, b.emp_name from employees a
full outer join employees b
on a.manager_id = b.employee_id
;


-- [���̽� DB]
-- id �˻�
select * from stu_score where id like '%a%'
order by no
;
-- row_number() over() �ֱ�
-- 11~20���� ����Ͻÿ�.
select * from
(select row_number() over(order by no) rnum, a.* from stu_score a 
where id like '%a%')
where rnum >= 11 and rnum <= 20
;

select count(*) from stu_score where id like '%a%';

select count(*) from
(select row_number() over(order by no) rnum, a.* from stu_score a 
where id like '%am%')
;

create table melon(
mno number primary key,
rank number,
v_rank number,
img varchar2(100),
title varchar2(100),
singer varchar2(100),
likeNum number
);

create table yanolja (
yno number primary key,
img varchar2(100),
title varchar2(100),
grade number,
grade_num number,
price number
);

alter table yanolja modify img varchar2(300);
alter table melon modify img varchar2(300);