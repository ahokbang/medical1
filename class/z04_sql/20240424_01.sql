-- [날짜함수]
-- trunc : 버림
select sysdate, hire_date, trunc(sysdate-hire_date, 3) from employees; -- 지정 자리수에서 버림
-- round : 반올림
select sysdate, hire_date, round(sysdate-hire_date, 3) from employees; -- 반올림

-- 어제 날짜 : sysdate-1
-- 내일 날짜 : sysdate+1
select sysdate-1 어제, sysdate 오늘, sysdate+1 내일, sysdate+100 from dual;

-- 퀴즈) m_no(시퀀스) : 1 - 9999 1씩 증가, 5번 반복해서 저장
-- column : m_yesterday, m_today, m_tomorrow, m_year 날짜컬럼을 가진 테이블 m_date
-- 어제, 오늘, 내일, 1년후 날짜를 저장하시오.
-- 날짜: date와 timestamp 사용 가능 timestamp는 밀리초까지 출력 가능
-- 시퀀스 생성
create sequence m_no
increment by 1
start with 1
minvalue 1
maxvalue 9999
cycle
nocache
;
-- 테이블생성
create table m_date(
m_no number(1) primary key,
m_yesterday date,
m_today date,
m_tommorow date,
m_year date
);
-- 1개 row 저장
insert into m_date values(
m_no.nextval, sysdate-1, sysdate, sysdate+1, sysdate+365
);
-- 검색
select * from m_date;

-- 회원들이 1년동안 로그인 없으면, 법적으로 회원유지 동의

-- abs :절대값
select hire_date-sysdate from employees; -- 음수 출력 --> abs로 절대값 씌워서 양수로 변환
select abs(hire_date-sysdate) from employees; 
-- ceil(올림), floor(버림), round(반올림, 자릿수), tunc(버림, 자릿수)
-- 날짜의 월을 기준으로 반올림
select hire_date, round(hire_date,'month') from employees;
-- 날짜의 월을 기준을 버림
select hire_date, trunc(hire_date,'month'), round(hire_date,'month') from employees;

select trunc(hire_date,'month') 기준일, hire_date from employees
order by hire_date;

select * from channels;

select * from kor_loan_status
order by period;

-- period 201111이 얼마나 나오는지 그룹핑 ==> 개수 확인 ===> count(해당 열)
select period, count(period) from kor_loan_status
group by period 
order by period;

select period from kor_loan_status
where period = '201111' ;



select * from students;
-- student table에서 국어점수 버림
select trunc(kor,-1) t_kor from students
order by t_kor;

-- 각 점수대의 인원 알고 싶어
select trunc(kor,-1) t_kor, count(trunc(kor, -1)) count from students
group by trunc(kor, -1)
order by t_kor;

select trunc(hire_date,'month') m_hire_date, count(trunc(hire_date, 'month')) from employees
group by trunc(hire_date, 'month')
order by m_hire_date
;

-- drop table stu_score;
-- drop table emp01;
-- drop table board;

select * from stu_score
order by no;

update stu_score set name='관순스'
where no=10;

update stu_score set avg=round(total/3,3);
select * from stu_score;

-- months_between(날짜1, 날짜2) : 2개의 날짜에서 월 간격을 확인 [암기]
select hire_date, months_between(sysdate, hire_date) from employees;
select hire_date, floor(months_between(sysdate, hire_date)), trunc(sysdate-hire_date,2) from employees;

-- add_months(날짜, 추가할 개월 숫자) : 개월 추가
select hire_date, add_months(hire_date, 6) from employees;

-- last_day(날짜) : 해당 월의 마지막 날짜
select hire_date, last_day(hire_date), round(hire_date, 'd') from employees;

-- round(날짜, 'd') : 요일을 기준으로 반올림해서 이전이면 일요일, 이후면 토요일로(한주의 제일 왼쪽(일), 제일 오른쪽(토))
select sysdate, round(sysdate, 'd') from employees;

select sysdate, trunc(sysdate, 'month') from employees;

-- 날짜 기준으로 현재일, 처음일, 마지막일 [암기]
select sysdate 현재일, trunc(sysdate, 'month') 월의첫일 , last_day(sysdate) 월의마지막일 from dual;

