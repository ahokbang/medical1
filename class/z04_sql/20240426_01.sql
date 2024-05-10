-- [9�� alter table]
-- table ����
-- ���̺� ����
create table emp01(
emp_id number(6),
emp_name varchar2(80),
hire_date date
);

-- (���̺� ����)table ���� : ���� ���̺� ���� �� ������ ��� ����
desc employees;

create table emp02 as
select * from employees;

select * from emp02;
select * from employees;

-- ���̺� ������ �����ϱ�
create table emp03 as 
select * from employees where 1=2;
select * from emp03; 

select * from emp01; -- �÷� 3��
select * from employees; -- �÷� 14��
-- ���̺� ������ �ٸ��鼭 �����͸� �����ϱ�(�ȿ� �ִ� ������ 3�� -> 14��)
insert into emp01(emp_id, emp_name, hire_date)
select employee_id, emp_name, hire_date from employees;

select * from emp01 order by emp_id desc;

-- ������ 1�� �߰�
insert into emp01 values(
 207, 'ȫ�浿','2024-04-26'
);

select * from emp01 order by emp_id desc;

-- ���̺� ������ �����鼭 �����͸� ����
insert into emp03
select * from employees;

select * from emp03;

-- drop table s_info;
-- drop table m_date;

desc member;

-- �÷� Ÿ�� ����
alter table member
modify(stu_name varchar2(30));

-- �÷� ����
alter table member
drop column pw;

desc member;

-- �÷� �߰�(�� ������)
alter table member
add (pw varchar2(30)); 

desc member;

select * from member;

-- ���� �÷� ������ �Ʒ��� ����.
select mno, id, pw, stu_name, gender from member; -- ==> �������⸸ �ϰ� ������ �Է��� pw ���� ��������.
select * from member;
insert into member values(
m_no.nextval, 'fff', '������','male', '1111'
);
select * from member;
insert into member values(
m_no.nextval, 'ggg', '1111', 'ȫ����','male'
); -- ==> error 

-- �÷� ���� ���� : �÷��� �Ⱥ��̰� ���� �� �ٽ� ���̰� �ϱ�
-- ����, stu_name, gender �� �Ⱥ��̰� ����, �÷� �����
alter table member modify stu_name invisible;
select * from member;
alter table member modify gender invisible;
select * from member;
-- ���� ���� �ٽ� ��Ÿ���� �ϸ�(�÷� �����ֱ�) ���� ������ ���� �پ�
alter table member modify stu_name visible;
select * from member;
alter table member modify gender visible;
select * from member;

-- �÷��� �Ͻ��� ��� ����
alter table member
set unused(id);
select * from member; -- > id �� ����

-- ��� ���ѵ� �÷����� ��� ���� ����
alter table member
drop unused columns;
select * from member; 

-- ���̺� ����
-- drop table emp03;

-- ���̺� �̸� ����
rename emp01 to employees01;

-- [9�� ����] 

-- [10�� ���Ἲ ���� ����]
-- ���Ἲ�������� : ���Ἲ�̶�, ������ ����� �Ѵٴ� �ǹ̷�, ����Ŭ�� �����ʹ� ���Ἲ �����̾�� ��. ==> �����Ͱ� �� ���������� ��ž�.
-- ���Ἲ���������̶� ���̺� �������� �ڷᰡ �ԷµǴ� ���� �����ϱ� ���� ���̺��� ������ �� �� �÷��� ���ؼ� �����ϴ� ���� ���� ��Ģ
-- ���Ἲ��������: not null(null �����), unique(�ߺ��� �����, �׻� ������ ���� ������ ��, null�� ���), 
--               primary key(����Ű, null �����, �ߺ��� �� �����, not null ���ǰ� unique ���� ���� ����)
--               foreign key(�����Ǵ� ���̺��� Į���� ���� �����ϸ� ���), check(���� ������ ������ ���� ������ ������ �����Ͽ� ������ ������ ���)

desc employees;    

-- [ ���Ἲ �������� ]
-- foreign key�� �ٸ� ���̺��� ������ �Է� �� ����Ǿ� �ִ� ���� ���̺� �Է��Ϸ��� �����Ͱ� �ִ��� Ȯ�� ==> ������ ��������ְ� ������ ������� ���� ����.

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
'aaaa','1111','ȫ�浿','male'
);


insert into member(id, pw, name) values(
'bbb','1111','������'
);

select * from member;

