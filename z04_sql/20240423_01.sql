select * from students;

-- 순차정렬
select * from students
order by name asc;

-- drop table students;

-- column 추가
alter table students add rank number(3);
select * from students;
update students set rank=0;
select * from students;
commit;

select total, rank() over(order by total desc) rank
from students;

update students set total=0; 

select * from students;
select total, rank from students
order by total desc;

update students set total=(kor+eng+math);

update students s1 set rank = (select ranks from 
(select no, rank() over(order by total desc) as ranks from students) s2
where s1.no=s2.no);

-- 1. update 구문
update students a set rank = (rank);

-- 2. no, rank() 구문
(select no, rank() over(order by total desc) ranks from students) b);
-- 위의 구문이 하나의 table 이름으로 너무 기니까 b로 별칭

-- 3. update 구문과 rank() 구문을 no 컬럼으로 비교, rank 컬럼을 검색
update studenst a set rank=(
select ranks from (students) b
where a.no = b.no);

-- 4. students 테이블에서 ranks가 들어가 있는 테이블을 넣어줌. 
update students a set rank = (
select ranks from (select no, rank() over(order by total desc) ranks from students) b
where a.no = b.no);

select no, total, rank from students
order by total desc;

update students a set rank=(select rank() over(order by total desc) rank
from students b where a.no = b.no);

-- update students a set rank = (select ranks from (select no, rank() over(order by
total desc) ranks from students) s2 where s1.no =s2.no);

-- 역순 정렬
select no, total, rank from students
order by total desc;

-- no 순차정렬
select no, total, rank from students
order by no;

select no, kor, eng, math, total, rank from students 
order by kor desc, eng asc;

select manager_id from employees
order by manager_id desc;

select hire_date from employees
order by hire_date;

-- 최대값
select max(hire_date) from employees
order by hire_date;

-- 최소값
select min(hire_date) from employees
order by hire_date;

-- 최대값 - 최소값
select max(hire_date)-min(hire_date) from employees
order by hire_date;
select max(kor)-min(kor) from students;

select max(kor), max(eng), max(math) from students;

-- 퀴즈 1.
-- hire_date로 오름차순, 컬럼 사원번호, 사원명, job_id-직급, 입사일, 월급 컬럼 출력
select * from employees;
select employee_id, emp_name, job_id, hire_date, salary from employees
order by hire_date;

-- 퀴즈 2.
-- 급여를 적게 받는 사람 순으로 출력하되, 월급이 같으면 사원명으로 순차정렬하시오.
select * from employees
order by salary, emp_name;


-- 숫자함수
-- abs: 절대값
-- dual은 가상 테이블 
select -10, abs(-10) from dual;
-- floor는 소수점 이하 다 버림 
select 34.789, floor(34.789) floor, round(34.789) round from dual;

-- round(대상, 자리수) ex) round(34.718,2) 소수점 2자리까지 표시
select 34.178, round(34.178) round, round(34.178, 2) round2 from dual; 

select avg from students;
select round(avg,2) avg from students;

-- -1에서 반올림은 1의 자리에서 반올림을 의미. -2는 십의자리에서 반올림, ...
select 34.567, round(34.5678, -1) from dual;

-- trunc: 지정한 자리수 이하 버림
select trunc(34.5678, 2) from dual;
select trunc(34.5678, -1) from dual;
select trunc(34.5678) from dual;

-- ceil: 소수점 자리에서 올림
select ceil(34.123) from dual;


-- 국어점수 일단위 절사해서 출력
select trunc(kor,-1) from students
order by kor
;

-- kor, eng, math 일단위 절사해서 kor, eng, math 합계 출력
select trunc(kor,-1) + trunc(eng,-1) + trunc(math,-1) as trunc_total from students;
-- k+e+m 으로하면 안나와 trunc(kor,-1) + trunc(eng,-1) + trunc(math,-1) as trunc_total로 해주어야 함.
select trunc(kor,-1) k, trunc(eng,-1) e, trunc(math,-1) m, 
(trunc(kor,-1) + trunc(eng,-1) + trunc(math,-1)) total from students;

-- mod : 나머지
select round(10/7,2) from dual;
select mod(10,7) from dual;
-- 나누기는 그냥
select 10/7 from dual;

-- 퀴즈. 사원번호가 짝수인 것을 출력하시오.
-- 파이썬 employee_id%2 = 0
select employee_id from employees
where mod(employee_id,2)=0;

-- 몫만 
select floor(10/7) from dual;
-- 나머지만, 나머지가 0이면 짝수, 1이면 홀수
select mod(10,7) from dual;

-- 퀴즈. 학번이 3의 배수인것만 출력하시오. students 테이블
select * from students
where mod(no,3)=0;


