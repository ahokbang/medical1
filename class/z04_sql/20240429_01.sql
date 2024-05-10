-- drop table dept01;
-- drop table emp;
-- drop table emp01;
-- drop table emp02;
-- drop table emp03;
-- drop table eventdate;
-- drop table member;
-- drop table board;
-- drop table employees01;

-- 무결성 제약조건 : 부적합한 자료가 입력되지 않도록 하기 위한 규칙
-- [암기] not null, unique, primary key, foreign key, check 

-- 테이블 생성
create table member(
memNo number(4) not null,
id varchar2(30) primary key,
pw varchar2(30) not null,
name varchar2(30),
gender varchar2(6) check(gender in ('남자','여자')),
mdate date default sysdate
);

-- [암기] 데이터 가공(입력, 출력, 수정, 삭제) 함수 외우기! insert, select, update, delete
-- 데이터 입력, 출력, 수정, 삭제 부분
insert into member(memNo, id, pw, name, gender, mdate) values(
member_seq.nextval, 'aaa', '1111', '홍길동', '남자', sysdate
);

insert into member(memNo, id, pw, name, gender) values(
member_seq.nextval, 'bbb', '1111', '유관순', 'Female'
); -- gender에서 '남자', '여자'로 한정하여 두 글자만 입력 가능 ==> error ORA-02290: 체크 제약조건(ORA_USER.SYS_C007362)이 위배되었습니다

insert into member(memNo, id, pw, name, gender) values(
member_seq.nextval, 'bbb', '1111', '유관순', '여자'
);

insert into member values(
member_seq.nextval, 'ccc', '1111', '이순신', '남자', sysdate
);

select * from member;

-- table 생성 : 게시판 테이블 구조
create table board01(
bno number(4) primary key,
id varchar2(30), -- 외래키 등록 
btitile varchar2(1000),
bcontent varchar2(4000),
bdate date default sysdate,
bgroup number(4),
bstep number default 0,
bindent number default 0,
bhit number default 1,
bfile varchar2(100) default '',
constraint fk_id foreign key(id) -- 외래키(foreign key) 별칭 : fk_id
references member(id) -- member라는 테이블의 primary key로 id가 선언되어 있음.
);

-- 원본테이블에 primary key를 삭제하려면 foreign key에 등록되어 있는 데이터를 우선 삭제를 모두해야 함.
-- primary key가 삭제되면 모두 삭제하는 방법(on delete cascade), 모두 존재하는 방법(od update cascade)

select * from member;

insert into board01(bno, id, btitile, bcontent, bdate, bgroup, bstep, bindent, bhit, bfile) values(
board_seq.nextval, 'aaa', '제목입니다.', '내용입니다.', sysdate, board_seq.currval,0,0,1,''
);

insert into board01 values(
board_seq.nextval, 'bbb', '제목입니다.2', '내용입니다.2', sysdate, board_seq.currval,0,0,1,''
);

insert into board01(bno, id, btitile, bcontent, bgroup) values(
board_seq.nextval, 'aaa', '제목입니다.3', '내용입니다.3', board_seq.currval
);

select * from board01;

-- 삭제
delete board01 where bno=3;

select * from board01;

commit;

delete member where id='aaa'; -- error ORA-02292: 무결성 제약조건(ORA_USER.FK_ID)이 위배되었습니다- 자식 레코드가 발견되었습니다
                              -- board의 id의 부모는 member의 id로 foreign key로 등록된 모든 데이터를 먼저 삭제해야 함.
                              
-- [11강]
-- 논리연산자(2) : decode(조건문 사용x, 일치하는 경우에만 사용, switch와 비슷), case(조건문 사용, if문과 비슷)
-- decode 조건문: 조건이 일치(=비교연산자)하는 경우에 대해서만 적용 
select emp_name, department_id from employees
order by department_id desc
;

select department_id, department_name from departments;

select emp_name, department_id ,
decode(department_id,
10,'총무기획부',
20,'마케팅',
30,'구매/생산부',
40,'인사부'
)
from employees
order by department_id asc
;


select * from stu_score
order by avg desc;

-- [퀴즈] 90점(A), 80점(B), 70점(B) 표시하기
select no, name, avg, 
decode(avg,
90,'A',
80,'B',
70,'C'
) grade
from stu_score
order by avg desc;

select job_id, salary from employees;
-- [퀴즈] 월급 출력, decode 사용
-- sh_clerk인 경우 salary*15%, ad_asst는 salary*10%, MK_rep의 경우 salary*5% 인상