insert into member(id, pw) values(
'ccc','1111'
);
-- error
select * from member;
insert into member(id) values( 
'ddd'
); -- ==> error ORA-01400: NULL�� ("ORA_USER"."MEMBER"."PW") �ȿ� ������ �� �����ϴ�

insert into member (id,pw) values(
'ddd', '1111'
);

insert into member (id,pw) values(
'aaaa', '1111'
); -- ==> error ORA-00001: ���Ἲ ���� ����(ORA_USER.SYS_C007343)�� ����˴ϴ� => id�� ���������� �ɾ��� ������ ������ id �Է� �� ���� �߻�. null�� ����

insert into member (id,pw,name) values(
'a', '1111', 'ȫ�浿'
);
select * from member;

-- ���� ����: not null : null���� ����
create table emp02(
empno number(4) not null,
ename varchar2(10) not null,
job varchar2(9),
deptno number(2)
);

insert into emp02 values(
'5','��âȣ','����','50'
);

select * from emp02;

-- ���� ����: unique : �ߺ��� ����, null ���
create table emp03(
empno number(4) unique,
ename varchar2(10) not null,
job varchar2(9),
deptno number(2)
); 

insert into emp03 values(
'1', 'ȫ�浿','1','1'
);

insert into emp03 values(
null, 'ȫ�浿','1','1'
);
select * from emp03;

insert into emp03 values(
'3', '�̼���','2','2'
);

insert into emp03 values(
null, '������','2','2'
);

insert into emp03 values(
'1', '�豸','3','3'
); -- error ORA-00001: ���Ἲ ���� ����(ORA_USER.SYS_C007347)�� ����˴ϴ�


--[����] 1�� ȫ�浿 �˻�
select * from emp03
where empno = 1;

-- [����] null ȫ�浿 �˻�
select * from emp03
where empno is null and ename = 'ȫ�浿';

-- [����] null�� ��� ��� �˻�
select * from emp03
where empno is null;

-- null�� �ƴ� ��� �˻� �ÿ��� 
select * from emp03
where empno is not null;

create table emp01(
empno number(4) primary key,
ename varchar2(10) not null,
job varchar2(9) ,
deptno number(2)
);

-- 5�� null, 1, 2, 3, 1
insert into emp01 values(
'1','ȫ�浿','���','1'
);

insert into emp01 values(
'1','������','�븮','1'
); -- error ORA-00001: ���Ἲ ���� ����(ORA_USER.SYS_C007349)�� ����˴ϴ�

insert into emp01 values(
'2','������','�븮','1'
); 

insert into emp01 values(
null,'��ҿ�','����','1'
); -- error ORA-01400: NULL�� ("ORA_USER"."EMP01"."EMPNO") �ȿ� ������ �� �����ϴ�

insert into emp01 values(
3,'��ҿ�','����','1'
);

insert into emp01 values(
4,null,'����',2
); -- error ORA-01400: NULL�� ("ORA_USER"."EMP01"."ENAME") �ȿ� ������ �� �����ϴ�

insert into emp01 values(
4,'��ҿ�','����',2
);

select * from emp01; 

-- [����] 4�� ��ҿ� �˻�
select * from emp01
where empno = 4;

-- foreign key(�ܷ�Ű)
-- primary key�� ����Ǿ�� foreign key�� ��� ����!
-- drop table emp01;

-- emp01 ���̺� ����
create table emp01(
empno number(4) primary key,
ename varchar2(20) not null,
job varchar2(9),
deptno number(6)
);
alter table emp01
modify(deptno number(6));

insert into emp01 values(
1, 'ȫ�浿', '0001', 10
);

insert into emp01 values(
2, '������', '0002', 20
);

insert into emp01 values(
3, '�̼���', '0002', 30
);

-- deptno 10-270

insert into emp01 values(
4, '�豸', '0003', 270
);

insert into emp01 values(
5, '������', '0004', 280
); -- error ORA-02291: ���Ἲ ��������(ORA_USER.FK_DEPTNO)�� ����Ǿ����ϴ�- �θ� Ű�� �����ϴ�
-- �ܷ�Ű�� ������ �Ǹ� deptno�� ���� �����͸� �Է��ص� �����.

-- foreign key ����
alter table emp01
drop constraint fk_deptno;

insert into emp01 values(
5, '������', '0004', 280
); -- 1 �� ��(��) ���ԵǾ����ϴ�.

commit;

