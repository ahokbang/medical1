select * from employees;

-- ȸ������ ���̺� ����
create table member( -- member�� ���̺� �̸�
id varchar2(20), -- id�� �÷� �̸�, varchar2�� ������, 20�� �ڸ���(���� ���� 1�ڸ�(����Ʈ)==> ���� aaa�� 3�ڸ� ����, �ѱ��� ��� 3�ڸ�==> �ѱ��� 6�� �ۼ� ����, ���� �̼����� 9�ڸ��� ����)�� 20�ڸ��� ����ϰڴٴ� �ǹ�
pw varchar2(20),
name varchar2(20),
phone varchar2(20)
);

-- ������ �Է�
insert into member(id, pw, name, phone) values(
'aaa', '1111', 'ȫ�浿', '010-1111-1111'
-- ����(varchar2)�� '' �ȿ� �Է�
);

insert into member values(  -- table�� �ִ� ��� ���� ���� �Է��� ��� ��������
'bbb', '1111', '������', '010-2222-2222'
);

insert into member (id, name, phone) values( -- �ش� ���� �Է��� ��쿡�� �ش� �� �ۼ� �ʿ�
'ccc', '�̼���', '010-3333-3333'
);

-- �÷� �� ���� ����, ���� �߻�: ���� ���� ���� ��ġ���� ����. 
/*
insert into member values(
'ddd', '������', '010-4444-4444'
);

���� �߻� �����: 25 ��: 13
���� ���� -
SQL ����: ORA-00947: ���� ���� ������� �ʽ��ϴ�
00947. 00000 -  "not enough values"
*Cause:    
*Action:

*/

select id, pw, name, phone from member;
-- ID ccc�� ��� pw �� �Է����� �ʾƼ� null�� ���
-- null : ���� ���� ���� �ƴ� "���Ѵ�"�� �ǹ�, null�� *, -, +, /(��Ģ����)�ϸ� ���� null�� ��.


-- �� �����ʹ� �ӽ�����ҿ� �־�. rollback�ϸ� data �����, commit�ϸ� �����.
commit;

-- commit�� �ϸ� rollback�ص� �����ʹ� �������� �ʾ�.
rollback;
select * from member; -- *�� ��� ������(�÷�)�� �ǹ�
select id from member; -- id�� ������
select id, name from member; -- id, name ������

insert into member values(
'ddd', '1111', '������', '010-4444-4444'
);

select * from member;

rollback; -- commit�� ���ķ� ���ư�. commit �������� ���ư��� �ʾ�.
select * from member;

commit;

select * from member;

update member set pw='2222'; -- ��� pw���� 2222�� �����
select * from member;
rollback;

-- where��� �������� �Է����־�� ��.
update member set pw='2222' where id='ccc'; -- ==> id�� ccc�� ������ pw�� 2222�� �ٲ���.

-- ���� ���� ��� ���̺� Ȯ�� ����
select * from tab; 

-- ���̺��� Ÿ�� Ȯ��
desc member;

/*
����Ŭ Ÿ��
- number: ����
- date: ��¥
- char: ��������
- vhrchar2: ��������
- clob: ��뷮����
*/

-- number: ������ �Ǽ��� ����.
-- number(4): 4�ڸ� ���ڷ� -9999~9999 ǥ�� ����

create table mem(
no number, -- ������(��) ���� �� ����. ���Ѵ�(������ �� �� ��). �׷����� �������̱����� ��.
no2 number(4),
no3 number(4,2) -- �� 4�ڸ��� ����Ұǵ� 2�ڸ��� ������ �Ҽ��� �ڸ��� �� 00.00 �̷��� ��µ�.
);

insert into mem (no) values(1234567890);
insert into mem (no2) values(9999);
insert into mem (no2) values(1.11); -- ���� 1�� ���. �����κи� �����Ƿ� 1�� ���. -9999~9999 ����ϹǷ� 1�� ��� ����
insert into mem (no2) values(1.6); -- �ݿø��Ͽ� 2�� ���
-- insert into mem (no2) values(99991); -- no2�� number(4)�̹Ƿ� 5�ڸ� ���ڸ� �Է��ϸ� error �߻�
insert into mem (no2) values(-9999);
-- insert into mem (no2) values(-99991); -- no2�� number(4)�̹Ƿ� 5�ڸ� ���ڸ� �Է��ϸ� error �߻�
-- ũ�⸦ �������� �� �˻� �� �������� ũ�⸦ �ѹ� �� ���� �ʰ� �����͸� �о� ó�� �ð��� ũ�⸦ �������� �ʾ��� �� ���� �� ������.
insert into mem (no3) values(11.11);
insert into mem (no3) values(111); -- 111.00�� �ǹǷ� 5�ڸ��� �Ǿ� error �߻�

select * from mem;

commit;

create table mem2 (
no number(4,2),
mdate date, -- date: ��, ��, ��, ��, ��, �ʱ��� ���� ����
mdate2 timestamp -- date = timestamp ��, timestamp�� �и��ʱ��� ���� ����
);

