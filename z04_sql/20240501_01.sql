select * from stu_score;

select * from students; -- 선생님 파일 받았는데 선생님과 달라

-- drop table students;

-- 첫번재 사람 바꾸기 (students 테이블)
update students set id = 'aaa',name='홍길동',gender='M' where id='Timothee' and pw='4120';
update students set id = 'bbb',name='유관순',gender='F' where id='Finley' and pw='5745';
update students set id = 'ccc',name='이순신',gender='M' where id='Adela';
update students set id = 'ddd',name='강감찬',gender='M' where id='Augustine';
update students set id = 'eee',name='김구',gender='M' where id='Thaine';
update students set id = 'fff',name='김유신',gender='M' where id='Torr';
update students set id = 'ggg',name='홍길자',gender='F' where id='Khalil' and pw='7280';
update students set id = 'hhh',name='홍길순',gender='F' where id='Tiena' and pw='4310';

select * from students where name ='김유신';
-- commit;
-- rollback;

-- 번호 부여 (rownum) ==> 새롭게 순차적 번호 생성
select rownum, a.* from students a
order by grade
;

-- 1. select 구문
select a.* from students a;

-- 2. rownum 함수 실행
select rownum, a.* from students a;

-- 3. order by 구문 실행
select rownum, a.* from students a
order by grade
;

-- 순서를 다음과 같이 변경해야 함.
-- 1. select 2. order by 구문, 3. rownum
select * from students a
order by grade
; -- 이 다음에 rownum 실행

select rownum, a.*  -- rownum이 마지막으로 수행됨.
from (
select * from students -- 첫번째로 수행되고
order by grade -- 두번째로 수행된 다음데
) a
;

select * from stu_score;
-- 평균이 85점 이상이면서 no가 500보다 큰 수를 출력하시오.
select * from stu_score
where avg>=85 and no>=500
;
-- 위의 코드는 아래와 같아
select * from 
(select * from stu_score where avg>= 85)
where no >= 500
;

select * from stu_score
where avg>=85;


select name, s_amount, rank from (select name, sum(amount) s_amount from shop_product where pdate>='2024/03/01'
group by name), customer_rank
where s_amount between low_amount and high_amount;

-- 테이블명 shop_product
select name, amount, pdate from shop_product
where pdate>='2024/03/01';

-- 이름별 구매내역 합계를 구하시오.
-- sum(amount) : 가상으로 만들어진 컬럼
select name, sum(amount) from shop_product
where pdate>= '2024/03/01'
group by name
;

select name, sum(amount), rank from shop_product, customer_rank
where pdate>= '2024/03/01' and
sum(amount) between low_amount and high_amount
group by name
; -- error  ORA-00934: 그룹 함수는 허가되지 않습니다 ==> group by에 rank 추가해야 함.

select name, sum(amount), rank from shop_product, customer_rank
where pdate>= '2024/03/01' and
sum(amount) between low_amount and high_amount
group by name, rank 
; -- error ORA-00934: 그룹 함수는 허가되지 않습니다 

select name, sum(amount) as s_amount from shop_product
where pdate>='2024/03/01'
group by name -- group by 없으면 error
; -- 얘를 위의 shop_product 테이블 자리에 넣어줌, 아래와 같은 코드가 됨.

-- equi join : 같은 컬럼이 2개의 테이블에 존재하여 2개 컬럼을 이용해 검색하는 방법
-- non-equi join : 같은 컬럼 없으면서 두개의 테이블을 사용해서 검색하는 방법
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
; -- 데이터 없음. rownum은 1번부터 매겨지는데 11번이 조건이라서 찾으면 없어 다음으로 넘어가면 다음 데이터가 다시 1번으로 돼서 또 찾을 수 없음. 이게 계속 반복돼. where 조건없으면 출력은 돼.
-- 그래서 123행에 미리 번호를 붙여논 코드를 넣어줘
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
-- 부서명 출력하기
select employee_id, emp_name, a.department_id, department_name, a.manager_id 
from employees a, departments b
where a.department_id = b.department_id
order by a.department_id
;

select employee_id, emp_name, manager_id, emp_name 
from employees; -- 124번에 해당하는 name이 아니야 ==> employees 테이블 한번 더 써줘

-- cross join 107*107
-- equi join : 2개의 테이블에 같은 컬럼을 가지고 검색
select a.employee_id, a.emp_name, a.manager_id, b.emp_name 
from employees a, employees b -- a는 전체, b는 manager_id에 맞는 emp_name을 가져와
where a.manager_id = b.employee_id -- a에서는 테이블 전체 찾고, b에서는 employee_id를 찾아
order by a.employee_id
;

-- self join,equi-join 함께 사용
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

-- [퀴즈] 193~214
-- Guy Himuro과 동일한 부서에 근무하는 사람을 출력하시오.(부서를 모를 때)
-- 컬럼 : 사원번호, 사원명, 부서번호, 부서명, 같이 근무하는 사원명 ==> 사원명, 부서번호, 같이 근무하는 사원 부서번호, 같이 근무하는 사원명
-- 1. john 부서를 출력
-- 2. 부서번호를 가지고 같은 사람을 출력
-- 3. 부서번호, 부서명 출력 ==> 어려우니까 하지마.

select * from employees;
select * from departments;

-- 1. Guy Himuro 부서 출력
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
member_seq.nextval, 'ddd', '1111', '강감찬', '남자', sysdate
);

insert into member values(
member_seq.nextval, 'eee', '1111', '김구', '남자', sysdate
);

insert into member values(
member_seq.nextval, 'fff', '1111', '김유신', '남자', sysdate
);

insert into member values(
member_seq.nextval, 'ggg', '1111', '홍길순', '여자', sysdate
);

rollback;

commit;
desc member;

update member set name='홍길동' where id='aaa'
;

-- employees에 있는 이름으로 검색하는 부분 로직 구현하시오.
select * from employees
-- where emp_name like '%홍%'
;

-- 이름을 입력하면 함께 근무하는 사원을 검색합니다.
select a.department_id,c.department_name, b.emp_name from employees a, employees b, departments c
where a.department_id = b.department_id and a.emp_name='Pat Fay'
and a.department_id=c.department_id
;

select b.employee_id,a.department_id,c.department_name, b.emp_name from employees a, employees b, departments c
where a.department_id = b.department_id and a.emp_name='Pat Fay'
and a.department_id=c.department_id
;

select * from member order by id;
-- hhh, 1111, 홍길자, 여자, sysdate

select * from member where id = 'aaa'
;

-- 테이블 생성
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