-- emp01�� foreign key �߰�
-- fk_deptno ��Ī
-- add constraint ��Ī foreign key(�����÷�) references �ٸ� ���̺�(�÷��̸�)
alter table emp01 
add constraint fk_deptno foreign key(deptno)
references dept01(deptno)
;

select * from dept01;

alter table emp01
modify(deptno number(6));

-- dept01 ���̺� ����
create table dept01(
deptno number(6) primary key,
dept_name varchar2(80)
);

-- select * from departments;

-- insert into dept01 (deptno, dept_name)
-- select department_id, department_name from departments;

desc departments;

-- �÷��� Ÿ�� ����
alter table dept01
modify (deptno number(6));

alter table dept01
modify (dept_name varchar2(80));
-- �÷��� ���� �߰�
insert into dept01 (deptno, dept_name)
select department_id, department_name from departments;

-- �÷� Ÿ�� ����
alter table emp01
modify (dept_name number(8));

desc member;

-- board table ����
create table board(
bno number(4) primary key,
id varchar2(30),
btitle varchar2(1000),
bcontent varchar2(3000)
);

insert into board values(
1, 'aaa', '�Խñ�1','����1'
);
insert into board values(
2, 'bbb', '�Խñ�2','����2'
);
insert into board values(
3, 'ccc', '�Խñ�3','����3'
);
insert into board values(
4, 'ddd', '�Խñ�4','����4'
);
insert into board values(
5, 'aaa', '�Խñ�5','����5'
);
insert into board values(
6, 'aaa', '�Խñ�6','����6'
);
insert into board values(
7, 'aaa', '�Խñ�7','����7'
);
insert into board values(
8, 'bbb', '�Խñ�8','����8'
);

select * from board;

alter table board
add constraint fk_id foreign key (id)
references member(id);

-- [Ȯ���ʿ�]
-- select * from member
-- where table_name = ''

-- comment table ������̺� 
-- ���̺� ����, �̸�: comment
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

-- ��۴ޱ�
insert into comments values(
1, 5, '1111', '��۳���1'
);
insert into comments values(
2, 1, '1111', '��۳���2'
);
insert into comments values(
3, 5, '1111', '��۳���3'
);
insert into comments values(
4, 2, '1111', '��۳���4'
);
insert into comments values(
5, 5, '1111', '��۳���5'
);
select * from board;

select * from comments;

-- fk ��� �� ����
-- - fkŰ�� ��ϵǾ� �ִ� ��� �����͸� ������Ű�� ��.
-- - fkŰ�� ��ϵǾ� �ִ� �����ʹ� ��� �����Ű�� ��
delete board where bno =5;

-- �ܷ�Ű ����
alter table board drop constraints fk_id;
alter table comments drop constraints fk_bno;

select * from board;
select * from comments;

delete board where bno=1;

alter table board
add constraints fk_id foreign key(id)
references member(id);

-- fk_cno�� �����ǵ��� ��.
alter table comments 
add constraint fk_bno foreign key(bno)
references comments(bno) on delete cascade;

delete comments where cno=2; -- ���� �����ؾ� �Ʒ��� ���� ��(primary key ���� �����ؾ� foreign key ���� ����)


-- check : �������� Ư������ ����, Ư������ �Էµǵ��� ��
create table emp(
empno number(4) primary key,
ename varchar2(20) not null,
job varchar2(9) default '0001' , -- column�� �����͸� ���������� �ڵ����� 0001�� ����.
sal number(7,2) check (sal between 2000 and 20000),
gender varchar2(6) check(gender in('����','����'))
);

insert into emp(empno, ename, job, sal, gender) values(
1,'ȫ�浿''0002',3000,'����'
);

insert into emp(empno, ename, job, sal, gender) values(
2,'������''0003',4000,'����'
);
-- ���� ����, ���ڸ� ����
insert into emp(empno, ename, job, sal, gender) values(
3,'�̼���''0004',5000,'�߼�'
);

insert into emp(empno, ename, job, sal, gender) values(
3,'�̼���''0004',5000,'����'
);

insert into emp(empno, ename, job, sal, gender) values(
4,'������''0005',2000,'����'
);
-- ���� 2000 ! 20000
insert into emp(empno, ename, job, sal, gender) values(
5,'�豸''0006',1000,'����'
);
-- check 2000-20000
insert into emp(empno, ename, job, sal, gender) values(
5,'�豸''0006',20000,'����'
);
-- job default '0001' ==> job �Է� ���ϸ� 0001
insert into emp(empno, ename, sal, gender) values(
6,'������',10000,'����'
);

select * from emp