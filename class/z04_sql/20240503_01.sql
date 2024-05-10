-- [ 오라클 퀴즈 ]
-- [ 1 ] 사원정보(employees) 테이블에서
-- 사원번호, 이름, 급여, 부서, 입사일, 상사의 사원번호를 출력하시오.
-- 이 때 이름은 이름과 직급을 연결하여 Name이라는 별칭으로 출력하시오.

select * from employees;
select * from departments;
select employee_id, emp_name, salary, department_name, hire_date, a.manager_id 
from employees a, departments b
where a.department_id = b.department_id;

select employee_id, emp_name||'/'||job_id "Name", salary, department_name, hire_date, a.manager_id 
from employees a, departments b
where a.department_id = b.department_id;
-- [tc 추가 풀이]
select employee_id, emp_name||'/'||job_id "Name", salary, department_id, hire_date, manager_id 
from employees;


-- [ 2 ] 사원정보(employees) 테이블에서
-- 사원의 이름과 성은 Name, 업무는 Job, 급여는 Salary, 
-- 연봉에 $100 보너스를 추가하여 계산한 값은 Increase Ann_Salary,
-- 급여에 $100 보너스를 추가하여 계산한 연봉은 Increase Salary라는 별칭을 붙여 출력하시오.

select emp_name "Name", job_id "Job", salary "Salary", 
(salary*12)+100 "Increase Ann_Salary", salary+100 "Increase Salary"
from employees;
-- [tc 추가 풀이]
select emp_name "Name", job_id "Job", salary "Salary", 
(salary*100)*12 "Increase Ann_Salary" from employees;


-- [ 3 ] H R 부서에서 예산 편성 문제로 급여 정보 보고서를 작성하려고 한다. 
-- 사원정보(Employees) 테이블에서 급여가 $7,000~$10,000 범위 이외인 사람의 
-- 이름과 성(Name으로 별칭) 및 급여를 급여가 적은 순서로 출력하시오(75행).
select emp_name "Name", salary from employees
where salary<7000 or salary>10000
order by salary;

-- [tc 추가 풀이]
-- 월급이 7000~10000 범위에 있는 사원
select emp_name "Name", salary from employees
where salary between 7000 and 10000
;
-- 월급이 7000~10000 범위 외에 있는 사원 : not between
select emp_name "Name", salary from employees
where salary not between 7000 and 10000
;


-- [ 4 ] 사원의 성(last_name) 중에 ‘e’ 및 ‘o’ 글자가 포함된 사원을 출력하시오. 
-- 이때 머리글은 ‘e or o Name’이라고 출력하시오(8행).
select emp_name as "e or o Name" from employees
where emp_name like '%e%' or emp_name like '%o%';

-- [tc 추가 풀이]
-- - emp_name을 보면 first name과 last name의 첫 글자가 대문자이기 때문에 emp_name은 소문자로 변환 후 검색
select emp_name as "e or o Name" from employees
where lower(emp_name) like '%e%' or lower(emp_name) like '%o%'
;


-- [ 5 ] 이번 분기에 60번 IT 부서에서는 신규 프로그램을 개발하고 보급하여 회사에 공헌하였다. 
-- 이에 해당 부서의 사원 급여를 12.3% 인상하기로 하였다. 
-- 60번 IT 부서 사원의 급여를 12.3% 인상하여 정수만(반올림) 표시하는 보고서를 작성하시오. 
-- 보고서는 사원번호, 성과 이름(Name으로 별칭), 급여, 인상된 급여(Increase Salary로 별칭)순으로 출력하시오(5행).
select employee_id, emp_name "Name", salary, salary+round(salary*0.123,-1) "Increase Salary"
from employees
where department_id = 60
;

-- [tc 추가 풀이]
select employee_id, emp_name "Name", department_id, salary, round(salary+(salary*0.123)) "Increase Salary"
from employees
where department_id = 60
;


-- [ 6 ] 모든 사원의 연봉을 표시하는 보고서를 작성하려고 한다. 
-- 보고서에 사원의 이름과 성(Name으로 별칭), 급여, 수당여부에 따른 연봉을 포함하여 출력하시오. 
-- 수당여부는 수당이 있으면 “Salary + Commission”, 수당이 없으면 “Salary only”라고 표시하고, 
-- 별칭은 적절히 붙이시오. 또한 출력 시 연봉이 높은 순으로 정렬하시오(107행).
select emp_name "Name", salary,
case
when commission_pct is null then 'Salary only'
else 'Salary + Commission'
end as "Commission"
from employees
order by salary desc
;

