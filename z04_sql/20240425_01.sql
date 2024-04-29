-- ********** [암기] ********** -- 
-- 어제, 오늘, 내일 
select sysdate-1, sysdate, sysdate+1 from dual;
-- 오늘, 이달의 첫일, 이달의 마지막일
select sysdate, trunc(sysdate,'month'), last_day(sysdate) from dual;
-- 두 날짜간 일수, 두 날짜간 달수
select round(sysdate-hire_date,3), trunc(months_between(sysdate, hire_date),2) from employees;
-- trunc 일단위 버림, group by 그룹함수
select trunc(kor,-1) kor, count(trunc(kor,-1)) from stu_score
group by trunc(kor,-1)
order by kor
;
-- ****************************** --

-- [퀴즈] hire_date 날짜에서 월만 출력하시오.
-- 2008-01-01 형식으로 먼저 출력
select hire_date, to_char(hire_date,'yyyy-mm-dd') from employees;
select hire_date, to_char(hire_date, 'mm') from employees;

select to_char(hire_date, 'mm') hire_date, count(to_char(hire_date,'mm')) from employees
group by to_char(hire_date, 'mm')
order by hire_date
;

-- [퀴즈] hire_date yyyy년도, 년도별 인원수를 출력하시오.
select to_char(hire_date, 'yyyy') hire_date, count(to_char(hire_date,'yyyy')) from employees
group by to_char(hire_date, 'yyyy')
order by hire_date
;

-- 형변환, number, character, date
-- number : 사칙연산 가능, 쉼표, 원화 표시 불가
-- char : 사칙연산(+, -) 불가, 쉼표, 원화 표시 가능
-- date : 사칙연산(+, -) 가능, 날짜출력형태는 변경 불가 ==> to_char로 변환 후 출력 형태 변경 가능

-- [퀴즈] [암기] 시퀀스(stu_seq), 날짜의 년도로 학번 부여시오. 학번 5개 출력(kor+2024+0001)

select 'ko'||to_char(sysdate,'yyyy')||trim(to_char(stu_seq.nextval,('0000'))) from dual;
--                                                                   9999  : 공백을 그대로 둠. 0000은 공백을 0으로 표현

-- [퀴즈] 123,456,789, 156,788 더하기 값
select to_number(replace('123,456,789',',','')+replace('156,789',',','')) from dual;

-- [퀴즈] (123,456,789) + (100,000) = 123556789 출력
select to_number(replace('123,456,789',',',''))+to_number(replace('100,000',',','')) from dual;
-- 아래 방법이 replace 대체
select to_number('123,456,789','999,999,999') from dual;
select to_char(to_number('123,456,789','999,999,999')+to_number('100,000','999,999'),'999,999,999') from dual;


select to_char(salary, '999,999') from employees;


-- 숫자 타입을 날짜 타입으로 변경
select 20240425 from dual;
select to_char(20240425) from dual;
select to_date(20240425) from dual; -- 24/04/25

-- 숫자 타입을 날짜 타입으로 변경 +3 해보기
select 20240425+3 from dual; -- 20240428
select to_char(20240425)+3 from dual; -- 20240428
select to_char(20240425+3) from dual; -- 20240428
select to_char(20240425+3)+3 from dual; -- 20240431
select to_date(20240425+3) from dual; -- 24/04/28

-- 숫자타입을 날짜타입으로 변경
select emp_name, hire_date from employees
where hire_date > 20070101; -- error hire_date가 문자이기 때문에
select emp_name, hire_date from employees
where hire_date > '20070101';  -- 문자로 변경 또는 to_date 사용하여 형변환
select emp_name, hire_date from employees
where hire_date > to_date(20070101)
order by hire_date
; 

-- [퀴즈] 08월에 입사한 사원이름의 2번째 글자에 a가 들어가 있는 사람을 출력하시오. 
select emp_name, hire_date from employees
where to_char(hire_date,'mm')='08' and emp_name like '_a%'
;