insert into mem2 (mdate) values('2024-04-19'); -- date�� ���������� �Է��ص� ��¥�� �ν�
insert into mem2 (mdate) values(sysdate); -- ����ð�
insert into mem2 (mdate2) values(sysdate);

select * from mem2; -- 2024-04-19�� �Է��ص� 24/04/29�� ���(�⺻��), ��/��/�� �����Ǿ� ����. �ð��� ������ ������ ���� �ҷ������־�.
select to_char(mdate, 'yyyy-mm-dd hh:mi:ss') from mem2;
select to_char(mdate, 'yyyy/mm/dd hh:mi:ss.ff') from mem2; -- error, date���� �и������� �����Ƿ� �������� ����.
select to_char(mdate2, 'yyyy/mm/dd hh:mi:ss:ff') from mem2;

-- '2024-04-19' �̷��� varchar2�� �޾Ƶ� ������, date�� ���ϱ� ���Ⱑ ��.
-- ���� ��¥���� 2�� ��
select mdate+2 from mem2;
-- ���� ��¥�� 30�� �� ==> ������ create �� �͸� ����ǹǷ� mdate+30�� �׳� [���� ���]���� �����ִ� ��. 
-- mdate+30�� �߰��ϰ� ������ 
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

-- ������ ���� ���: char, varchar2
--char : ��������
insert into mem3 (tel) values('11112222');
insert into mem3 (tel) values('22223333');
insert into mem3 (tel) values('111');
insert into mem3 (tel) values('123456789'); -- error
insert into mem3 (tel) values('ȫ');

-- varchar2: ��������
insert into mem3 (name) values('11112222');
insert into mem3 (name) values('ȫ�浿'); -- �ѱ�(�� ����): 3ũ��
insert into mem3 (name) values('�Ż��Ӵ�'); -- 12�ڸ� �ʿ�
INSERT INTO MEM3 (NAME) VALUES('AAA');  
insert into mem3 (name) values('aaa'); 

commit;

select * from mem, mem2;
select * from mem3 where name='aaa'; -- sql ������ ��ҹ��� ���� ����. �����ʹ� ��ҹ��� ������.
select * from mem3 where name='AAA';
select * from mem3 where lower(name)='aaa';

-- select, from 2���� Ű����� ������
-- ��� �÷� ����� ��: select * from (���̺� ��);
-- ��ҹ��ڸ� �������� ����. data(��)�� ����

select * from mem;
SELECT * FROM MEM;

select emp_name, department_id from employees;

-- distinct: ���� ���� 1���� ���(�ߺ� ����)
select distinct department_id from employees;

select * from departments;
select department_id, department_name from departments;

select * from employees;
select employee_id, emp_name, salary from employees;
-- ���� ���� ���� ������� ������ ���� table�� �ٸ� �����ۼ��� ������ ���
select employee_id, job_id, emp_name, salary from employees;

select * from jobs;

select * from products;

select * from mem3;
-- �÷��� ��ġ�� �ٲٰ� ������ �ٲ㼭 ������ ��.
select no, mdate2, tel, name, mdate from mem3; 
select * from employees;

-- �����ȣ(employee_id), ����̸�(employee_name), �޿�(salary), �Ի�����(hire_date) ���
select employee_id, emp_name, salary, hire_date from employees;

desc employees;

-- ���̺� ����
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
1, 'ȫ�浿',100,100,100,300,100,1
);

insert into stu_score values(2, '�̼���',100,100,100,300,100,1);

insert into stu_score values(
3, '������',100,100,100,300,100,1
);

insert into stu_score values(
4, '������',100,100,100,300,100,1
);

insert into stu_score values(
5, '�豸',100,100,100,300,100,1
);

commit;

select * from stu_score;


-- ��������� number Ÿ���� ��쿡�� ����
select * from stu_score;

insert into stu_score values(
6, '������', 100, 95, 96, (100+95+96),((100+95+96)/3),1
);

insert into stu_score values(
7, 'ȫ����', 100, 100, 99, (100+100+99), (100+100+99)/3, 1
);

select * from stu_score;

-- ��ȣ, �̸�, ��������, ��������-20, ���, ��������-20�� �� ���
select no, name, kor, kor-20,avg,(kor-20+eng+math)/3 from stu_score;



select * from employees;

-- �޷�, ��ȭ ȯ�� - 1381.79
select employee_id, emp_name, salary from employees;

select employee_id, emp_name, salary, salary*1381.79 from employees;

-- ���� * 12 = ����
-- �޷�����, ��ȭ������ ���Ͻÿ�.
select employee_id, emp_name, salary*12, salary*1381.78*12 from employees;

-- Ŀ�̼��� ����*Ŀ�̼�, ���� �������� ����+(����*Ŀ�̼�)
-- commission_pct
select employee_id, emp_name, salary+(salary*commission_pct) from employees;
-- null�� ��쿡�� ? �Ǵ� ���Ѵ븦 �ǹ��ϹǷ� ������ ���� �������־�� ��.
-- nvl(�÷�, 0) ==> �÷��� null���� 0���� �������־�� �Ѵٴ� �ǹ�
select employee_id, emp_name, nvl(commission_pct,0),salary+(salary*nvl(commission_pct,0)) from employees;

select * from employees;




