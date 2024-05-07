-- 2개 테이블 : department_id

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

-- rownum 만들어서 만들어진 번호를 no에 넣고 싶어.
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

-- 홍길동 학생의 학생성적에 있는 모든 내용과 전화번호, 이메일, 과, 학년을 보고 싶어.
select no, name, kor, eng, math, total, avg, rank, c_date from stu_score
where name = '홍길동';

select id, name, phone, email, major, grade from students
where name = '홍길동'
;

select no, id, a.name, phone, major, grade, kor, eng, math, total, avg, rank, c_date
from stu_score a, students b
where a.name ='홍길동' and a.name=b.name
;

-- drop table students;
-- drop table stu_score;

-- equi join
-- - 2개의 테이블 join 시 1개의 동일한 컬럼 있어야 함.
-- - 이 때, 동일한 컬럼은 중복이 없어야 함. 
-- - 두 테이블 중 하나의 테이블에서는 primary key가 꼭 사용되어야 함.


select a.id, a.name, phone, total, avg 
from students a, stu_score b
where a.id = b.id
order by name
;


-- self join
-- - 동일한 테이블 2개를 가지고 서로 join
select employee_id, department_id, job_id, manager_id from employees
order by department_id
;

select a.employee_id, a.department_id, a.job_id, a.manager_id, b.emp_name 
from employees a, employees b
where a.manager_id = b.employee_id -- where 조건 반대로 짜지 않게 주의!! 나는 a.employee_id = b.manager_id로 했어ㅜㅠ
order by department_id;
;

desc stu_score;

desc students;

-- drop table students;

select * from students;

select * from stu_score;

-- rank 하는 방법 : rank() 함수 사용
select no, id, rank() over(order by total desc) ranks, rank, total from stu_score a
;

-- ranks만 추출
select ranks from (select no, id, rank() over(order by total desc) ranks, rank, total from stu_score) b
;

-- [최종] stu_score에 rank 넣기
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

--id를 no에 넣기
update member a
set no = (select rnum from (select rownum rnum, id from member) b 
where a.id = b.id)  -- rnum을 찾기위한 b
;

select * from member;

-- rank와 id를 가져오려면
select rownum rnum, id from member;
-- rnum만 가져오려면
select rnum from (select rownum rnum, id from member);

select rnum from (select rownum rnum, id from member) b
where id = b.id;

-- rank 넣어주면
select no, id, rank() over(order by total desc) as ranks, rank, total from stu_score;

update stu_score set rank=0;

commit;

select total, rank from stu_score
order by total desc
;


-- rank 붙이려면: 랭킹해서 번호 부여
select total, rank() over(order by total desc) ranks from stu_score;
-- 순차 번호 부여
select row_number() over(order by total desc) rnum from stu_score; 


-- [퀴즈] stu_score에 rank 순위를 update 하시오. 
select * from stu_score;

-- [힌트] update 구문 : update 하는 방법
update stu_score set rank = 1; -- => 모든 rank 열에 1 입력됨
-- update 구문에 where 조건 넣어주면 그 조건에만 rank=1 입력
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
where rownum>=11 and rownum<= 20 -- 에러
; -- rownum>=1 and rownum<= 10의 경우 에러 안남

-- rownum 암기하기
select * from
(
select rownum rnum, a.* from
(select * from stu_score order by total desc) a
)
where rnum>=11 and rnum<=20
; 
-- row_number 암기하기
select * from (
select row_number() over(order by total desc) rnum, a.* from stu_score a
)
where rnum>= 11 and rnum<= 20
;

-- [ outer join ]
select employee_id, emp_name, manager_id from employees
order by employee_id
;

select * from employees; -- 모든 것을 검색했을 때는 107개 검색됨

-- self join으로 manager_id, 이름 출력하시오.
select a.employee_id, a.emp_name, a.manager_id, b.emp_name
from employees a, employees b
where a.manager_id = b.employee_id
;  -- 얘는 106개 검색됨. null은 검색되지 않음. ==> outer join 사용으로 보완
-- 외부 조인은 조인 조건에 만족하지 못하였더라도 해당 로우르 나타내고 싶을 때 사용
-- 값이 충족되지 않아도 출력되도록 하는 것이 outer join
-- null 값이 있는 그 반대편 항목에 (+)기호를 넣으면 됨.
select a.employee_id, a.emp_name, a.manager_id, b.emp_name
from employees a, employees b
where a.manager_id = b.employee_id(+)
; -- 외부조인은 null 값이 있는 manager_id 반대편인 employee_id에 (+) 추가함.

select manager_id, emp_name from employees
where emp_name = 'Diana Lorentz'
;

-- equi join, outer join      
-- employees 테이블에는 부서번호 10~110
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

-- departments 테이블에는 부서번호 10~270
select department_id from departments;

-- [ ANSI Join - inner join]
select * from employees cross join departments;
-- 위의 코드는 아래와 같음
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
-- null값이 있는 위치(left) 작성 ==>  null 값 출력
select a.manager_id, a.emp_name from employees a
left outer join employees b
on a.manager_id = b.employee_id
;
select a.manager_id, a.emp_name, b.emp_name from employees a
left outer join employees b
on a.manager_id = b.employee_id
;
-- 기본 sql left outer join, right outer join, full outer join 불가
select a.emp_name, a.manager_id, b.emp_name 
from employees a, employees b
where a.manager_id = b.employee_id(+)
;
-- (+) 양쪽에 하면 error나지만, outer join은 full로 양쪽 표시 가능
select a.manager_id, a.emp_name, b.emp_name from employees a
full outer join employees b
on a.manager_id = b.employee_id
;


-- [파이썬 DB]
-- id 검색
select * from stu_score where id like '%a%'
order by no
;
-- row_number() over() 넣기
-- 11~20까지 출력하시오.
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