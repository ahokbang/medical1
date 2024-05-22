-- [��¥�Լ�]
-- trunc : ����
select sysdate, hire_date, trunc(sysdate-hire_date, 3) from employees; -- ���� �ڸ������� ����
-- round : �ݿø�
select sysdate, hire_date, round(sysdate-hire_date, 3) from employees; -- �ݿø�

-- ���� ��¥ : sysdate-1
-- ���� ��¥ : sysdate+1
select sysdate-1 ����, sysdate ����, sysdate+1 ����, sysdate+100 from dual;

-- ����) m_no(������) : 1 - 9999 1�� ����, 5�� �ݺ��ؼ� ����
-- column : m_yesterday, m_today, m_tomorrow, m_year ��¥�÷��� ���� ���̺� m_date
-- ����, ����, ����, 1���� ��¥�� �����Ͻÿ�.
-- ��¥: date�� timestamp ��� ���� timestamp�� �и��ʱ��� ��� ����
-- ������ ����
create sequence m_no
increment by 1
start with 1
minvalue 1
maxvalue 9999
cycle
nocache
;
-- ���̺�����
create table m_date(
m_no number(1) primary key,
m_yesterday date,
m_today date,
m_tommorow date,
m_year date
);
-- 1�� row ����
insert into m_date values(
m_no.nextval, sysdate-1, sysdate, sysdate+1, sysdate+365
);
-- �˻�
select * from m_date;

-- ȸ������ 1�⵿�� �α��� ������, �������� ȸ������ ����

-- abs :���밪
select hire_date-sysdate from employees; -- ���� ��� --> abs�� ���밪 ������ ����� ��ȯ
select abs(hire_date-sysdate) from employees; 
-- ceil(�ø�), floor(����), round(�ݿø�, �ڸ���), tunc(����, �ڸ���)
-- ��¥�� ���� �������� �ݿø�
select hire_date, round(hire_date,'month') from employees;
-- ��¥�� ���� ������ ����
select hire_date, trunc(hire_date,'month'), round(hire_date,'month') from employees;

select trunc(hire_date,'month') ������, hire_date from employees
order by hire_date;

select * from channels;

select * from kor_loan_status
order by period;

-- period 201111�� �󸶳� �������� �׷��� ==> ���� Ȯ�� ===> count(�ش� ��)
select period, count(period) from kor_loan_status
group by period 
order by period;

select period from kor_loan_status
where period = '201111' ;



select * from students;
-- student table���� �������� ����
select trunc(kor,-1) t_kor from students
order by t_kor;

-- �� �������� �ο� �˰� �;�
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

update stu_score set name='������'
where no=10;

update stu_score set avg=round(total/3,3);
select * from stu_score;

-- months_between(��¥1, ��¥2) : 2���� ��¥���� �� ������ Ȯ�� [�ϱ�]
select hire_date, months_between(sysdate, hire_date) from employees;
select hire_date, floor(months_between(sysdate, hire_date)), trunc(sysdate-hire_date,2) from employees;

-- add_months(��¥, �߰��� ���� ����) : ���� �߰�
select hire_date, add_months(hire_date, 6) from employees;

-- last_day(��¥) : �ش� ���� ������ ��¥
select hire_date, last_day(hire_date), round(hire_date, 'd') from employees;

-- round(��¥, 'd') : ������ �������� �ݿø��ؼ� �����̸� �Ͽ���, ���ĸ� ����Ϸ�(������ ���� ����(��), ���� ������(��))
select sysdate, round(sysdate, 'd') from employees;

select sysdate, trunc(sysdate, 'month') from employees;

-- ��¥ �������� ������, ó����, �������� [�ϱ�]
select sysdate ������, trunc(sysdate, 'month') ����ù�� , last_day(sysdate) ���Ǹ������� from dual;

-- Ư�� ������ ��¥�� Ȯ�� 
select sysdate, next_day(sysdate, '�����') from dual;

-- tuncs(��¥, 'd') : ������ ó����(��¥) 
select sysdate, trunc(sysdate, 'd') from dual;

-- next_day(����, '����') : ���� �ش� ������ ��¥
select sysdate, next_day(sysdate, '������') from dual;