-- [tc 추가 풀이]
-- 방법1 : case when then
select emp_name, salary,salary+nvl(salary*commission_pct,0) comm_salary, commission_pct ,
-- case when then
case 
when commission_pct is null then 'Salary only' -- then 뒤에는 ', "는 에러
when commission_pct is not null then 'Salary + Commission'
end as "commission_isNull"
from employees
order by salary desc
;
-- 방법2 : decode
select emp_name, salary,salary+nvl(salary*commission_pct,0) comm_salary, commission_pct ,
-- decode(salary
-- '3000', 'A',         ==> salary가 3000이면 A, 4000dlaus B
-- '4000', 'B',
-- '5000', 'C',
-- )
-- decode(department_id
-- '10', 'A',       
-- '20', 'B',
-- '30', 'C',
-- ) as dept
-- nvl2: nvl2(commission_pct,'null일 경우 조건', 'null이 아닐 경우 조건')
-- nvl2(commission_pct, 'Salary + Commission','Salary only')
 decode(commission_pct, null,'Salary only','Salary + Commission')
from employees
order by salary desc
;
select emp_name, salary,salary+nvl(salary*commission_pct,0) comm_salary, commission_pct ,
decode(department_id,
'10', 'A',     
'20', 'B',
'30', 'C')
as dept
from employees
order by salary desc
;
-- 방법3: nvl2
select emp_name, salary,salary+nvl(salary*commission_pct,0) comm_salary, commission_pct ,
-- nvl2: nvl2(commission_pct,'null일 경우 조건', 'null이 아닐 경우 조건')
nvl2(commission_pct, 'Salary + Commission','Salary only')
from employees
order by salary desc
;


-- [ 7 ] 각 사원이 소속된 부서별로 급여 합계, 급여 평균, 급여 최댓값, 급여 최솟값을 집계하고자 한다. 
-- 계산된 출력값은 여섯 자리와 세 자리 구분기호, $ 표시와 함께 아래와 같이 출력하시오. 
-- 단, 부서에 소속되지 않은 사원에 대한 정보는 제외하고, 출력 시 머리글은 다음 그림처럼 별칭(alias) 처리하시오(11행).
-- 출력 시 머리글은 "그룹함수명"을 별칭(alias) 처리하시오(11행).
select department_id, to_char(sum(salary),'$999,999') sum, to_char(avg(salary),'$999,999') avg, 
to_char(max(salary),'$999,999') max ,to_char(min(salary),'$999,999') min from employees
where department_id is not null
group by department_id;

-- [tc 추가 풀이]
select department_id, 
to_char(sum(salary),'$000,999,999') sum_sal, 
to_char(round(avg(salary),2),'$000,999,999') 
avg_sal, to_char(max(salary),'$000,999,999') max_sal, 
to_char(min(salary),'$000,999,999') min_sal 
from employees
group by department_id
;


-- [ 8 ] 사원들의 업무별 전체 급여 평균이 $10,000보다 큰 경우를 조회하여 업무별 급여 평균을 출력하시오. 
-- 단 업무에 사원(CLERK)이 포함된 경우는 제외하고 전체 급여 평균이 높은 순서대로 출력하시오(7행).
select job_id, avg(salary) from employees
where job_id not in ('CLERK')
group by job_id 
having avg(salary) >10000 
order by avg(salary) desc
;
-- [tc 추가 풀이]
-- 업무별 --> 직급별, job_id
select avg(salary) from employees
;
select job_id, avg(salary) from employees
-- where : 일반 컬럼의 조건을 넣는 곳
where job_id not like '%CLERK%'
group by job_id
-- having : 그룹컬럼의 조건을 넣는 곳
having avg(salary)>10000
;


-- [ 9 ] 각 사원과 직속 상사와의 관계를 이용하여 다음과 같은 형식의 보고서를 작성하고자 한다.
-- (예) 홍길동은 허균에게 보고한다 → Eleni Zlotkey report to Steven King
-- 어떤 사원이 누구에게 보고하는지 위 예를 참고하여 출력하시오.
-- 단, 보고할 상사가 없는 사원이 있다면 그 정보도 포함하여 출력하고, 상사의 이름과 성은 대문자로 출력하시오(107행).
select * from employees;
select a.employee_id, a.emp_name, a.manager_id, upper(b.emp_name) "manager_name" from employees a, employees b
where a.manager_id = b.employee_id 
order by a.employee_id
;

-- [tc 추가 풀이]
-- - 단, 보고할 상사가 없는 사원이 있다면 그 정보도 포함하여 출력하고, ====> outer join 사용
select a.employee_id, a.emp_name, a.manager_id, b.emp_name
from employees a, employees b
where a.manager_id=b.employee_id(+) -- null이 없는 쪽에 (+) 추가
order by a.employee_id
;


