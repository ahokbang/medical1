-- drop table dept01;
-- drop table emp;
-- drop table emp01;
-- drop table emp02;
-- drop table emp03;
-- drop table eventdate;
-- drop table member;
-- drop table board;
-- drop table employees01;

-- ���Ἲ �������� : �������� �ڷᰡ �Էµ��� �ʵ��� �ϱ� ���� ��Ģ
-- [�ϱ�] not null, unique, primary key, foreign key, check 

-- ���̺� ����
create table member(
memNo number(4) not null,
id varchar2(30) primary key,
pw varchar2(30) not null,
name varchar2(30),
gender varchar2(6) check(gender in ('����','����')),
mdate date default sysdate
);

-- [�ϱ�] ������ ����(�Է�, ���, ����, ����) �Լ� �ܿ��! insert, select, update, delete
-- ������ �Է�, ���, ����, ���� �κ�
insert into member(memNo, id, pw, name, gender, mdate) values(
member_seq.nextval, 'aaa', '1111', 'ȫ�浿', '����', sysdate
);

insert into member(memNo, id, pw, name, gender) values(
member_seq.nextval, 'bbb', '1111', '������', 'Female'
); -- gender���� '����', '����'�� �����Ͽ� �� ���ڸ� �Է� ���� ==> error ORA-02290: üũ ��������(ORA_USER.SYS_C007362)�� ����Ǿ����ϴ�

insert into member(memNo, id, pw, name, gender) values(
member_seq.nextval, 'bbb', '1111', '������', '����'
);

insert into member values(
member_seq.nextval, 'ccc', '1111', '�̼���', '����', sysdate
);

select * from member;

-- table ���� : �Խ��� ���̺� ����
create table board01(
bno number(4) primary key,
id varchar2(30), -- �ܷ�Ű ��� 
btitile varchar2(1000),
bcontent varchar2(4000),
bdate date default sysdate,
bgroup number(4),
bstep number default 0,
bindent number default 0,
bhit number default 1,
bfile varchar2(100) default '',
constraint fk_id foreign key(id) -- �ܷ�Ű(foreign key) ��Ī : fk_id
references member(id) -- member��� ���̺��� primary key�� id�� ����Ǿ� ����.
);

-- �������̺� primary key�� �����Ϸ��� foreign key�� ��ϵǾ� �ִ� �����͸� �켱 ������ ����ؾ� ��.
-- primary key�� �����Ǹ� ��� �����ϴ� ���(on delete cascade), ��� �����ϴ� ���(od update cascade)

select * from member;

insert into board01(bno, id, btitile, bcontent, bdate, bgroup, bstep, bindent, bhit, bfile) values(
board_seq.nextval, 'aaa', '�����Դϴ�.', '�����Դϴ�.', sysdate, board_seq.currval,0,0,1,''
);

insert into board01 values(
board_seq.nextval, 'bbb', '�����Դϴ�.2', '�����Դϴ�.2', sysdate, board_seq.currval,0,0,1,''
);

insert into board01(bno, id, btitile, bcontent, bgroup) values(
board_seq.nextval, 'aaa', '�����Դϴ�.3', '�����Դϴ�.3', board_seq.currval
);

select * from board01;

-- ����
delete board01 where bno=3;

select * from board01;

commit;

delete member where id='aaa'; -- error ORA-02292: ���Ἲ ��������(ORA_USER.FK_ID)�� ����Ǿ����ϴ�- �ڽ� ���ڵ尡 �߰ߵǾ����ϴ�
                              -- board�� id�� �θ�� member�� id�� foreign key�� ��ϵ� ��� �����͸� ���� �����ؾ� ��.
                              
-- [11��]
-- ��������(2) : decode(���ǹ� ���x, ��ġ�ϴ� ��쿡�� ���, switch�� ���), case(���ǹ� ���, if���� ���)
-- decode ���ǹ�: ������ ��ġ(=�񱳿�����)�ϴ� ��쿡 ���ؼ��� ���� 
select emp_name, department_id from employees
order by department_id desc
;

select department_id, department_name from departments;

select emp_name, department_id ,
decode(department_id,
10,'�ѹ���ȹ��',
20,'������',
30,'����/�����',
40,'�λ��'
)
from employees
order by department_id asc
;


select * from stu_score
order by avg desc;

