select * from employees;

-- 회원정보 테이블 생성
create table member( -- member는 테이블 이름
id varchar2(20), -- id는 컬럼 이름, varchar2는 문자형, 20은 자릿수(영문 기준 1자리(바이트)==> 예로 aaa는 3자리 차지, 한글의 경우 3자리==> 한글은 6자 작성 가능, 예로 이순신은 9자리를 차지)로 20자리를 사용하겠다는 의미
pw varchar2(20),
name varchar2(20),
phone varchar2(20)
);

-- 데이터 입력
insert into member(id, pw, name, phone) values(
'aaa', '1111', '홍길동', '010-1111-1111'
-- 문자(varchar2)라서 '' 안에 입력
);

insert into member values(  -- table에 있는 모든 열의 값을 입력할 경우 생략가능
'bbb', '1111', '유관순', '010-2222-2222'
);

insert into member (id, name, phone) values( -- 해당 열만 입력할 경우에는 해당 열 작성 필요
'ccc', '이순신', '010-3333-3333'
);

-- 컬럼 수 부족 에러, 에러 발생: 열과 값의 수가 일치하지 않음. 
/*
insert into member values(
'ddd', '강감찬', '010-4444-4444'
);

오류 발생 명령행: 25 열: 13
오류 보고 -
SQL 오류: ORA-00947: 값의 수가 충분하지 않습니다
00947. 00000 -  "not enough values"
*Cause:    
*Action:

*/

select id, pw, name, phone from member;
-- ID ccc의 경우 pw 값 입력하지 않아서 null로 출력
-- null : 값이 없는 것이 아닌 "무한대"를 의미, null에 *, -, +, /(사칙연산)하면 값이 null이 돼.


-- 위 데이터는 임시저장소에 있어. rollback하면 data 사라져, commit하면 저장됨.
commit;

-- commit을 하면 rollback해도 데이터는 없어지지 않아.
rollback;
select * from member; -- *는 모든 데이터(컬럼)을 의미
select id from member; -- id만 보여줘
select id, name from member; -- id, name 보여줘

insert into member values(
'ddd', '1111', '강감찬', '010-4444-4444'
);

select * from member;

rollback; -- commit한 이후로 돌아감. commit 이전으로 돌아가지 않아.
select * from member;

commit;

select * from member;

update member set pw='2222'; -- 모든 pw값이 2222로 변경됨
select * from member;
rollback;

-- where라는 조건절을 입력해주어야 해.
update member set pw='2222' where id='ccc'; -- ==> id가 ccc인 절에만 pw를 2222로 바꿔줘.

-- 내가 가진 모든 테이블 확인 가능
select * from tab; 

-- 테이블의 타입 확인
desc member;

/*
오라클 타입
- number: 숫자
- date: 날짜
- char: 고정문자
- vhrchar2: 가변문자
- clob: 대용량문자
*/

-- number: 정수와 실수가 있음.
-- number(4): 4자리 숫자로 -9999~9999 표현 가능

create table mem(
no number, -- 데이터(값) 길이 미 지정. 무한대(무조건 값 다 들어가). 그렇지만 적정길이까지만 돼.
no2 number(4),
no3 number(4,2) -- 총 4자리를 사용할건데 2자리는 무조건 소수점 자리야 즉 00.00 이렇게 출력됨.
);

insert into mem (no) values(1234567890);
insert into mem (no2) values(9999);
insert into mem (no2) values(1.11); -- 값은 1이 출력. 정수부분만 나오므로 1만 출력. -9999~9999 출력하므로 1도 출력 가능
insert into mem (no2) values(1.6); -- 반올림하여 2가 출력
-- insert into mem (no2) values(99991); -- no2는 number(4)이므로 5자리 숫자를 입력하면 error 발생
insert into mem (no2) values(-9999);
-- insert into mem (no2) values(-99991); -- no2는 number(4)이므로 5자리 숫자를 입력하면 error 발생
-- 크기를 지정했을 때 검색 시 데이터의 크기를 한번 더 읽지 않고 데이터를 읽어 처리 시간이 크기를 지정하지 않았을 때 보다 더 빠르다.
insert into mem (no3) values(11.11);
insert into mem (no3) values(111); -- 111.00이 되므로 5자리가 되어 error 발생

select * from mem;

commit;

create table mem2 (
no number(4,2),
mdate date, -- date: 년, 월, 일, 시, 분, 초까지 저장 가능
mdate2 timestamp -- date = timestamp 단, timestamp는 밀리초까지 저장 가능
);

insert into mem2 (mdate) values('2024-04-19'); -- date는 문자형으로 입력해도 날짜로 인식
insert into mem2 (mdate) values(sysdate); -- 현재시간
insert into mem2 (mdate2) values(sysdate);

select * from mem2; -- 2024-04-19로 입력해도 24/04/29로 출력(기본형), 시/분/초 생략되어 있음. 시간은 보이지 않지만 같이 불러와져있어.
select to_char(mdate, 'yyyy-mm-dd hh:mi:ss') from mem2;
select to_char(mdate, 'yyyy/mm/dd hh:mi:ss.ff') from mem2; -- error, date에는 밀리세컨드 없으므로 지원하지 않음.
select to_char(mdate2, 'yyyy/mm/dd hh:mi:ss:ff') from mem2;