-- 특정 요일의 날짜를 확인 
select sysdate, next_day(sysdate, '토요일') from dual;

-- tuncs(날짜, 'd') : 요일의 처음일(날짜) 
select sysdate, trunc(sysdate, 'd') from dual;

-- next_day(날자, '요일') : 다음 해당 요일의 날짜
select sysdate, next_day(sysdate, '수요일') from dual;



-- board 테이블 default는 입력 없을 시지정한 데이터가 자동 입력됨.
create table board(
bno number(4) primary key, -- 중복이 안됨, null 값 허용하지 않음. 기본키로 사용됨.
id varchar2(30),
btitle varchar2(1000),
bcontent clob, -- varchar2는 3000자까지 작성 가능, clob은 무제한 작성 가능, 형태는 varchar2 타입과 동일
bdate date default sysdate,
bhit number default 0,
bgroup number,
bstep number default 0,
bindent number default 0,
bfile varchar2(100)
);

insert into board values(
board_seq.nextval, 'aaa', '제목입니다.', '내용입니다.', sysdate,0,board_seq.currval, 0, 0, '1.jpg'
);

insert into board (bno, id, btitle, bcontent, bgroup, bfile)
values(board_seq.nextval, 'bbb', '이벤트 신청', '이벤트를 신청합니다.', board_seq.currval, '2.jpg'
);

select * from board;


-- [형변환]
-- 오라클에는 다음의 3가지 타입이 있음 :  number, character, date 

select sysdate from dual;
select sysdate, to_char(sysdate, 'yyyy-mm-dd hh:mi:ss')  from dual;
-- 모양도 변환 가능
select to_char(sysdate, 'yy/mm/dd') from dual;
select to_char(sysdate, 'yyyy') from dual;

-- kor20240001
select 'ko'||to_char(sysdate,'yyyy')||trim(to_char(m_no.nextval,'0000')) from dual;
-- dy: 요일을 뺀 요일 예) 수, 목, ...  
-- day: 요일 포함 예) 수요일, 목요일
select to_char(sysdate, 'dy'), to_char(sysdate, 'day') from dual;
-- mon: month
select to_char(sysdate, 'yyyy-mm-dd hh:mi:ss mon day') from dual;

-- [해보기] hire_date, yyyy-mm-dd hh:mi:ss mon day
select to_char(hire_date, 'yyyy-mm-dd hh:mi:ss mon day') from employees;

-- am : 오전 표시, pm : 오후 표시
select to_char(sysdate, ' am hh:mi:ss') from dual;
select to_char(sysdate, ' pm hh:mi:ss') from dual;
-- hh24 : 24시간으로 표시 ==> sysdate로 am/pm 있어도 현재시간 기준으로 오전/오후 표시
select to_char(sysdate, ' am hh24:mi:ss') from dual;
select to_char(sysdate, ' pm hh24:mi:ss') from dual;

select * from stu_score;
select to_char(c_date, 'yyyy-mm-dd hh:mi:ss day') from stu_score
order by c_date;

-- 날짜별로 몇개의 데이터가 들어가 있는지 출력하시오.
select c_date, count(c_date) from stu_score
group by c_date
order by c_date
;


-- 문자형은 사칙연산(+, -, *, /) 안됨. 자리수(쉼표) 표시 가능, 날짜형태 표시
-- 숫자형은 사칙연산 가능(컬럼별 사칙연산 가능). 자리수(쉼표) 표시 불가, 0001로 출력 불가
-- 날짜형은 +, - 연산 가능 months_between 2개 날짜 달 수 계산, 날짜유형을 지정해서 출력 불가

-- 문자형이라도 안에 있는 데이터가 숫자이면 자동으로 형변환하여 계산
select 10 a, 100 b, 10+100 ab, to_char(100), 10+to_char(300) from dual;
select 10 a, 100 b, 10+100 ab, to_char(100), 10+'100' from dual;
-- 문자형 안에 문자가 있으면 자동형변환 불가능
select 10 a, 100 b, 10+100 ab, to_char(100), 10+'100원' from dual;

-- '0000' 빈자리를 0으로 채움. '9999' 빈자리를 빈자리로둠.
select 12340000, to_char(12340000), length(to_char(12340000,'999,999,999')) from dual;
select length(12340000), to_char(12340000), length(to_char(12340000,'999,999,999')), 
to_char(12340000,'000,999,999') from dual;

