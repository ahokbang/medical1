-- ���̺� ����
create table stu_score(
 no number(4) primary key, 
 name varchar2(30), 
 kor number(3),
 eng number(3),
 math number(3),
 total number(3),
 avg number(6)
);

-- 1�� ������ �Է�: insert 
insert into stu_score (no, name, kor, eng, math, total, avg) values(
1, 'ȫ�浿', 58, 99, 95, (58+99+95), (58+99+95)/3
);

-- data �˻�: select
select * from STU_SCORE;

commit;

-- 1�� ������ ����: update
update stu_score set name='ȫ����' where no=1;

select * from stu_score;

rollback;

select * from stu_score;

desc stu_score;

-- ����: delete
delete stu_score where no=1;

select * from stu_score;
-- commit �������� ���� �����Ϳ� �ݿ����� �ʾ�.

commit;
-- ���� ����. ���� �Ұ�. ���� ��� ����.

drop table stu_score;
-- rollback�� ����. 