-- [9장 alter table]
-- table 복사
-- 테이블 생성
create table emp01(
emp_id number(6),
emp_name varchar2(80),
hire_date date
);

-- (테이블 생성)table 복사 : 기존 테이블 구조 및 데이터 모두 복사
desc employees;

create table emp02 as
select * from employees;

select * from emp02;
select * from employees;

-- 테이블 구조만 복사하기
create table emp03 as 
select * from employees where 1=2;
select * from emp03; 

select * from emp01; -- 컬럼 3개
select * from employees; -- 컬럼 14개
-- 테이블 구조가 다르면서 데이터만 복사하기(안에 있는 구조가 3개 -> 14개)
insert into emp01(emp_id, emp_name, hire_date)
select employee_id, emp_name, hire_date from employees;

select * from emp01 order by emp_id desc;

-- 데이터 1개 추가
insert into emp01 values(
 207, '홍길동','2024-04-26'
);

select * from emp01 order by emp_id desc;

-- 테이블 구조가 같으면서 데이터만 복사
insert into emp03
select * from employees;

select * from emp03;

-- drop table s_info;
-- drop table m_date;

desc member;

-- 컬럼 타입 변경
alter table member
modify(stu_name varchar2(30));

-- 컬럼 삭제
alter table member
drop column pw;

desc member;

-- 컬럼 추가(맨 오른쪽)
alter table member
add (pw varchar2(30)); 

desc member;

select * from member;

-- 현재 컬럼 순서는 아래와 같음.
select mno, id, pw, stu_name, gender from member; -- ==> 보여지기만 하고 데이터 입력은 pw 제일 마지막에.
select * from member;
insert into member values(
m_no.nextval, 'fff', '김유신','male', '1111'
);
select * from member;
insert into member values(
m_no.nextval, 'ggg', '1111', '홍길자','male'
); -- ==> error 

-- 컬럼 순서 변경 : 컬럼을 안보이게 숨긴 후 다시 보이게 하기
-- 먼저, stu_name, gender 열 안보이게 해줘, 컬럼 숨기기
alter table member modify stu_name invisible;
select * from member;
alter table member modify gender invisible;
select * from member;
-- 숨긴 것을 다시 나타나게 하면(컬럼 보여주기) 제일 오른쪽 열에 붙어
alter table member modify stu_name visible;
select * from member;
alter table member modify gender visible;
select * from member;

-- 컬럼의 일시적 사용 제한
alter table member
set unused(id);
select * from member; -- > id 안 보여

-- 사용 제한된 컬럼들의 사용 제한 해제
alter table member
drop unused columns;
select * from member; 

-- 테이블 삭제
-- drop table emp03;

-- 테이블 이름 변경
rename emp01 to employees01;

-- [9장 종료] 

-- [10장 무결성 제약 조건]
-- 무결성제약조건 : 무결성이란, 결점이 없어야 한다는 의미로, 오라클의 데이터는 무결성 조건이어야 함. ==> 데이터가 더 안정적으로 들거아.
-- 무결성제약조건이란 테이블에 부적절한 자료가 입력되는 것을 방지하기 위해 테이블을 생성할 때 각 컬럼에 대해서 정의하는 여러 가지 규칙
-- 무결성제약조건: not null(null 미허용), unique(중복값 미허용, 항상 유일한 값을 갖도록 함, null은 허용), 
--               primary key(유일키, null 미허용, 중복된 값 미허용, not null 조건과 unique 조건 결합 형태)
--               foreign key(참조되는 테이블의 칼럽의 값이 존재하면 허용), check(저장 가능한 데이터 값의 범위나 조건을 지정하여 설정한 값만을 허용)

desc employees;    

-- [ 무결성 제약조건 ]
-- foreign key는 다른 테이블에서 데이터 입력 시 선언되어 있는 기존 테이블에 입력하려는 데이터가 있는지 확인 ==> 있으면 저장시켜주고 없으면 저장시켜 주지 않음.

-- drop table employees01;
-- drop table emp02;
-- drop table member;
-- drop table board;

create table member (
id varchar2(30) primary key,
pw varchar2(30) not null,
name varchar2(30),
gender varchar(6)
);

insert into member values(
'aaaa','1111','홍길동','male'
);


insert into member(id, pw, name) values(
'bbb','1111','유관순'
);

select * from member;