-- L : 원화 표시
select 12340000, to_char(12340000, 'L000,999,999') from dual;
-- $ : 달러 표시
select 12340000, to_char(12340000, '$000,999,999') from dual;
-- 소수점 자리 표시
select 1234.1234, to_char(1234.1234,'000,999.99') from dual;
-- 10개 자리수 표시 
select length(trim(to_char(12345, '0000000000'))), length(trim(to_char(12345,'999,999'))) from dual;
select trim(to_char(12345, '0000000000')), trim(to_char(12345,'999,999')) from dual;

-- length : 데이터의 길이 함수
select length('안녕하세요') from dual;
select length(1234000) from dual;

-- [퀴즈] 123,456,789 + 100,000 의 값 출력(천 단위 표시)
select 123456789+100000 from dual;
-- 123,456,789 쉼표 제거 ==> replace('123,456,789',',',"")
-- 타입 number로 형변환
-- 더하기
-- 문형 타입으로 형변환 후 쉼표 표시
select (123,456,789)+(100,000) from dual;
select replace('123,456,789',',','') from dual;
-- 내 코드
select to_char(replace('123,456,789',',','')+replace('100,000',',',''),'L999,999,999') sum from dual;
-- 선생님 코드
select to_char(to_number(replace('123,456,789',',',''))+to_number(replace('100,000',',','')),'L999,999,999') sum from dual;

-- 아래와 같이 해도 나오지만, 보통의 데이터는 아래와 같이 넘어와.
-- total = '123,456,789'
-- wire = '100,000'
select to_char(123456789+100000,'L999,999,999') from dual;

select to_number('0000123') from dual;

-- 날짜형 사칙연산
-- 아래와 같이 문자형은 사칙연산(+,-) 안돼. ==> 형변환 필요
select '2024-04-24'-'2024-04-01' from dual;
-- 날짜형 형변환 : -, / 모두 사용 및 생략 가능, 년도 20생략도 가능
select to_date('2024-04-24')-to_date('2024/04/01') from dual;
select to_date('2024-04-24')-to_date('24/04/01') from dual;
select to_date('20240424')-to_date('240401') from dual;

-- [퀴즈] '20240401'을 2024-04-01 타입으로 변경해서 출력
select to_date('20240401') from dual;
select to_char(to_date('20240401'),'yyyy-mm-dd hh:mi:ss') from dual;

-- 날짜를 작성한 것은 문자형으로 찾는 것은 되지만, 사칙연산은 안됨 즉, 날짜형으로 변환 필요
select hire_date from employees
where hire_date >= '20080101';

select * from stu_score;

select c_date from stu_score
where c_date = '2024/04/05'
;

select sysdate-hire_date from employees;
-- 날짜를 작성한 것은 문자형으로 빼기 위해서는 날짜형으로 변환 필요
select sysdate-to_date('2024/04/01') from dual;

-- [퀴즈] 
-- 20,000 / 10,000 문자형을 빼기 연산을 해서 10,000을 출력하시오.(replace 미사용)
select to_char(to_number('20,000','99,999')-to_number('10,000','99,999'),'999,999') from dual;

-- [퀴즈] 
select commission_pct from employees;
-- 실제 월급 = 월급 + (월급 * 커미션) 출력하시오.
-- nvl(데이터, 0) : null 값을 0으로 처리
select * from employees;
select (salary + (salary*nvl(commission_pct,0))) real_salary from employees;

-- commission_pct null값만 출력하시오.
-- is null
select commission_pct from employees
where commission_pct is null
;

-- null값은 내림차순 시 제일 위에, 오름차순 시 제일 아래 위치
select manager_id from employees
order by manager_id desc;

-- [퀴즈] manager_id가 null이면 0으로 입력 ==> nvl(데이터, 0)
select nvl(manager_id,0) from employees
order by manager_id desc
;

-- [퀴즈] manager_id가 null이면 ceo로 입력
-- manager_id 타입은 number이기 때문에 아래와 같이 'ceo'(문자형)를 대입하면 error 발생 ==> 형변환
select nvl(manager_id,'ceo') from employees
order by manager_id desc
;

select nvl(to_char(manager_id),'ceo') from employees
order by manager_id desc
;