select job_id, salary,
decode(job_id,
'SH_CLERK',salary+(salary*0.15),
'AD_ASST',salary+(salary*0.1),
'MK_REP',salary+(salary*0.05)
) new_salary
from employees;
-- 모든 clerk 인상
-- 방법1
select job_id, salary,
decode(job_id,
'SH_CLERK',salary+(salary*0.15),
'PU_CLERK',salary+(salary*0.15),
'ST_CLERK',salary+(salary*0.15),
'AD_ASST',salary+(salary*0.1),
'MK_REP',salary+(salary*0.05)
) new_salary
from employees;

-- job_id 중에 clerk이 들어가 있는 job_id를 검색하시오.
-- like_자리수, % 모든 것
select job_id from employees
where job_id like '%CLERK%'; --'___CLERK'도 가능

-- 방법 2 ==> error
select job_id, salary, decode(job_id,
(like '%CLERK', salary+salary*0.15
'AD_ASST',salary+(salary*0.1),
'MK_REP',salary+(salary*0.05)
) new_salary
from employees;

-- case 함수 : 다양한 비교 여산자를 이요하여 조건 제시 및 범위 지정 가능
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

-- case 구문 사용하여 department_id 이름을 출력하시오.
select department_id,
case
when department_id = 10 then '총무기획부'
when department_id = 20 then '마케팅'
when department_id = 30 then '구매/생산부'
when department_id = 40 then '인사부'
when department_id = 50 then '배송부'
when department_id = 60 then 'IT'
when department_id = 70 then '홍보부'
end as dpt_name from employees
order by department_id asc;

-- [퀴즈] 월급을 출력하시오. case 사용
-- job_id
-- CLERK 포함, slary * 15%, ad_asst*10%, rep(포함)*5%, man(포함) * 2%

select job_id, salary, 
case 
when job_id like '%CLERK%' then salary+salary*0.15
when job_id like 'AD_ASST' then salary+salary*0.10
-- when job_id = 'AD_ASST' then salary+salary*0.10
when job_id like '%REP%' then salary+salary*0.05
when job_id like '%MAN%' then salary+salary*0.02
end as new_salary from employees
;

-- 월급 평균 이하인 사람 0.15, 평균 이상인 사람은 0.05로 월급 인상해서 출력하시오.
select avg(salary) from employees; -- 6461.8... ==> 6462

select salary, 
case 
when salary>= 6462 then salary+salary*0.05
when salary < 6462 then salary+salary*0.15
end as new_salary2 from employees
order by new_salary2;

-- employees 테이블에서 검색: new_salary2 없음
select salary, 
case 
-- when avg(salary)>=salary then salary+salary*0.15 -- ==> error ORA-00937: 단일 그룹의 그룹 함수가 아닙니다 아래와 같이 작성 시 가능
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

-- new_salary2 컬럼이 있음 == > employees 대신에 위의 select 문을 넣을거야 [확인 필요, error]
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

-- case 2개 사용
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

-- rank() 함수
select total, rank, rank() over(order by total desc) as ranks from stu_score;

select no, rank() over(order by total desc) as ranks from stu_score;

select total, rank from stu_score
order by total desc;

update stu_score set rank = 1 
where total=293
;
-- [암기]
-- 1000명 순위를 각각 입력
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
when department_id = 10 then '총무기획부'
when department_id = 20 then '마케팅'
when department_id = 30 then '구매/생산부'
when department_id = 40 then '인사부'
when department_id = 50 then '배송부'
when department_id = 60 then 'IT'
when department_id = 70 then '홍보부'
end as dpt_name from employees
order by department_id asc;


select emp_name, department_id from employees;
select department_id, department_name from departments;

select emp_name, department_id, department_name from employees, deparments; -- error, ORA-00942: 테이블 또는 뷰가 존재하지 않습니다

select emp_name, employees.department_id, department_name from employees, departments;

select emp_name, employees.department_id, department_name from employees, departments
where employees.department_id = departments.department_id
;


-- 두 테이블 조인, 두 테이블 조인해서 출력
select a.department_id, department_name from employees a, departments b
where a.department_id = b.department_id

-- [ group 함수 ]
-- 종류 : sum, avg, count, max, min, steddev(표준편차), variance(분산)

-- 월급의 총합 
select sum(salary) from employees;
-- 국어점수 총합 stu_score;
select sum(kor) from stu_score;

-- employees 사람 수
select count(*) from employees;

-- 부서 번호가 50번 인 사람의 총합
select count(*) from employees
where department_id = 50;

-- 커미션을 받는 사원의 수를 구하시오.
select * from employees;
select count(*) from employees
where commission_pct is not null;

-- [group by절]
-- 그룹합수를 쓰되 어떤 컬럼 값을 기준으로 그룹함수를 적용할 경우 group by 절 뒤에 해당 컬럼을 기술 
-- select 칼럼명, 그룹함수
-- from 테이블명
-- where 조건(연산자_
-- group by 칼럼명; -- ==> 칼럼의 별칭 사용 불가. 반드시 칼럼명 기술 
-- 합계, 평균, 최대값이나 최소값 등 어떤 칼럼을 기준으로 그 칼럼의 값 별로 보고자 할 때 group by 절 뒤에 해당 칼럼 기술

select * from employees a; -- a가 테이블의 별칭
select emp.employee_id from employees emp;
select employees.employee_id from employees; -- 테이블이 하나 밖에 없을 때는 생략 가능
select employees.employee_id from employees, departments; -- 테이블이 2개 이상일 경우 반드시 작성해야 함.

-- 전체사원수 
select count(*) from employees;

-- department_id=50인 사람 카운트
select count(*) from employees
where department_id = 50;


select count(*) from employees
group by department_id;

-- 부서별 그룹 지어 사원 수 출력 
select department_id, count(department_id) from employees
group by department_id
order by department_id
;

-- stu_score, 컬럼명: grade
-- avg가 90점 이상 A, 80점 이상 B, 70점 이상 C, 60점 이상 D, 60점 미만 F 출력
select name, avg,
case
when avg >= 90 then 'A'
when avg >= 80 then 'B'
when avg >= 70 then 'C'
when avg >= 60 then 'D'
else 'F' end as grade
from stu_score;

-- A학점 몇명인지 출력
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

-- kor 점수를 100점이면 100, 90~99점이면 90, 80~89점이면 80으로 출력하시오. trunc 사용
select kor, trunc(kor, -1) from stu_score;

-- 카운트
select trunc(kor,-1), count(trunc(kor,-1)) from
(select kor, trunc(kor, -1) from stu_score)
group by trunc(kor,-1)
order by trunc(kor,-1) desc;

-- trunc(kor,-1) 사용해서 group by 사용
select trunc(kor,-1), count(trunc(kor,-1)) from stu_score
group by trunc(kor,-1);

-- trunc(kor,-1) 사용해서 group by 사용: 두번째 방법
-- 먼저,
select trunc(kor, -1) as k_kor from stu_score;
-- 그 다음 위에서 한 코드를 테이블로 사용
select k_kor, count(k_kor) as k_count from 
(select trunc(kor, -1) as k_kor from stu_score)
group by k_kor;

-- 그룹함수 group by 사용
select department_id, count(*) from employees
group by department_id
order by department_id;

-- 일반함수와 그룹함수는 같이 쓸 수 없음.
select emp_name, count(emp_name) from employees;

-- 그룹함수 지정해주어야 해.
select emp_name, count(emp_name) from employees
group by emp_name; 

-- 부서별 평균 월급 구하시오
select department_id, round(avg(salary),2) from employees
group by department_id
order by department_id
;

-- CRERK 포함, MEP 포함, MAN 포함된 직급의 월급 평균을 구하시오.
select job_id, count(salary) from employees
where job_id like '%CLERK%' and job_id like '%REP%' and job_id like '%MAN%'
group by job_id
;
-- CRERK이 포함되어 있는 월급 평균을 구하시오. 
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

-- 내가한 거
select substr(job_id,4,5), count(substr(job_id,4,5)) from employees
where job_id like '%CLERK%'
group by job_id;

-- 문자열 자르기 substr(job_id, 4, 5)
-- 내가 한 거
select job_id, avg(salary),
case
when job_id like '%CLERK%' then avg(salary)
when job_id like '%REP%' then avg(salary)
when job_id like '%MAN%' then avg(salary)
end from employees
group by job_id;
-- 내가 한 거
select job_id,avg(salary) from employees
where job_id like '%CLERK%'
group by job_id;


select substr(job_id, 4, 7) as job_id, count(substr(job_id,4,7)) as c_job_id from employees
group by substr(job_id, 4,7)
order by c_job_id
;

-- 부서별 최대월급, 최소월급, 평균월급을 출력하시오.
select department_id, round(max(salary),2) max_salary, round(min(salary),2) min_salary, round(avg(salary),2) avg_salary from employees
group by department_id
order by department_id;

-- null 값 제외하고 출력 
select department_id, round(max(salary),2) max_salary, round(min(salary),2) min_salary, round(avg(salary),2) avg_salary 
from employees
where department_id is not null
group by department_id
order by department_id;

-- 이정도까지만 알아도 돼.
select department_id, count(salary), round(max(salary),2) max_salary, round(min(salary),2) min_salary, round(avg(salary),2) avg_salary 
from employees
where department_id is not null
group by department_id
order by department_id;

-- 부서명 출력하고 싶어 ==> table 조인
select a.department_id,department_name, count(salary), round(max(salary),2) max_salary, round(min(salary),2) min_salary, round(avg(salary),2) avg_salary 
from employees a, departments b
where a.department_id = b.department_id
group by a.department_id, department_name
order by a.department_id;

-- 부서별 사원 수, 커미션을 받는 사원 수를 출력하시오.
-- 부서별 사원 수를 출력하시오.
select department_id, count(department_id) from employees
group by department_id
order by department_id;

-- 커미션을 받는 사원 수를 출력하시오.
select commission_pct, count(commission_pct) from employees
where commission_pct is not null
group by commission_pct
order by commission_pct;

-- 부서별 사원 수, 커미션을 받는 사원 수를 출력하시오.
select department_id, count(department_id),count(commission_pct) from employees
group by department_id
order by department_id;


-- [having절]
-- group by에 대한 조건절, where은 일반 컬럼에 대한 조건절
select department_id, round(avg(salary),2) from employees
group by department_id
order by avg(salary);

select department_id, round(avg(salary),2) from employees
group by department_id
having avg(salary) >= 6000
order by avg(salary)
;

-- emp_name의 두번째 글자가 a로 시작하는 데이터 제외
select emp_name from employees
where emp_name not like '_a%';

select department_id, round(avg(salary),2) from employees
where emp_name not like '_a%'
group by department_id
having avg(salary) >= 6000
order by avg(salary)
;

-- 평균월급보다 작은 그룹 출력
select department_id, round(avg(salary),2) from employees
where emp_name not like '_a%'
group by department_id
having avg(salary) >= (select avg(salary) from employees)
order by avg(salary);

-- 부서별 최대월급이 8000이상인 것만 출력
select department_id, max(salary) from employees
group by department_id
having max(salary)>=8000
order by department_id
;

-- [조인] ==> 테이블에서 가장 중요!!
-- RDBMS : 관계형 Database

select emp_name, department_id,salary from employees; -- department_name 없어

select department_id, department_name from departments; -- emp_name과 salary 없어

select count(*) from employees;  -- data: 107개
select count(*) from departments;  -- data: 27개

-- 테이블 2개 연결한 것을 조인이라고 함. 
-- 데이터 : 107*27(=2889)개
select * from employees, departments;

-- cross join(3): 
-- - inner join(2) : 
--   - equi join : 동일한 칼럼을 기준으로 조인
--   - non-equi join: 동일 칼럼이 없이 다른 조건을 사용하여 조인
-- - outer join : 조인 조건에 만족하지 않는 행도 나타냄
-- self join: 한 테이블 내에서 조인

-- equi join :  가장 많이 사용하는 조인 방법, 공통으로 존재하는 컬럼의 값이 일치되는 행을 연결. 
--              컬럼의 이름이 같으므로 앞에 테이블명 명시

-- [ equi join ]
-- 두 테이블간의 같은 컬럼으 가지고 비교해서 해당되는 데이터를 출력
-- 플러스 조인 : 의미없음. 107*27 =2889개의 데이터가 나와
select employee_id, emp_name, employees.department_id, department_name, salary 
from employees, departments;
select department_id, department_name from departments;
-- equi join : 106개 데이터 나와(null값 한개 검색되지 않음).
select employee_id, emp_name, employees.department_id, department_name, salary 
from employees, departments
where employees.department_id = departments.department_id
;

select * from board01; -- id만 있어
select * from member; -- 이름이 있어
-- id 대신 이름을 넣고 싶어
select member.id, name, btitile, bcontent from board01, member;
select id, btitile, bcontent from board01;

--
update member set name='홍길자'
where id = 'aaa';

select * from member;

-- equi.join
select bno, name, btitile, bcontent, bdate, bgroup, bstep, bindent, bhit, bfile from board01, member
where member.id = board01.id;