insert into member(id, pw) values(
'ccc','1111'
);
-- error
select * from member;
insert into member(id) values( 
'ddd'
); -- ==> error ORA-01400: NULL을 ("ORA_USER"."MEMBER"."PW") 안에 삽입할 수 없습니다

insert into member (id,pw) values(
'ddd', '1111'
);

insert into member (id,pw) values(
'aaaa', '1111'
); -- ==> error ORA-00001: 무결성 제약 조건(ORA_USER.SYS_C007343)에 위배됩니다 => id에 제약조건을 걸었기 때문에 동일한 id 입력 시 에러 발생. null도 에러

insert into member (id,pw,name) values(
'a', '1111', '홍길동'
);
select * from member;

-- 제약 조건: not null : null값만 제외
create table emp02(
empno number(4) not null,
ename varchar2(10) not null,
job varchar2(9),
deptno number(2)
);

insert into emp02 values(
'5','안창호','부장','50'
);

select * from emp02;

-- 제약 조건: unique : 중복만 제거, null 허용
create table emp03(
empno number(4) unique,
ename varchar2(10) not null,
job varchar2(9),
deptno number(2)
); 

insert into emp03 values(
'1', '홍길동','1','1'
);

insert into emp03 values(
null, '홍길동','1','1'
);
select * from emp03;

insert into emp03 values(
'3', '이순신','2','2'
);

insert into emp03 values(
null, '강감찬','2','2'
);

insert into emp03 values(
'1', '김구','3','3'
); -- error ORA-00001: 무결성 제약 조건(ORA_USER.SYS_C007347)에 위배됩니다


--[퀴즈] 1번 홍길동 검색
select * from emp03
where empno = 1;

-- [퀴즈] null 홍길동 검색
select * from emp03
where empno is null and ename = '홍길동';

-- [퀴즈] null인 모든 사람 검색
select * from emp03
where empno is null;

-- null이 아닌 사람 검색 시에는 
select * from emp03
where empno is not null;

create table emp01(
empno number(4) primary key,
ename varchar2(10) not null,
job varchar2(9) ,
deptno number(2)
);

-- 5개 null, 1, 2, 3, 1
insert into emp01 values(
'1','홍길동','사원','1'
);

insert into emp01 values(
'1','윤동주','대리','1'
); -- error ORA-00001: 무결성 제약 조건(ORA_USER.SYS_C007349)에 위배됩니다

insert into emp01 values(
'2','윤동주','대리','1'
); 

insert into emp01 values(
null,'김소월','과장','1'
); -- error ORA-01400: NULL을 ("ORA_USER"."EMP01"."EMPNO") 안에 삽입할 수 없습니다

insert into emp01 values(
3,'김소월','과장','1'
);

insert into emp01 values(
4,null,'차장',2
); -- error ORA-01400: NULL을 ("ORA_USER"."EMP01"."ENAME") 안에 삽입할 수 없습니다

insert into emp01 values(
4,'김소월','차장',2
);

select * from emp01; 

-- [퀴즈] 4번 김소월 검색
select * from emp01
where empno = 4;

-- foreign key(외래키)
-- primary key로 저장되어야 foreign key로 등록 가능!
-- drop table emp01;

-- emp01 테이블 생성
create table emp01(
empno number(4) primary key,
ename varchar2(20) not null,
job varchar2(9),
deptno number(6)
);
alter table emp01
modify(deptno number(6));

insert into emp01 values(
1, '홍길동', '0001', 10
);

insert into emp01 values(
2, '유관순', '0002', 20
);

insert into emp01 values(
3, '이순신', '0002', 30
);

-- deptno 10-270

insert into emp01 values(
4, '김구', '0003', 270
);

insert into emp01 values(
5, '강감찬', '0004', 280
); -- error ORA-02291: 무결성 제약조건(ORA_USER.FK_DEPTNO)이 위배되었습니다- 부모 키가 없습니다
-- 외래키가 삭제가 되면 deptno에 없는 데이터를 입력해도 저장됨.

-- foreign key 삭제
alter table emp01
drop constraint fk_deptno;

insert into emp01 values(
5, '강감찬', '0004', 280
); -- 1 행 이(가) 삽입되었습니다.

commit;

-- emp01에 foreign key 추가
-- fk_deptno 별칭
-- add constraint 별칭 foreign key(현재컬럼) references 다른 테이블(컬럼이름)
alter table emp01 
add constraint fk_deptno foreign key(deptno)
references dept01(deptno)
;

select * from dept01;

alter table emp01
modify(deptno number(6));

