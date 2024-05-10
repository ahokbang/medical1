-- [ ���̽� ����] 
select * from stu_score;

select * from stu_score
where name like '_a%'
order by no asc;

select * from board01;

select a.*, b.name from board01 a, member b
where a.id = b.id
;
-- id ���� �̸��� ���� ���ھ�.
select bno, a.id, name, btitile, bcontent, bdate, bgroup, bstep, bindent, bhit, bfile
from board01 a, member b
where a.id = b.id
;

select * from stu_score;

select no, name, total, avg,
case
when avg >= 90 then 'A'
when avg >= 80 then 'B'
when avg >= 70 then 'C'
when avg >= 60 then 'D'
else 'F' end as grade 
from stu_score;

select round(avg(salary),2) from employees;

select * from employees;
select employee_id, emp_name, salary, salary+(salary*nvl(commission_pct,0)), to_char(salary*1410,'L999,999,999') from employees;

select * from employees;
select department_id, round(avg(salary),2), round(max(salary),2), round(min(salary),2) from employees
where department_id is not null
group by department_id
order by department_id;

select * from stu_score
order by no;

-- ȫ�̶�� �˻��ϸ� ȫ�� ���õ� �л��� ��� ��µǵ��� �Ͻÿ�.
select * from stu_score
where name like '%ȫ%'
;


-- ��������� �Է� �޾� �Է��� ������� �̻��� �л��� ����Ͻÿ�.
-- �ݺ��ؼ� �����ϰ� -1�� �Է��ϸ� ���α׷��� �����Ͻÿ�.
select * from stu_score;
select avg(avg) from stu_score;
select name from stu_score
where avg >= 74.764
;

desc stu_score;

-- [����]
-- �����ȣ, �����, �μ���ȣ, �μ����� ����Ͻÿ�.
-- equi join
select employee_id, emp_name, employees.department_id, department_name 
from employees a, departments b
where employees.department_id = departments.department_id and emp_name like '_a%'
and salary >= (select avg(salary) from employees)
;

-- �׸���, �̸��� �ι�° �ڸ��� a�� ���� ����� �˻��Ͻÿ�.
select emp_name from employees
where emp_name like '_a%'
;

-- ������ ��� �̻��� ����� �˻��Ͻÿ�.
select emp_name, salary from employees
where salary >= (select avg(salary) from employees)
;

select * from employees;
select * from departments;
select * from jobs; -- ����

-- �����ȣ, �����, �μ���ȣ, �μ���, ���޹�ȣ, ���޸� ���
select employee_id, emp_name, a.department_id, department_name, a.job_id, job_title
from employees a, departments b, jobs c
where a.department_id = b.department_id and a.job_id = c.job_id 
;


select * from jobs;

-- min_salary �߰� 
-- �����ȣe, �����e, ����e, �ּҿ��޺�j, ����e, j, ���޸�j
select employee_id, emp_name, salary, min_salary, a.job_id, job_title
from employees a, jobs b
where a.job_id = b.job_id
;
-- �߰������� �ּҿ����� �λ�� ���
-- �ּҿ����� �� % �̻��� �ް� �ִ���, �λ��: (�ּҿ���/�������)*100
select employee_id, emp_name, salary, min_salary, to_char(round(((salary-min_salary)/min_salary)*100,2)||'%') inc_sal, a.job_id, job_title
from employees a, jobs b
where a.job_id = b.job_id
;

-- job_title�� manager ���ڰ� �� �ִ� 
-- �����ȣe, �����e, ���޹�ȣe, ���޸�j, ����e, �ִ����j�� ����Ͻÿ�.
select job_id, job_title from jobs;

select employee_id, emp_name, a.job_id, job_title, salary, max_salary 
from employees a, jobs b
where a.job_id=b.job_id  -- equi join ���� ��������!!!!
and job_title like '%Manager%' -- �빮�� ����!!!!!!!!!!
;

select a.user_id, user_name, user_phone, user_address1, user_address2, user_addres3
from user a, deliver adress b
where a.user_id=b.user_id
;

-- [non-equi join]
-- non-equi join : ���� ���� ���� ���� ���ؼ� ���.
create table stu_grade(
grade varchar2(1) primary key,
low_score number(3) not null,
high_score number(3) not null
);

insert into stu_grade values(
'A', 90, 100
);
insert into stu_grade values(
'B', 80, 89
);
insert into stu_grade values(
'C', 70, 79
);
insert into stu_grade values(
'D', 60, 69
);
insert into stu_grade values(
'F', 0, 59
);

commit;

select * from stu_grade;

select avg from stu_score;

-- case when then grade �÷� 90�� �̻� A, 80�� �̻� B, ...
select no, name, avg,
case
when avg >= 90 then 'A'
when avg >= 80 then 'B'
when avg >= 70 then 'C'
when avg >= 60 then 'D'
when avg < 60 then 'F' -- else 'F' �� ����
end as grade from stu_score
order by no
;

-- non-equi join ==> case when then grade ���� �ӵ��� ���� �� ����
select no, name, avg, grade
from stu_score, stu_grade
;
-- stu_score�� stu_grade�� �ߺ��Ǵ� column ����
select * from stu_score;
select * from stu_grade;

-- stu_score�� stu_grade�� �ߺ��Ǵ� column ������ 2�� ���̺��� �����ϰڴ� ==> non-equi join
select no, name, avg, grade
from stu_score, stu_grade
where avg between low_score and high_score
order by no
;