-- '2024-04-19' 이렇게 varchar2로 받아도 되지만, date는 더하기 빼기가 돼.
-- 현재 날짜에서 2일 뒤
select mdate+2 from mem2;
-- 현재 날짜의 30일 뒤 ==> 무조건 create 된 것만 저장되므로 mdate+30은 그냥 [질의 결과]에서 보여주는 것. 
-- mdate+30을 추가하고 싶으면 
insert into mem2 (mdate, mdate2) values(sysdate, sysdate+30);
select mdate, mdate+30 from mem2;


select * from employees;
select sysdate-hire_date from employees;

create table mem3(
no number(4,2),
tel char(8),
name varchar2(9),
mdate date,
mdate2 timestamp
);

-- 문자형 저장 방법: char, varchar2
--char : 고정문자
insert into mem3 (tel) values('11112222');
insert into mem3 (tel) values('22223333');
insert into mem3 (tel) values('111');
insert into mem3 (tel) values('123456789'); -- error
insert into mem3 (tel) values('홍');

-- varchar2: 가변문자
insert into mem3 (name) values('11112222');
insert into mem3 (name) values('홍길동'); -- 한글(한 글자): 3크기
insert into mem3 (name) values('신사임당'); -- 12자리 필요
INSERT INTO MEM3 (NAME) VALUES('AAA');  
insert into mem3 (name) values('aaa'); 

commit;

select * from mem, mem2;
select * from mem3 where name='aaa'; -- sql 구문은 대소문자 구분 없음. 데이터는 대소문자 구분함.
select * from mem3 where name='AAA';
select * from mem3 where lower(name)='aaa';

-- select, from 2개의 키워드로 구성됨
-- 모든 컬럼 출력할 때: select * from (테이블 명);
-- 대소문자를 구분하지 않음. data(값)은 구분

select * from mem;
SELECT * FROM MEM;

select emp_name, department_id from employees;

-- distinct: 같은 것은 1번만 출력(중복 제거)
select distinct department_id from employees;

select * from departments;
select department_id, department_name from departments;

select * from employees;
select employee_id, emp_name, salary from employees;
-- 보고 싶은 열을 순서대로 적으면 기존 table과 다른 내가작성한 순서로 출력
select employee_id, job_id, emp_name, salary from employees;

select * from jobs;

select * from products;

select * from mem3;
-- 컬럼의 위치를 바꾸고 싶으면 바꿔서 적으면 됨.
select no, mdate2, tel, name, mdate from mem3; 
select * from employees;

-- 사원번호(employee_id), 사원이름(employee_name), 급여(salary), 입사일자(hire_date) 출력
select employee_id, emp_name, salary, hire_date from employees;

desc employees;

-- 테이블 삭제
drop table stu_score;

create table stu_score(
no number,
name varchar2(30),
kor number(3),
eng number(3),
math number(3),
total number(3),
avg number(5,2),
rank number
);

insert into stu_score values(
1, '홍길동',100,100,100,300,100,1
);

insert into stu_score values(2, '이순신',100,100,100,300,100,1);

insert into stu_score values(
3, '유관순',100,100,100,300,100,1
);

insert into stu_score values(
4, '강감찬',100,100,100,300,100,1
);

insert into stu_score values(
5, '김구',100,100,100,300,100,1
);

commit;

select * from stu_score;


-- 산술연산자 number 타인인 경우에만 가능
select * from stu_score;

insert into stu_score values(
6, '김유신', 100, 95, 96, (100+95+96),((100+95+96)/3),1
);

insert into stu_score values(
7, '홍길자', 100, 100, 99, (100+100+99), (100+100+99)/3, 1
);

select * from stu_score;

-- 번호, 이름, 국어점수, 국어점수-20, 평균, 국어점수-20을 한 평균
select no, name, kor, kor-20,avg,(kor-20+eng+math)/3 from stu_score;



select * from employees;

-- 달러, 원화 환산 - 1381.79
select employee_id, emp_name, salary from employees;

select employee_id, emp_name, salary, salary*1381.79 from employees;

-- 월급 * 12 = 연봉
-- 달러연봉, 원화연봉을 구하시오.
select employee_id, emp_name, salary*12, salary*1381.78*12 from employees;

-- 커미션은 월급*커미션, 실제 월급은은 월급+(월급*커미션)
-- commission_pct
select employee_id, emp_name, salary+(salary*commission_pct) from employees;
-- null의 경우에는 ? 또는 무한대를 의미하므로 별도의 값을 지정해주어야 함.
-- nvl(컬럼, 0) ==> 컬럼의 null값을 0으로 지정해주어야 한다는 의미
select employee_id, emp_name, nvl(commission_pct,0),salary+(salary*nvl(commission_pct,0)) from employees;

select * from employees;