-- [퀴즈] 01, 05, 08월에 입사한 사원이름의 2번째 글자에 a가 들어가 있는 사람을 출력하시오.  ===> or 사용
select emp_name, hire_date from employees
where to_char(hire_date,'mm')='01' or to_char(hire_date,'mm')='05' or to_char(hire_date,'mm')='08'
and emp_name like '_a%'
;

-- [퀴즈] 01, 05, 08월에 입사한 사원이름의 2번째 글자에 a가 들어가 있는 사람을 출력하시오.  ===> in 사용
-- 1. 입사일
select hire_date from employees
where to_char(hire_date,'mm') in('01','05','08')
;
-- 2. 이름
select emp_name from employees
where emp_name like '_a%'
;
-- 3. 입사일, 이름 합치기
select emp_name, hire_date from employees
where emp_name like '_a%' and to_char(hire_date,'mm') in ('01','05','08')
;

 -- [퀴즈] 20070101 이후 입사한 사원이름에 a가 들어가 있는 사람을 출력하시오. 
 select emp_name, hire_date from employees
 where hire_date>'20070101' and emp_name like '%a%'
 ;
-- + 됨
select sysdate+'20240401' from dual;
-- - 안됨. 에러 발생
select sysdate-'20240401' from dual;
-- 문자타입을 날짜타입으로 변경
select sysdate-to_date('20240401') from dual; 

select sysdate, '2024-04-01', sysdate-to_date('2024-04-01') from dual;

select * from m_date;