-- [6장 시퀀스]
-- 기본 키: 행을 구분하기 위한 기본 키.  null값 없어. 항상 유일한 키로 중복되지 않아. ==> 자동번호발생기. 유일한 primary key
create sequence seq_no 
increment by 1 -- 1씩 증감
start with 1 -- 1부터 시작
minvalue 1 -- 최소값
maxvalue 9999 -- 최대값
nocycle -- 순환하지 않음
nocache; -- 캐시 사용하지 않음

-- nextval : 시퀀스 번호 1씩 증가, 숫자가 1씩 카운트 돼
select seq_no.nextval from dual;

-- currval : 시퀀스 번호 확인 ==> 현재 값 확인
select seq_no.currval from dual;

-- drop table member;
-- 삭제 후에는 주석 처리

-- drop table mem3;

create table member (
mno number(4),
id varchar2(30),
pw varchar2(20),
name varchar2(30),
phone varchar2(15)
);

create sequence seq_mno
increment by 1
start with 1
minvalue 1
maxvalue 9999
nocycle
nocache
;

select seq_mno.nextval from dual;

insert into member values (
seq_mno.nextval, 'eee','1111','김구','010-5555-5555'
);
select * from member;

-- 현재 날짜에서 년도 추출
select sydate from dual;
select to_char(sysdate,'yyyy') from dual;
-- ||: 문자 합치기
select 's0000'||to_char(seq_mno.currval) from dual;
-- trim() : 공백제거
select 's0000'||trim(to_char(seq_mno.currval)) from dual;


-- 퀴즈.
-- 한국대학교 학번 ko+입학년도+00001(ko202400001, ko202400002, .....) 출력
-- 시퀀스 seq_ko, 1-9999
create sequence seq_ko
increment by 1
start with 1
minvalue 1
maxvalue 9999
nocycle
nocache;

-- '00000': 자리수
select 'ko'||to_char(sysdate,'yyyy')||trim(to_char(seq_ko.nextval,'00000')) as stuno from dual;

-- 게시판
create table board (
bno number(5) primary key,
btitle varchar2(1000),
bcontent varchar2(3000),
id varchar2(30),
bdate date,
bhit number(10)
);
-- cycle: 중복 가능. 중복 발생 시 error

-- 퀴즈
-- 시퀀스 생성: seq_deptno, 시작1001, 증감 10, 최소값 1, 최대값 99999, cycle
-- 5번 실행
create sequence seq_deptno
increment by 10
start with 1001
minvalue 1
maxvalue 99999
cycle 
nocache;

select seq_deptno.nextval from dual;

create table emp01(
empno number(4) primary key,
ename varchar2(30),
hire_date date
);
-- 시퀀스 수정
alter sequence emp_seq
increment by 1001
;

create sequence emp_seq
increment by 1
start with 1
minvalue 1
maxvalue 9999
nocycle
nocache;

insert into emp01 values(
emp_seq.nextval, '이순신',sysdate
);

select * from emp01;

commit;

-- 퀴즈 1. 입사일 오름차순 정렬, 사번, 이름, 직급, 입사일 출력
select * from employees;

select employee_id, emp_name, job_id, hire_date from employees
order by hire_date;

--퀴즈 2. 현재까지 입사한 일수를 함께 출력(반올림)
select employee_id, emp_name, job_id, hire_date, ceil(sysdate-hire_date)||'일' from employees
order by hire_date;

select emp_name from employees;

-- Quiz
-- 직급과 사번을 합쳐서 출력
select job_id||employee_id from employees;
-- 앞에 두자리만 출력하고 싶어
-- substr(대상, 시작위치, 개수) : 문자열 자르기 함수
select substr(job_id,0,2) from employees;

select emp_name, substr(emp_name,1,3) from employees;

select substr('abcde',2,3) from dual;

-- Quiz
-- job_id에서 앞에 두 문자와 사번5자리 (00101)를 만들어 함께 출력하시오.
select substr(job_id,1,2)||'00'||employee_id from employees;
-- 선생님 코드
select substr(job_id,0,2),employee_id,to_char(employee_id,'00000'), 
substr(job_id,0,2)||trim(to_char(employee_id, '00000')) from employees;

-- 날짜함수
select sysdate from dual;

select to_char(sysdate,'yyyy-mm-dd hh:mi:ss') from dual;

-- months_between(날짜1, 날짜2) : 두 날짜 사이의 개월 수 확인
select months_between(sysdate,hire_date), sysdate-hire_date from employees;

-- add_months(기준날짜, 개월수) : 개월수를 추가
select sysdate, add_months(sysdate, 2) from dual;

-- next_day(기준날짜,요일): 입력한 날짜를 기준으로 다음번 요일을 알려줌 ==> 기준날짜 다음으로 돌아오는 요일을 날짜로 출력
select next_day(sysdate,'월요일') from dual;

-- last_day(날짜) : 입력한 날짜를 기준으로 마지막 일을 알려줌.
select last_day(sysdate) from dual;
select last_day('2024-02-01') from dual;