-- ���α׷��� �� �� �ʿ� ���� ���̺��� �����͸� ���� �ٲٸ� ��(update ���) ==> ���α׷��� ������ �ʾƵ� ��.
update stu_grade set low_score=92
where grade = 'A'
;
update stu_grade set low_score=82, high_score=91
where grade = 'B'
;
update stu_grade set low_score=72, high_score=81
where grade = 'C'
;
update stu_grade set low_score=62, high_score=71
where grade = 'D'
;
update stu_grade set high_score=61
where grade = 'F'
;

commit;

-- ���� ������� �������� ����� ����

select * from kor_loan_status;

-- ������ ���� �հ踦 ����Ͻÿ�.
select * from kor_loan_status;
select region, gubun, sum(loan_jan_amt)
from kor_loan_status
group by region, gubun
order by region
;
-- gubun ����
select * from kor_loan_status;
select region, sum(loan_jan_amt)
from kor_loan_status
group by region
order by region
;

-- �⵵��, ������, �����հ�ݾ� [ �����ϱ�-group by �κ�, substr �κ� ]
select substr(period,1,4), region, sum(loan_jan_amt)
from kor_loan_status
group by substr(period,1,4), region
order by region, substr(period,1,4)
;

-- �μ��� ���� �հ� ����Ͻÿ�.
select department_id, sum(salary) a from employees
group by department_id
order by a
;

select * from lotte_product;
desc lotte_product;
-- �ð��뺰, ���ɴ뺰 �Ǹŷ� ������ ����Ͻÿ�.
select time_cd, age_cd, sum(purh_amt) a
from lotte_product
group by time_cd,age_cd
order by a desc
;

select * from lotte_product;
select * from shop_product;


select * from shop_product
where pdate>='2024/03/01'
;

-- 2024/03/01 ���� �̸���, �ݾ��հ踦 ����Ͻÿ�.
select name, sum(amount) from shop_product
where pdate>='2024/03/01'
group by name
;

-- customer_rank ���̺� ����
-- rank �� 
-- 100���� �̸� : bronze
-- 200���� �̸� : silver
-- 300���� �̸� : gold
-- 300���� �̻� : platinum

-- name, 3�� ���� 2�� �з�, sum(amount), rank ����Ͻÿ�.
-- non-equi join���� ó��

create table customer_rank(
rank varchar2(10),
low_amount number(7),
high_amount number(8)
);

-- drop table customer_rank;
select * from customer_rank;

insert into customer_rank values(
'bronze',0,999999
);

insert into customer_rank values(
'silver',1000000,1999999
);

insert into customer_rank values(
'gold',2000000,2999999
);

alter table customer_rank
modify (high_amount number(10));

insert into customer_rank values(
'platinum',3000000,10000000
);

select * from customer_rank;

select name, s_amount, rank
from (select name, sum(amount) s_amount
from shop_product
where pdate>='2024/03/01'
group by name), customer_rank
where s_amount between low_amount and high_amount
;

select name, sum(amount) s_amount
from shop_product group by name
order by name
;

--select name, sum(amount) s_mount
--from shop_product, customer_rank
--group by name;

select name, sum(amount),rank
from shop_productm, customer_rank
where pdate>='2024/03/01' and sum(amount) between low_amount and high_amount
group by name, rank
; -- error ORA-00934: �׷� �Լ��� �㰡���� �ʽ��ϴ� ==> rank�� �� ���������(rank�� �����̶�� �ǹ�) group by rank�� �� �� ����.

select * from lotte_product -- ��ȣ�� ����
order by std_ym
;

-- [rownum, row_number()]
-- ������ ���Ӱ� �ο��ؼ� ������ִ� �Լ�

-- rownum : �˻��Ǿ� �ִ� ���¿��� ��ȣ�� �ο�, std_ym, sex_cd, age_cd, time_cd, purh_amt���� ���� �� rownum�� �ο���.
select rownum, std_ym, sex_cd, age_cd, time_cd, purh_amt
from lotte_product
;

select rownum, a.*
from lotte_product a
where rownum <= 10;
;

select * from stu_score 
where no <= 10
order by no
;
select * from stu_score 
where no>= 11 and no <= 20
order by no
;

select rownum, a.*
from lotte_product a
where rownum >= 11 and rownum <= 20
; -- no result ==> ������ �� ���� �Ŀ� rownum�� �ο��Ǳ� ������

-- ��ȣ�� �̸� �־�� ��. [ �ϱ� ] 
select rnum, b.* 
from 
(
select rownum rnum, a.* from lotte_product a
) b
where rnum >= 11 and rnum <= 20
;

-- b.* ��� �� �ۼ�
select rnum, std_ym, sex_cd, age_cd, time_cd, purh_amt
from 
(
select rownum rnum, a.* from lotte_product a
) b
where rnum >= 11 and rnum <= 20
;

-- order by �ϸ� �̹� ��ȣ �ο��Ǿ� �ִ� ���¿��� ���ĵ�
select rownum, a.*
from lotte_product a
order by ste_ym
;

-- order by�� ��ȣ �ο� �ϱ�
select rownum, b.*
from (select * from lotte_product order by std_ym) b
;

select * from stu_score
order by no
;

-- kor ������ ���� ������ 21����� 30����� ����Ͻÿ�.
-- ���� 21, 22, 23, ..., 30�� �ο��ϼ���.
-- mc : Ʋ��
select b.*
from (select rownum rnum, a.* from stu_score a order by kor desc) b
where rnum >= 21 and rnum <= 30
order by rnum
;
-- tc
select rnum, no, name, kor, eng, math, total, avg, rank, c_date
from (
select rownum rnum, b.*
from (select a.* from stu_score a order by kor desc) b
)
where rnum >= 21 and rnum <= 30
-- order by rnum
;

-- [row_number()]