insert into m_date(m_no, m_yesterday) values(
m_no.nextval, '2024-04-01'  -- m_yesterday의 타입이 날짜여서 문자로 넣어도 자동으로 날짜로 변환됨
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

-- 입력 시 날짜 타입에 문자(형태-날짜형태)를 입력해도 저장됨.
-- 날짜와 문자를 빼기는 불가능, 그래서 문자를 날짜타입으로 변경해야 함.
insert into eventDate values(
m_no.nextval, sysdate, '2024-04-01', sysdate-to_date('2024-04-01')
);

select * from eventDate;

-- 문자타입을 숫자타입으로 변경
select to_number('20,000','99,999')-to_number('10,000','99,999') from dual;

-- null을 0으로 치환 nvl()
select salary, commission_pct, salary+(salary*nvl(commission_pct,0)) from employees;

-- manager_id null ceo
select manager_id from employees
order by manager_id desc
;

-- 숫자타입을 문자타입으로 변경
select nvl(to_char(manager_id),'ceo') from employees
order by manager_id desc
;

-- [그룹함수]
-- 그룹함수 : sum, avg, count(), count(*), min, max
-- count(*) : null값 포함하여 count
-- - 그 테이블 전체, 또는 일부
-- count : 개수
select count(emp_name) from employees; -- 결과값 : 107명
-- null값 있으면 count에서 제외
select count(manager_id) from employees; -- 결과값 : 106명
select emp_name, manager_id from employees;

-- sum : 총합
select to_char(sum(salary),'999,999') from employees;

-- avg : 평균
select avg(salary) avg_sal from employees;

-- min : 최소값, max : 최대값
select min(salary), max(salary) from employees;

-- [퀴즈] salary가 6461달러 보다 높은 사람 출력하시오 
select emp_name, salary from employees
where salary > 6461
;

-- [퀴즈] salary가 평균보다 높은 사람 출력 ==> 이중쿼리 사용 
select emp_name, salary from employees
where salary > (select avg(salary) avg_sal from employees)
;
-- 최소 연봉의 사원을 알고 싶어
select min(salary), emp_name from employees; -- ==> error, ORA-00937: 단일 그룹의 그룹 함수가 아닙니다

-- [퀴즈] 최소 월급을 받는 사람의 사번, 이름을 출력하시오.
select employee_id, emp_name from employees
where salary = 2100
; 
select employee_id, emp_name from employees
where salary = (select min(salary) from employees)
; 

-- [퀴즈] 최대 월급을 받는 사람의 사번, 이름을 출력하시오.
select employee_id, emp_name from employees
where salary=(select max(salary) from employees)
;

select department_id, salary from employees;
-- 부서번호가 50번인 사원만 전체 월급
select sum(salary) from employees
where department_id = 50
;


select count(*) from stu_score;

-- [quiz] kor 점수가 80점 이상인 학생 출력
select no, name, kor from stu_score
where kor >= 80
order by no
;
-- [quiz] kor에서 kor 점수 평균이상, eng에서 eng 점수 평균 이상인 학생 출력
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

-- [quiz] 국어점수 최고점인 학생, 영어점수 최고점인 학생, 수학점수 최고점인 학생 출력
select name, kor, eng, math from stu_score
where kor = (select max(kor) from stu_score) 
or eng = (select max(eng) from stu_score) 
or math = (select max(math) from stu_score)
;

-- [quiz] employees에서 월급이 최대, 최소, 평균인 사원을 출력하시오.
select emp_name, salary from employees
where salary = (select max(salary) from employees)
or salary = (select min(salary) from employees)
or salary = (select avg(salary) from employees)
;

-- 최대값
select emp_name, salary from employees
where salary = (select max(salary) from employees)
;

-- select max(salary) from (테이블)

-- 평균보다 낮은 값 : 56명, 56명 중 최대 연봉 : 6400
select emp_name, salary from employees
where salary <= (select avg(salary) from employees)
order by salary desc
;
-- 평균보다 낮은 값을 테이블로 쓸거야. ==> 6400 출력됨
select max(salary) from (select emp_name, salary from employees
where salary <= (select avg(salary) from employees)
order by salary desc)
;

-- 평균값보다 낮은 사원 중에 최대값을 출력하시오.
-- 1. 평균값보다 낮은 사원을 검색
-- 2. 검색된 사원 중에 최대값을 검색
select emp_name, salary from employees
where salary = 6400
;
-- 6400을 찾아야 해. 6400 찾는 방법을 6400에 넣어줘 
select emp_name, salary from employees
where salary = (select max(salary) from (select emp_name, salary from employees
where salary <= (select avg(salary) from employees)
order by salary desc))
;

-- [수학 함수] : ceil(a), floor(a), round(a), trunc(a) ==> 얘네는 외워
-- [문자함수] 
-- to_char : yyyy,mm,dd(ddd),hh,mi,ss,am/pm,day(dy) ==> 외워
-- inicap(a): 첫글자만 대문자, upper(a): 모두 대문자
-- lpad(데이터, 자리수, 채울 문자)
select emp_name, lpad(emp_name, 15, '#') from employees; -- ==>  왼쪽에 자리 수 만큼 빈공백에 # 넣어줘
-- rpad(데이터, 자리수, 채울 문자)
select emp_name, rpad(emp_name, 20, '@') from employees; -- ==> 오른쪽에 자리 수 만큼 빈공백에 @ 넣어줘
-- ltrim(데이터, 잘라올 문자) : 지정한 문자를 잘라내고 출력
select emp_name, ltrim(emp_name,'Do') from employees; -- ==> 'Do'글자 잘라옴
-- rtrim(데이터, 잘라올 문자) : 지정한 문자를 잘라내고 출력 

-- ko20240001
select 'ko20240001', ltrim('ko20240001','ko2024') from dual;

-- substr(데이터, 짤라올 자리(시작하는)수, 시작한 자리에서부터 가져올 개수)
-- substr(데이터, 순서, 개수) ex) substr('abcdegf', 3, 3) - > cde 
select emp_name, substr(emp_name, 3, 4) from employees;


select job_id from employees;
-- [퀴즈] job_id에 있는 SH와 사원번호를 결합해서 출력하시오.
select substr(job_id, 1, 2)||employee_id from employees;

-- length
select emp_name, length(emp_name) from employees
where length(emp_name) >15;