-- [ 10 ] Employees, Departments 테이블의 구조를 파악한 후 
-- 사원 수가 다섯 명 이상인 부서의 부서이름과 사원 수를 출력하시오. 이때 사원 수가 많은 순으로 정렬하시오(5행).
select department_id from employees;
select * from departments;

select a.department_id, department_name, count(a.department_id) from employees a, departments b
where a.department_id = b.department_id
group by a.department_id
having count(a.department_id)>= 5
order by count(a.department_id)
;

-- [tc 추가 풀이]
-- 1. 부서번호, 사원수
-- 2. 사원수 >= 5
-- 3. 사원수별 정렬
-- 부서별 인원
select department_id, count(department_id) from employees
group by department_id
having count(department_id)>=5
order by count(department_id) desc
;


--[추가 문제1] HR 부서의 어떤 사원은 급여정보를 조회하는 업무를 맡고 있다.
-- Tucker 사원보다 급여를 많이 받고 있는 사원의 이름과 성(Name으로 별칭), 업무, 급여를 출력하시오(15행).
select emp_name, salary from employees
where emp_name like '%Tucker%'
;
select emp_name, job_id, salary from employees
where salary >= (select salary from employees
where emp_name like '%Tucker%')
;

-- [tc 추가 풀이]
select salary from employees
where emp_name like '%Tucker%'
;
select salary from employees
where salary >10000
;
select salary from employees
where salary >(select salary from employees
where emp_name like '%Tucker%')
;
-- 전체 평균 월급 이상인 사원의 월급 출력는 방법과 동일
select salary from employees
where salary > (select avg(salary) from employees)
order by salary desc
;


-- [추가 문제2] 모든 사원의 소속부서 평균연봉을 계산하여 사원별로 이름과 성(Name으로 별칭), 업무,
-- 급여, 부서번호, 부서평균연봉(Department Avg Salary로 별칭)을 출력하시오(107행).
-- 내가 푼 거는 틀림. 부서평균연봉이 동일하게 나와, 잘 이해안가 공부하기
select department_id, round(avg(salary),-1) from employees
group by department_id
;

select emp_name, job_id, salary, department_id, round((select avg(salary) from employees),-1) 
"Department Avg Salary" from employees;

select emp_name, job_id, salary, department_id, round(avg(salary),-1) "Department Avg Salary" 
from employees, (select department_id, round(avg(salary),-1) from employees
group by department_id)
;

-- [tc 추가 풀이]
select avg(salary) from employees;
select emp_name, job_id, salary, department_id from employees;
-- 답
select emp_name, job_id, salary, department_id,
(select round(avg(salary),2) from employees a
where a.department_id = e.department_id) "Department Avg Salar"
from employees e
;

select department_id, round(avg(salary),2) from employees
group by department_id;

-- department_id가 50번인 부서의 평균 연봉만 계산돼
select department_id, round(avg(salary),-1) from employees
where department_id = 50
group by department_id
;

-- department_id = 50인 연봉의 평균 구해져
select round(avg(salary),-1) from employees
where department_id = 50
; -- ==> 답은 50을 e.department_id로만 변경된 것.

-- join
select salary, a.department_id, b.round_salary
from employees a,
(select department_id, round(avg(salary),2) round_salary from employees
group by department_id) b
where a. department_id = b.department_id
;

select emp_name from employees
where emp_name like '%a%'
;
-- 위의 코드에 연봉이 평균 이상인 조건 추가
-- - 먼저 연봉이 평균 이상인 사람 구해
select * from employees
where salary>(select avg(salary) from employees);
-- - 위의 코드를 테이블에 넣어줘
select emp_name from 
(select * from employees
where salary>(select avg(salary) from employees))
where emp_name like '%a%'
;

-- equi join 
select salary, a.department_id, department_name
from employees a, departments b
where a.department_id = b.department_id
;

-- [웹 스크래핑 퀴즈]
-- # 역대관객순
-- # 이미지, 제목, 누적관객수, 개봉일 
-- # 이미지 저장까지 해야 함.
-- # 2023, 2022, 2021, 2020

-- # 콘솔창에 출력하고 DB에 저장

-- DB
-- 테이블 명 : daum_movie
-- dno : 시퀀스
-- title 문자타입(100)
-- img 문자타입(100)
-- audience 숫자타입(10)
-- ddate 날짜타입

create table daum_movie(
dno number primary key,
title varchar2(100),
img varchar2(100),
audience number(10),
ddate date
);

create table coupang(
cno number primary key,
title varchar2(100),
img varchar2(100),
price number(10),
grade number(10),
eval_num number(10)
);

create table flight(
fno number(4),
airline varchar2(100),
departure_time date,
arrival_time date,
flight_time varchar2(20),
price number(10)
);