-- [����] 90��(A), 80��(B), 70��(B) ǥ���ϱ�
select no, name, avg, 
decode(avg,
90,'A',
80,'B',
70,'C'
) grade
from stu_score
order by avg desc;

select job_id, salary from employees;
-- [����] ���� ���, decode ���
-- sh_clerk�� ��� salary*15%, ad_asst�� salary*10%, MK_rep�� ��� salary*5% �λ�

select job_id, salary,
decode(job_id,
'SH_CLERK',salary+(salary*0.15),
'AD_ASST',salary+(salary*0.1),
'MK_REP',salary+(salary*0.05)
) new_salary
from employees;
-- ��� clerk �λ�
-- ���1
select job_id, salary,
decode(job_id,
'SH_CLERK',salary+(salary*0.15),
'PU_CLERK',salary+(salary*0.15),
'ST_CLERK',salary+(salary*0.15),
'AD_ASST',salary+(salary*0.1),
'MK_REP',salary+(salary*0.05)
) new_salary
from employees;

-- job_id �߿� clerk�� �� �ִ� job_id�� �˻��Ͻÿ�.
-- like_�ڸ���, % ��� ��
select job_id from employees
where job_id like '%CLERK%'; --'___CLERK'�� ����

-- ��� 2 ==> error
select job_id, salary, decode(job_id,
(like '%CLERK', salary+salary*0.15
'AD_ASST',salary+(salary*0.1),
'MK_REP',salary+(salary*0.05)
) new_salary
from employees;

-- case �Լ� : �پ��� �� �����ڸ� �̿��Ͽ� ���� ���� �� ���� ���� ����
select name, avg from stu_score;

select name, avg,
case 
when avg >= 90 then 'A'
when avg >= 80 then 'B'
when avg >= 70 then 'C'
else 'F'
end as grade
from stu_score;

select department_id, department_name from departments;

select department_id from employees
order by department_id asc;

-- case ���� ����Ͽ� department_id �̸��� ����Ͻÿ�.
select department_id,
case
when department_id = 10 then '�ѹ���ȹ��'
when department_id = 20 then '������'
when department_id = 30 then '����/�����'
when department_id = 40 then '�λ��'
when department_id = 50 then '��ۺ�'
when department_id = 60 then 'IT'
when department_id = 70 then 'ȫ����'
end as dpt_name from employees
order by department_id asc;

-- [����] ������ ����Ͻÿ�. case ���
-- job_id
-- CLERK ����, slary * 15%, ad_asst*10%, rep(����)*5%, man(����) * 2%

select job_id, salary, 
case 
when job_id like '%CLERK%' then salary+salary*0.15
when job_id like 'AD_ASST' then salary+salary*0.10
-- when job_id = 'AD_ASST' then salary+salary*0.10
when job_id like '%REP%' then salary+salary*0.05
when job_id like '%MAN%' then salary+salary*0.02
end as new_salary from employees
;

-- ���� ��� ������ ��� 0.15, ��� �̻��� ����� 0.05�� ���� �λ��ؼ� ����Ͻÿ�.
select avg(salary) from employees; -- 6461.8... ==> 6462

select salary, 
case 
when salary>= 6462 then salary+salary*0.05
when salary < 6462 then salary+salary*0.15
end as new_salary2 from employees
order by new_salary2;

-- employees ���̺��� �˻�: new_salary2 ����
select salary, 
case 
-- when avg(salary)>=salary then salary+salary*0.15 -- ==> error ORA-00937: ���� �׷��� �׷� �Լ��� �ƴմϴ� �Ʒ��� ���� �ۼ� �� ����
when salary>= (select avg(salary) from employees) then salary+salary*0.15
when salary < (select avg(salary) from employees) then salary+salary*0.05
end as new_salary2 from employees
order by new_salary2;

select salary, 
case 
when salary>= 6462 then 'down'
when salary < 6462 then 'up'
end as new_salary2 from employees
order by new_salary2;


select emp_name, salary, new_salary2,
case 
when salary >= (select avg(salary) from employees) then salary+salary*0.15
when salary < (select avg(salary) from employees) then salary+salary*0.05
end as new_salary2 
from employees
order by new_salary2;

-- new_salary2 �÷��� ���� == > employees ��ſ� ���� select ���� �����ž� [Ȯ�� �ʿ�, error]
select emp_name, salary, new_salary2
case 
when salary >= (select avg(salary) from employees) then salary+salary*0.15
when salary < (select avg(salary) from employees) then salary+salary*0.05
end as new_salary2 
from (select emp_name, salary,
case 
when salary >= 6462 then 'down'
when salary < 6462 then 'up'
end as new_salary2 from employees
order by new_salary2)
order by new_salary2;

-- case 2�� ���
select salary, 
case 
when salary>=(select avg(salary) from employees) then salary+salary*0.15
when salary<(select avg(salary) from employees) then salary+salary*0.05
end as salary_down
,
case 
when salary>=(select avg(salary) from employees) then 'up'
when salary<(select avg(salary) from employees) then 'down'
end as salary_up
from employees
order by salary_up;


select * from stu_score;
select total, rank from stu_score
order by total desc;

-- rank() �Լ�
select total, rank, rank() over(order by total desc) as ranks from stu_score;

select no, rank() over(order by total desc) as ranks from stu_score;

select total, rank from stu_score
order by total desc;

update stu_score set rank = 1 
where total=293
;
-- [�ϱ�]
-- 1000�� ������ ���� �Է�
update stu_score a 
set rank = (
select ranks from (
select no, rank() over(order by total desc) as ranks from stu_score
) b
where a.no = b.no 
);

commit ;
update stu_score
set rank = (
1
);

select rank from stu_score
order by no;

select rank() over (order by total desc) as ranks from stu_score;



select department_id,
case
when department_id = 10 then '�ѹ���ȹ��'
when department_id = 20 then '������'
when department_id = 30 then '����/�����'
when department_id = 40 then '�λ��'
when department_id = 50 then '��ۺ�'
when department_id = 60 then 'IT'
when department_id = 70 then 'ȫ����'
end as dpt_name from employees
order by department_id asc;


select emp_name, department_id from employees;
select department_id, department_name from departments;

select emp_name, department_id, department_name from employees, deparments; -- error, ORA-00942: ���̺� �Ǵ� �䰡 �������� �ʽ��ϴ�

select emp_name, employees.department_id, department_name from employees, departments;

select emp_name, employees.department_id, department_name from employees, departments
where employees.department_id = departments.department_id
;


-- �� ���̺� ����, �� ���̺� �����ؼ� ���
select a.department_id, department_name from employees a, departments b
where a.department_id = b.department_id

-- [ group �Լ� ]
-- ���� : sum, avg, count, max, min, steddev(ǥ������), variance(�л�)

-- ������ ���� 
select sum(salary) from employees;
-- �������� ���� stu_score;
select sum(kor) from stu_score;

-- employees ��� ��
select count(*) from employees;

-- �μ� ��ȣ�� 50�� �� ����� ����
select count(*) from employees
where department_id = 50;

-- Ŀ�̼��� �޴� ����� ���� ���Ͻÿ�.
select * from employees;
select count(*) from employees
where commission_pct is not null;

-- [group by��]
-- �׷��ռ��� ���� � �÷� ���� �������� �׷��Լ��� ������ ��� group by �� �ڿ� �ش� �÷��� ��� 
-- select Į����, �׷��Լ�
-- from ���̺��
-- where ����(������_
-- group by Į����; -- ==> Į���� ��Ī ��� �Ұ�. �ݵ�� Į���� ��� 
-- �հ�, ���, �ִ밪�̳� �ּҰ� �� � Į���� �������� �� Į���� �� ���� ������ �� �� group by �� �ڿ� �ش� Į�� ���

select * from employees a; -- a�� ���̺��� ��Ī
select emp.employee_id from employees emp;
select employees.employee_id from employees; -- ���̺��� �ϳ� �ۿ� ���� ���� ���� ����
select employees.employee_id from employees, departments; -- ���̺��� 2�� �̻��� ��� �ݵ�� �ۼ��ؾ� ��.

-- ��ü����� 
select count(*) from employees;

-- department_id=50�� ��� ī��Ʈ
select count(*) from employees
where department_id = 50;


select count(*) from employees
group by department_id;

-- �μ��� �׷� ���� ��� �� ��� 
select department_id, count(department_id) from employees
group by department_id
order by department_id
;

-- stu_score, �÷���: grade
-- avg�� 90�� �̻� A, 80�� �̻� B, 70�� �̻� C, 60�� �̻� D, 60�� �̸� F ���
select name, avg,
case
when avg >= 90 then 'A'
when avg >= 80 then 'B'
when avg >= 70 then 'C'
when avg >= 60 then 'D'
else 'F' end as grade
from stu_score;

-- A���� ������� ���
select count(*) from stu_score
where avg>=90;

select avg,
case
when avg >= 90 then 'A'
when avg >= 80 then 'B'
when avg >= 70 then 'C'
when avg >= 60 then 'D'
else 'F' end as grade
from stu_score
where avg>=90;

select grade, count(grade) from 
(
select name, avg,
case
when avg >= 90 then 'A'
when avg >= 80 then 'B'
when avg >= 70 then 'C'
when avg >= 60 then 'D'
else 'F' end as grade
from stu_score
)
group by grade
order by grade asc
;

-- kor ������ 100���̸� 100, 90~99���̸� 90, 80~89���̸� 80���� ����Ͻÿ�. trunc ���
select kor, trunc(kor, -1) from stu_score;

-- ī��Ʈ
select trunc(kor,-1), count(trunc(kor,-1)) from
(select kor, trunc(kor, -1) from stu_score)
group by trunc(kor,-1)
order by trunc(kor,-1) desc;

-- trunc(kor,-1) ����ؼ� group by ���
select trunc(kor,-1), count(trunc(kor,-1)) from stu_score
group by trunc(kor,-1);

-- trunc(kor,-1) ����ؼ� group by ���: �ι�° ���
-- ����,
select trunc(kor, -1) as k_kor from stu_score;
-- �� ���� ������ �� �ڵ带 ���̺�� ���
select k_kor, count(k_kor) as k_count from 
(select trunc(kor, -1) as k_kor from stu_score)
group by k_kor;

-- �׷��Լ� group by ���
select department_id, count(*) from employees
group by department_id
order by department_id;

-- �Ϲ��Լ��� �׷��Լ��� ���� �� �� ����.
select emp_name, count(emp_name) from employees;

-- �׷��Լ� �������־�� ��.
select emp_name, count(emp_name) from employees
group by emp_name; 

-- �μ��� ��� ���� ���Ͻÿ�
select department_id, round(avg(salary),2) from employees
group by department_id
order by department_id
;

-- CRERK ����, MEP ����, MAN ���Ե� ������ ���� ����� ���Ͻÿ�.
select job_id, count(salary) from employees
where job_id like '%CLERK%' and job_id like '%REP%' and job_id like '%MAN%'
group by job_id
;
-- CRERK�� ���ԵǾ� �ִ� ���� ����� ���Ͻÿ�. 
select job_id,avg(salary) from employees
where job_id like '%CLERK%'
group by job_id;

select job_id, substr(job_id, 4, length(job_id)-3) frin employees;
select substr(job_id, 4, 7), length(substr(job_id,4,7)) from employees;
select job_id, length(job_id) from employees;

select job_id, substr(job_id, 4, length(job_id)-3) from employees;

select substr(job_id, 4, 7),count(substr(job_id,4,7)) from employees
where substr(job_id,4,7) = 'CLERK'
group by substr(job_id, 4,7);

-- ������ ��
select substr(job_id,4,5), count(substr(job_id,4,5)) from employees
where job_id like '%CLERK%'
group by job_id;

-- ���ڿ� �ڸ��� substr(job_id, 4, 5)
-- ���� �� ��
select job_id, avg(salary),
case
when job_id like '%CLERK%' then avg(salary)
when job_id like '%REP%' then avg(salary)
when job_id like '%MAN%' then avg(salary)
end from employees
group by job_id;
-- ���� �� ��
select job_id,avg(salary) from employees
where job_id like '%CLERK%'
group by job_id;


select substr(job_id, 4, 7) as job_id, count(substr(job_id,4,7)) as c_job_id from employees
group by substr(job_id, 4,7)
order by c_job_id
;

-- �μ��� �ִ����, �ּҿ���, ��տ����� ����Ͻÿ�.
select department_id, round(max(salary),2) max_salary, round(min(salary),2) min_salary, round(avg(salary),2) avg_salary from employees
group by department_id
order by department_id;

-- null �� �����ϰ� ��� 
select department_id, round(max(salary),2) max_salary, round(min(salary),2) min_salary, round(avg(salary),2) avg_salary 
from employees
where department_id is not null
group by department_id
order by department_id;

-- ������������ �˾Ƶ� ��.
select department_id, count(salary), round(max(salary),2) max_salary, round(min(salary),2) min_salary, round(avg(salary),2) avg_salary 
from employees
where department_id is not null
group by department_id
order by department_id;

-- �μ��� ����ϰ� �;� ==> table ����
select a.department_id,department_name, count(salary), round(max(salary),2) max_salary, round(min(salary),2) min_salary, round(avg(salary),2) avg_salary 
from employees a, departments b
where a.department_id = b.department_id
group by a.department_id, department_name
order by a.department_id;

-- �μ��� ��� ��, Ŀ�̼��� �޴� ��� ���� ����Ͻÿ�.
-- �μ��� ��� ���� ����Ͻÿ�.
select department_id, count(department_id) from employees
group by department_id
order by department_id;

-- Ŀ�̼��� �޴� ��� ���� ����Ͻÿ�.
select commission_pct, count(commission_pct) from employees
where commission_pct is not null
group by commission_pct
order by commission_pct;

-- �μ��� ��� ��, Ŀ�̼��� �޴� ��� ���� ����Ͻÿ�.
select department_id, count(department_id),count(commission_pct) from employees
group by department_id
order by department_id;


-- [having��]
-- group by�� ���� ������, where�� �Ϲ� �÷��� ���� ������
select department_id, round(avg(salary),2) from employees
group by department_id
order by avg(salary);

select department_id, round(avg(salary),2) from employees
group by department_id
having avg(salary) >= 6000
order by avg(salary)
;

-- emp_name�� �ι�° ���ڰ� a�� �����ϴ� ������ ����
select emp_name from employees
where emp_name not like '_a%';

select department_id, round(avg(salary),2) from employees
where emp_name not like '_a%'
group by department_id
having avg(salary) >= 6000
order by avg(salary)
;

-- ��տ��޺��� ���� �׷� ���
select department_id, round(avg(salary),2) from employees
where emp_name not like '_a%'
group by department_id
having avg(salary) >= (select avg(salary) from employees)
order by avg(salary);

-- �μ��� �ִ������ 8000�̻��� �͸� ���
select department_id, max(salary) from employees
group by department_id
having max(salary)>=8000
order by department_id
;

-- [����] ==> ���̺��� ���� �߿�!!
-- RDBMS : ������ Database

select emp_name, department_id,salary from employees; -- department_name ����

select department_id, department_name from departments; -- emp_name�� salary ����

select count(*) from employees;  -- data: 107��
select count(*) from departments;  -- data: 27��

-- ���̺� 2�� ������ ���� �����̶�� ��. 
-- ������ : 107*27(=2889)��
select * from employees, departments;

-- cross join(3): 
-- - inner join(2) : 
--   - equi join : ������ Į���� �������� ����
--   - non-equi join: ���� Į���� ���� �ٸ� ������ ����Ͽ� ����
-- - outer join : ���� ���ǿ� �������� �ʴ� �൵ ��Ÿ��
-- self join: �� ���̺� ������ ����

-- equi join :  ���� ���� ����ϴ� ���� ���, �������� �����ϴ� �÷��� ���� ��ġ�Ǵ� ���� ����. 
--              �÷��� �̸��� �����Ƿ� �տ� ���̺�� ���

-- [ equi join ]
-- �� ���̺��� ���� �÷��� ������ ���ؼ� �ش�Ǵ� �����͸� ���
-- �÷��� ���� : �ǹ̾���. 107*27 =2889���� �����Ͱ� ����
select employee_id, emp_name, employees.department_id, department_name, salary 
from employees, departments;
select department_id, department_name from departments;
-- equi join : 106�� ������ ����(null�� �Ѱ� �˻����� ����).
select employee_id, emp_name, employees.department_id, department_name, salary 
from employees, departments
where employees.department_id = departments.department_id
;

select * from board01; -- id�� �־�
select * from member; -- �̸��� �־�
-- id ��� �̸��� �ְ� �;�
select member.id, name, btitile, bcontent from board01, member;
select id, btitile, bcontent from board01;

--
update member set name='ȫ����'
where id = 'aaa';

select * from member;

-- equi.join
select bno, name, btitile, bcontent, bdate, bgroup, bstep, bindent, bhit, bfile from board01, member
where member.id = board01.id;