-- board ���̺� default�� �Է� ���� �������� �����Ͱ� �ڵ� �Էµ�.
create table board(
bno number(4) primary key, -- �ߺ��� �ȵ�, null �� ������� ����. �⺻Ű�� ����.
id varchar2(30),
btitle varchar2(1000),
bcontent clob, -- varchar2�� 3000�ڱ��� �ۼ� ����, clob�� ������ �ۼ� ����, ���´� varchar2 Ÿ�԰� ����
bdate date default sysdate,
bhit number default 0,
bgroup number,
bstep number default 0,
bindent number default 0,
bfile varchar2(100)
);

insert into board values(
board_seq.nextval, 'aaa', '�����Դϴ�.', '�����Դϴ�.', sysdate,0,board_seq.currval, 0, 0, '1.jpg'
);

insert into board (bno, id, btitle, bcontent, bgroup, bfile)
values(board_seq.nextval, 'bbb', '�̺�Ʈ ��û', '�̺�Ʈ�� ��û�մϴ�.', board_seq.currval, '2.jpg'
);

select * from board;


-- [����ȯ]
-- ����Ŭ���� ������ 3���� Ÿ���� ���� :  number, character, date 

select sysdate from dual;
select sysdate, to_char(sysdate, 'yyyy-mm-dd hh:mi:ss')  from dual;
-- ��絵 ��ȯ ����
select to_char(sysdate, 'yy/mm/dd') from dual;
select to_char(sysdate, 'yyyy') from dual;

-- kor20240001
select 'ko'||to_char(sysdate,'yyyy')||trim(to_char(m_no.nextval,'0000')) from dual;
-- dy: ������ �� ���� ��) ��, ��, ...  
-- day: ���� ���� ��) ������, �����
select to_char(sysdate, 'dy'), to_char(sysdate, 'day') from dual;
-- mon: month
select to_char(sysdate, 'yyyy-mm-dd hh:mi:ss mon day') from dual;

-- [�غ���] hire_date, yyyy-mm-dd hh:mi:ss mon day
select to_char(hire_date, 'yyyy-mm-dd hh:mi:ss mon day') from employees;

-- am : ���� ǥ��, pm : ���� ǥ��
select to_char(sysdate, ' am hh:mi:ss') from dual;
select to_char(sysdate, ' pm hh:mi:ss') from dual;
-- hh24 : 24�ð����� ǥ�� ==> sysdate�� am/pm �־ ����ð� �������� ����/���� ǥ��
select to_char(sysdate, ' am hh24:mi:ss') from dual;
select to_char(sysdate, ' pm hh24:mi:ss') from dual;

select * from stu_score;
select to_char(c_date, 'yyyy-mm-dd hh:mi:ss day') from stu_score
order by c_date;

-- ��¥���� ��� �����Ͱ� �� �ִ��� ����Ͻÿ�.
select c_date, count(c_date) from stu_score
group by c_date
order by c_date
;


-- �������� ��Ģ����(+, -, *, /) �ȵ�. �ڸ���(��ǥ) ǥ�� ����, ��¥���� ǥ��
-- �������� ��Ģ���� ����(�÷��� ��Ģ���� ����). �ڸ���(��ǥ) ǥ�� �Ұ�, 0001�� ��� �Ұ�
-- ��¥���� +, - ���� ���� months_between 2�� ��¥ �� �� ���, ��¥������ �����ؼ� ��� �Ұ�

-- �������̶� �ȿ� �ִ� �����Ͱ� �����̸� �ڵ����� ����ȯ�Ͽ� ���
select 10 a, 100 b, 10+100 ab, to_char(100), 10+to_char(300) from dual;
select 10 a, 100 b, 10+100 ab, to_char(100), 10+'100' from dual;
-- ������ �ȿ� ���ڰ� ������ �ڵ�����ȯ �Ұ���
select 10 a, 100 b, 10+100 ab, to_char(100), 10+'100��' from dual;

-- '0000' ���ڸ��� 0���� ä��. '9999' ���ڸ��� ���ڸ��ε�.
select 12340000, to_char(12340000), length(to_char(12340000,'999,999,999')) from dual;
select length(12340000), to_char(12340000), length(to_char(12340000,'999,999,999')), 
to_char(12340000,'000,999,999') from dual;