-- dept01 테이블 생성
create table dept01(
deptno number(6) primary key,
dept_name varchar2(80)
);

-- select * from departments;

-- insert into dept01 (deptno, dept_name)
-- select department_id, department_name from departments;

desc departments;

-- 컬럼의 타입 변경
alter table dept01
modify (deptno number(6));

alter table dept01
modify (dept_name varchar2(80));
-- 컬럼의 내용 추가
insert into dept01 (deptno, dept_name)
select department_id, department_name from departments;

-- 컬럼 타입 변경
alter table emp01
modify (dept_name number(8));

desc member;

-- board table 생성
create table board(
bno number(4) primary key,
id varchar2(30),
btitle varchar2(1000),
bcontent varchar2(3000)
);

insert into board values(
1, 'aaa', '게시글1','내용1'
);
insert into board values(
2, 'bbb', '게시글2','내용2'
);
insert into board values(
3, 'ccc', '게시글3','내용3'
);
insert into board values(
4, 'ddd', '게시글4','내용4'
);
insert into board values(
5, 'aaa', '게시글5','내용5'
);
insert into board values(
6, 'aaa', '게시글6','내용6'
);
insert into board values(
7, 'aaa', '게시글7','내용7'
);
insert into board values(
8, 'bbb', '게시글8','내용8'
);

select * from board;

alter table board
add constraint fk_id foreign key (id)
references member(id);

-- [확인필요]
-- select * from member
-- where table_name = ''

-- comment table 댓글테이블 
-- 테이블 생성, 이름: comment
-- cno number(4) primary key
-- bno number(4)
-- cpw varchar2(20)
-- content varchar2(1000)

create table comments(
cno number(4) primary key,
bno number(4),
cpw varchar2(20),
content varchar2(1000),
constraint fk_bno foreign key(bno)
references board(bno)
);

-- 댓글달기
insert into comments values(
1, 5, '1111', '댓글내용1'
);
insert into comments values(
2, 1, '1111', '댓글내용2'
);
insert into comments values(
3, 5, '1111', '댓글내용3'
);
insert into comments values(
4, 2, '1111', '댓글내용4'
);
insert into comments values(
5, 5, '1111', '댓글내용5'
);
select * from board;

select * from comments;

-- fk 등록 시 설정
-- - fk키로 등록되어 있는 모든 데이터를 삭제시키는 것.
-- - fk키로 등록되어 있는 데이터는 모두 존재시키는 것
delete board where bno =5;

-- 외래키 삭제
alter table board drop constraints fk_id;
alter table comments drop constraints fk_bno;

select * from board;
select * from comments;

delete board where bno=1;

alter table board
add constraints fk_id foreign key(id)
references member(id);

-- fk_cno가 삭제되도록 함.
alter table comments 
add constraint fk_bno foreign key(bno)
references comments(bno) on delete cascade;

delete comments where cno=2; -- 먼저 삭제해야 아래가 삭제 돼(primary key 먼저 삭제해야 foreign key 삭제 가능)


-- check : 제약조건 특정값의 범위, 특정값만 입력되도록 함
create table emp(
empno number(4) primary key,
ename varchar2(20) not null,
job varchar2(9) default '0001' , -- column에 데이터를 넣지않으면 자동으로 0001이 저장.
sal number(7,2) check (sal between 2000 and 20000),
gender varchar2(6) check(gender in('남자','여자'))
);

insert into emp(empno, ename, job, sal, gender) values(
1,'홍길동''0002',3000,'남자'
);

insert into emp(empno, ename, job, sal, gender) values(
2,'유관순''0003',4000,'여자'
);
-- 에러 남자, 여자만 가능
insert into emp(empno, ename, job, sal, gender) values(
3,'이순신''0004',5000,'중성'
);

insert into emp(empno, ename, job, sal, gender) values(
3,'이순신''0004',5000,'남자'
);

insert into emp(empno, ename, job, sal, gender) values(
4,'강감찬''0005',2000,'남자'
);
-- 에러 2000 ! 20000
insert into emp(empno, ename, job, sal, gender) values(
5,'김구''0006',1000,'남자'
);
-- check 2000-20000
insert into emp(empno, ename, job, sal, gender) values(
5,'김구''0006',20000,'남자'
);
-- job default '0001' ==> job 입력 안하면 0001
insert into emp(empno, ename, sal, gender) values(
6,'김유신',10000,'남자'
);

select * from emp