-- [날짜함수]
-- 날짜와 날짜를 더하면 오류 발생 ==> 날짜+날짜 불가능
select sysdate + hire_date from employees; -- ==> error ORA-00975: 날짜와 날짜의 가산은 할 수 없습니다
-- 날짜에 날짜를 빼면 그 사이의 일수가 나온다. ==> 날짜 - 날짜 가능
select sysdate - hire_date from employees;
-- 날짜에 숫자를 더하거나 빼면 날짜가 나온다.
select sysdate+1 from dual;
select sysdate-1 from dual;
-- 월 
select sysdate, trunc(sysdate, 'month'), round(sysdate, 'month') from dual;
-- 년
select round(sysdate, 'year') from dual;

-- add_months(데이터, 추가/축소 할 월 수) : 개월 수 추가/축소
select sysdate, add_months(sysdate, 3) from dual; -- ==> 현재에서 3개월 후
select sysdate, add_months(sysdate, -3) from dual; -- ==> 현재에서 3개월 전

-- ceil(올림), floor(버림), mod(나머지), power(제곱)
select ceil(-4.2), floor(-4.2), mod(8,3), power(2,10) from dual;

-- [퀴즈] 학생 테이블에서 이름과 생일을 "김진우 1979년09월19일 수요일" 형태로 출력
select * from employees;
select emp_name||to_char(hire_date, ' yyyy"년" mm"월" dd"일" day') from employees;

select emp_name||' '||to_char(hire_date, 'yyyy')||'년 '||to_char(hire_date, 'mm')||'월 '
||to_char(hire_date, 'dd')||'일 '||to_char(hire_date, 'day') from employees;

-- [퀴즈] 사원명, 자리수 9자리 빈공백 0으로 표시
-- 월급*1400 앞에 원화표시와 쉼표를 넣어 출력
select emp_name, to_char(salary*1400,'L000,000,000') from employees;

-- [퀴즈] 자신의 생일과 자신의 생일이 속한 달의 마지막 날을 구하시오.
select to_date(20101010), last_day(to_date(20101010)) from dual;
select '2010-10-10', last_day('10/10/10') from dual;
select trunc(to_date('2010-10-10'),'month'), '2010-10-10', last_day('2010-10-10') from dual;

-- [8장. DB 객체 타입]

-- [9장 alter table]
-- alter table : table 수정
-- drop table: table 삭제
-- DDL : 데이터 정의어(data definition language), create, alter, drop, truncate(테이블 초기화)
-- DML : 데이터 조작어(data manipulation language), select, insert,update,delete
-- DCL : 데이터베이스에 접근하거나 객체에 권한을 주는 등의 역할을 하는 언어(data control language), grant, revoke, commit, rollback

-- [alter table]

select * from member;

desc member;

-- DDL(Data Definition Language) : coloumn 추가, 수정, 삭제
-- DDL은 commit, rollback 없음. 바로 저장됨.
alter table member add gender varchar2(6) default 'female' not null;
desc member;
select * from member;

update member set gender='male';
select * from member;
commit;

-- 컬럼 수정 
-- - 컬럼이름변경
alter table member rename column name to stu_name;
-- - 타입 변경
alter table member modify(stu_name varchar2(50));
-- 기존의 데이터가 변경하려는 크기보다 작을 때만 가능.
update member set stu_name = '';
alter table memebr modify(stu_name varchar2(6));
-- 컬럼의 타입을 변경하려면 컬럼데이터가 빈공백이거나 null일 때 가능 
alter table memebr modify(stu_name varchar2(3));
alter table memebr modify(stu_name number(4 ));
select stu_name from member;
alter table member modify(stu_name number(100)); -- error, ORA-01727: 수치의 정도 범위(38 자리 이내)를 초과했습니다


desc member;



-- 컬럼삭제 : commit, rollback이 없음
alter table member drop column phone;
desc member;

select * from member;