-- L : ��ȭ ǥ��
select 12340000, to_char(12340000, 'L000,999,999') from dual;
-- $ : �޷� ǥ��
select 12340000, to_char(12340000, '$000,999,999') from dual;
-- �Ҽ��� �ڸ� ǥ��
select 1234.1234, to_char(1234.1234,'000,999.99') from dual;
-- 10�� �ڸ��� ǥ�� 
select length(trim(to_char(12345, '0000000000'))), length(trim(to_char(12345,'999,999'))) from dual;
select trim(to_char(12345, '0000000000')), trim(to_char(12345,'999,999')) from dual;

-- length : �������� ���� �Լ�
select length('�ȳ��ϼ���') from dual;
select length(1234000) from dual;

-- [����] 123,456,789 + 100,000 �� �� ���(õ ���� ǥ��)
select 123456789+100000 from dual;
-- 123,456,789 ��ǥ ���� ==> replace('123,456,789',',',"")
-- Ÿ�� number�� ����ȯ
-- ���ϱ�
-- ���� Ÿ������ ����ȯ �� ��ǥ ǥ��
select (123,456,789)+(100,000) from dual;
select replace('123,456,789',',','') from dual;
-- �� �ڵ�
select to_char(replace('123,456,789',',','')+replace('100,000',',',''),'L999,999,999') sum from dual;
-- ������ �ڵ�
select to_char(to_number(replace('123,456,789',',',''))+to_number(replace('100,000',',','')),'L999,999,999') sum from dual;

-- �Ʒ��� ���� �ص� ��������, ������ �����ʹ� �Ʒ��� ���� �Ѿ��.
-- total = '123,456,789'
-- wire = '100,000'
select to_char(123456789+100000,'L999,999,999') from dual;

select to_number('0000123') from dual;

-- ��¥�� ��Ģ����
-- �Ʒ��� ���� �������� ��Ģ����(+,-) �ȵ�. ==> ����ȯ �ʿ�
select '2024-04-24'-'2024-04-01' from dual;
-- ��¥�� ����ȯ : -, / ��� ��� �� ���� ����, �⵵ 20������ ����
select to_date('2024-04-24')-to_date('2024/04/01') from dual;
select to_date('2024-04-24')-to_date('24/04/01') from dual;
select to_date('20240424')-to_date('240401') from dual;

-- [����] '20240401'�� 2024-04-01 Ÿ������ �����ؼ� ���
select to_date('20240401') from dual;
select to_char(to_date('20240401'),'yyyy-mm-dd hh:mi:ss') from dual;

-- ��¥�� �ۼ��� ���� ���������� ã�� ���� ������, ��Ģ������ �ȵ� ��, ��¥������ ��ȯ �ʿ�
select hire_date from employees
where hire_date >= '20080101';

select * from stu_score;

select c_date from stu_score
where c_date = '2024/04/05'
;

select sysdate-hire_date from employees;
-- ��¥�� �ۼ��� ���� ���������� ���� ���ؼ��� ��¥������ ��ȯ �ʿ�
select sysdate-to_date('2024/04/01') from dual;

-- [����] 
-- 20,000 / 10,000 �������� ���� ������ �ؼ� 10,000�� ����Ͻÿ�.(replace �̻��)
select to_char(to_number('20,000','99,999')-to_number('10,000','99,999'),'999,999') from dual;

-- [����] 
select commission_pct from employees;
-- ���� ���� = ���� + (���� * Ŀ�̼�) ����Ͻÿ�.
-- nvl(������, 0) : null ���� 0���� ó��
select * from employees;
select (salary + (salary*nvl(commission_pct,0))) real_salary from employees;

-- commission_pct null���� ����Ͻÿ�.
-- is null
select commission_pct from employees
where commission_pct is null
;

-- null���� �������� �� ���� ����, �������� �� ���� �Ʒ� ��ġ
select manager_id from employees
order by manager_id desc;

-- [����] manager_id�� null�̸� 0���� �Է� ==> nvl(������, 0)
select nvl(manager_id,0) from employees
order by manager_id desc
;

-- [����] manager_id�� null�̸� ceo�� �Է�
-- manager_id Ÿ���� number�̱� ������ �Ʒ��� ���� 'ceo'(������)�� �����ϸ� error �߻� ==> ����ȯ
select nvl(manager_id,'ceo') from employees
order by manager_id desc
;

select nvl(to_char(manager_id),'ceo') from employees
order by manager_id desc
;