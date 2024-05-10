-- [ 파이썬 연결] 
select * from stu_score;

select * from stu_score
where name like '_a%'
order by no asc;

select * from board01;

select a.*, b.name from board01 a, member b
where a.id = b.id
;
-- id 다음 이름이 왔음 좋겠어.
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

-- 홍이라고 검색하면 홍에 관련된 학생이 모두 출력되도록 하시오.
select * from stu_score
where name like '%홍%'
;


-- 평균점수를 입력 받아 입력한 평균점수 이상의 학생을 출력하시오.
-- 반복해서 진행하고 -1을 입력하면 프로그램을 종료하시오.
select * from stu_score;
select avg(avg) from stu_score;
select name from stu_score
where avg >= 74.764
;

desc stu_score;

-- [조인]
-- 사원번호, 사원명, 부서번호, 부서명을 출력하시오.
-- equi join
select employee_id, emp_name, employees.department_id, department_name 
from employees a, departments b
where employees.department_id = departments.department_id and emp_name like '_a%'
and salary >= (select avg(salary) from employees)
;

-- 그리고, 이름의 두번째 자리에 a가 들어가는 사원을 검색하시오.
select emp_name from employees
where emp_name like '_a%'
;

-- 월급이 평균 이상인 사람만 검색하시오.
select emp_name, salary from employees
where salary >= (select avg(salary) from employees)
;

select * from employees;
select * from departments;
select * from jobs; -- 직급

-- 사원번호, 사원명, 부서번호, 부서명, 직급번호, 직급명 출력
select employee_id, emp_name, a.department_id, department_name, a.job_id, job_title
from employees a, departments b, jobs c
where a.department_id = b.department_id and a.job_id = c.job_id 
;


select * from jobs;

-- min_salary 추가 
-- 사원번호e, 사원명e, 월급e, 최소월급분j, 직급e, j, 직급명j
select employee_id, emp_name, salary, min_salary, a.job_id, job_title
from employees a, jobs b
where a.job_id = b.job_id
;
-- 추가적으로 최소월급의 인상분 출력
-- 최소월급의 몇 % 이상을 받고 있는지, 인상분: (최소월급/현재월급)*100
select employee_id, emp_name, salary, min_salary, to_char(round(((salary-min_salary)/min_salary)*100,2)||'%') inc_sal, a.job_id, job_title
from employees a, jobs b
where a.job_id = b.job_id
;

-- job_title에 manager 글자가 들어가 있는 
-- 사원번호e, 사원명e, 직급번호e, 직급명j, 월급e, 최대월급j을 출력하시오.
select job_id, job_title from jobs;

select employee_id, emp_name, a.job_id, job_title, salary, max_salary 
from employees a, jobs b
where a.job_id=b.job_id  -- equi join 조건 잊지말기!!!!
and job_title like '%Manager%' -- 대문자 주의!!!!!!!!!!
;

select a.user_id, user_name, user_phone, user_address1, user_address2, user_addres3
from user a, deliver adress b
where a.user_id=b.user_id
;

-- [non-equi join]
-- non-equi join : 같은 것이 없는 것을 비교해서 출력.
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

-- case when then grade 컬럼 90점 이상 A, 80점 이상 B, ...
select no, name, avg,
case
when avg >= 90 then 'A'
when avg >= 80 then 'B'
when avg >= 70 then 'C'
when avg >= 60 then 'D'
when avg < 60 then 'F' -- else 'F' 도 가능
end as grade from stu_score
order by no
;

-- non-equi join ==> case when then grade 보다 속도가 조금 더 빨라
select no, name, avg, grade
from stu_score, stu_grade
;
-- stu_score와 stu_grade는 중복되는 column 없음
select * from stu_score;
select * from stu_grade;

-- stu_score와 stu_grade는 중복되는 column 없지만 2개 테이블을 조인하겠다 ==> non-equi join
select no, name, avg, grade
from stu_score, stu_grade
where avg between low_score and high_score
order by no
;

-- 프로그램을 손 댈 필요 없이 테이블의 데이터만 값만 바꾸면 돼(update 사용) ==> 프로그램을 멈추지 않아도 됨.
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

-- 월별 매출액을 기준으로 고객등급 산출

select * from kor_loan_status;

-- 지역별 대출 합계를 출력하시오.
select * from kor_loan_status;
select region, gubun, sum(loan_jan_amt)
from kor_loan_status
group by region, gubun
order by region
;
-- gubun 빼기
select * from kor_loan_status;
select region, sum(loan_jan_amt)
from kor_loan_status
group by region
order by region
;

-- 년도별, 지역별, 대출합계금액 [ 복습하기-group by 부분, substr 부분 ]
select substr(period,1,4), region, sum(loan_jan_amt)
from kor_loan_status
group by substr(period,1,4), region
order by region, substr(period,1,4)
;

-- 부서별 월급 합계 출력하시오.
select department_id, sum(salary) a from employees
group by department_id
order by a
;

select * from lotte_product;
desc lotte_product;
-- 시간대별, 연령대별 판매량 총합을 출력하시오.
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

-- 2024/03/01 이후 이름별, 금액합계를 출력하시오.
select name, sum(amount) from shop_product
where pdate>='2024/03/01'
group by name
;

-- customer_rank 테이블 생성
-- rank 열 
-- 100만원 미만 : bronze
-- 200만원 미만 : silver
-- 300만원 미만 : gold
-- 300만원 이상 : platinum

-- name, 3월 이후 2달 분량, sum(amount), rank 출력하시오.
-- non-equi join으로 처리

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
; -- error ORA-00934: 그룹 함수는 허가되지 않습니다 ==> rank가 안 만들어져서(rank가 가상이라는 의미) group by rank를 할 수 없어.

select * from lotte_product -- 번호가 없어
order by std_ym
;

-- [rownum, row_number()]
-- 순번을 새롭게 부여해서 출력해주는 함수

-- rownum : 검색되어 있는 형태에서 번호를 부여, std_ym, sex_cd, age_cd, time_cd, purh_amt먼저 실행 후 rownum이 부여돼.
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
; -- no result ==> 데이터 다 나온 후에 rownum이 부여되기 때문에

-- 번호를 미리 넣어야 해. [ 암기 ] 
select rnum, b.* 
from 
(
select rownum rnum, a.* from lotte_product a
) b
where rnum >= 11 and rnum <= 20
;

-- b.* 대신 열 작성
select rnum, std_ym, sex_cd, age_cd, time_cd, purh_amt
from 
(
select rownum rnum, a.* from lotte_product a
) b
where rnum >= 11 and rnum <= 20
;

-- order by 하면 이미 번호 부여되어 있는 상태에서 정렬되
select rownum, a.*
from lotte_product a
order by ste_ym
;

-- order by로 번호 부여 하기
select rownum, b.*
from (select * from lotte_product order by std_ym) b
;

select * from stu_score
order by no
;

-- kor 점수가 높은 순으로 21등부터 30등까지 출력하시오.
-- 순번 21, 22, 23, ..., 30번 부여하세요.
-- mc : 틀림
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
