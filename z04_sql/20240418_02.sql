--  ������ �ִ� ���̺� �˻�
select * from tab;
-- F5: �ָܼ��(�ڵ� ��ü����) ==> �����ݷ��� �ִµ� ���� ������, �巡���ϰ�(�ϳ��� �� ����) F5 ������ �� �ุ ���� F9ó��
-- F9: ������(�κн���, �ش� �ڵ�(Ŀ���� �ִ� ��))   ==> F9 �����

select * from employees;

-- ���̺� ���� Ȯ��
desc employees;

-- ���̺� ����
create table stu_score(
    no number(2), 
    kor number(3),
    eng number(3),
    avg number(5,2) 
    -- 3�ڸ��� ����, 2�ڸ� �Ҽ����̹Ƿ� ��(��ü �ڸ���)�� 5, ��(�Ҽ����ڸ�)�� 2
);

-- ���̺� ������ ����
insert into stu_score(no, kor, eng, avg) values(
1, 100, 99, (100+99)/2
);
-- �Ʒ��� ���� ����ؼ� ��� ����
insert into stu_score values(
1, 95, 98, (95+98)/2
);

insert into stu_score values(
    1,80,70.223,(80+70.223)/2
);

select * from stu_score;

-- commint �ؾ� �ݿ�
commit;

create table num(
no number,
name varchar2(10),
kor number,
eng number,
avg number(4,1)
);
-- number�� ���ڸ� �������� ������ 30�� ������ �˾Ƽ� ����


-- ���� ��¥, �⺻ ����: 24/01/01
-- dual �������̺�
select sysdate from dual;

-- ��¥ ���� ����(yyyy/mm/dd -> yyyy-mm-dd), to_chart : ����ȯ => ���� ����
select to_char(sysdate, 'yyyy-mm-dd') from dual;
-- ��/��/��/�� ���
select to_char(sysdate, 'yyyy-mm-dd hh:mi:ss') from dual;
-- �ð��� ���
select to_char(sysdate, 'hh:mi:ss') from dual;

-- ����+100�� ���� ��¥�� �˷���
select sysdate+100 from dual;
-- ����+1000���� ���� ��¥
select sysdate+1000 from dual;
-- ���� ��¥�� 24�� 1�� 1�� ���Ŀ� ��ĥ�� ��������?
select sysdate - to_date('24/01/01') from dual;