--  가지고 있는 테이블 검색
select * from tab;
-- F5: 콘솔모양(코드 전체실행) ==> 세미콜론이 있는데 까지 열어줘, 드래그하고(하나의 행 선택) F5 누르면 그 행만 실행 F9처럼
-- F9: 격자형(부분실행, 해당 코드(커서가 있는 행))   ==> F9 사용해

select * from employees;

-- 테이블 구조 확인
desc employees;

-- 테이블 생성
create table stu_score(
    no number(2), 
    kor number(3),
    eng number(3),
    avg number(5,2) 
    -- 3자리의 정수, 2자리 소수점이므로 앞(전체 자리수)은 5, 뒤(소수점자리)는 2
);

-- 테이블에 데이터 삽입
insert into stu_score(no, kor, eng, avg) values(
1, 100, 99, (100+99)/2
);
-- 아래와 같이 축약해서 사용 가능
insert into stu_score values(
1, 95, 98, (95+98)/2
);

insert into stu_score values(
    1,80,70.223,(80+70.223)/2
);

select * from stu_score;

-- commint 해야 반영
commit;

create table num(
no number,
name varchar2(10),
kor number,
eng number,
avg number(4,1)
);
-- number에 숫자를 지정하지 않으면 30개 정도를 알아서 지정


-- 현재 날짜, 기본 형태: 24/01/01
-- dual 가상테이블
select sysdate from dual;

-- 날짜 포맷 변경(yyyy/mm/dd -> yyyy-mm-dd), to_chart : 형변환 => 포맷 지정
select to_char(sysdate, 'yyyy-mm-dd') from dual;
-- 년/월/일/시 출력
select to_char(sysdate, 'yyyy-mm-dd hh:mi:ss') from dual;
-- 시간만 출력
select to_char(sysdate, 'hh:mi:ss') from dual;

-- 오늘+100일 후의 날짜를 알려줌
select sysdate+100 from dual;
-- 오늘+1000일의 후의 날짜
select sysdate+1000 from dual;
-- 현재 날짜가 24년 1월 1일 이후에 며칠이 지났는지?
select sysdate - to_date('24/01/01') from dual;