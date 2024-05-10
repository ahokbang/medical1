-- 테이블 생성
create table stu_score(
 no number(4) primary key, 
 name varchar2(30), 
 kor number(3),
 eng number(3),
 math number(3),
 total number(3),
 avg number(6)
);

-- 1개 데이터 입력: insert 
insert into stu_score (no, name, kor, eng, math, total, avg) values(
1, '홍길동', 58, 99, 95, (58+99+95), (58+99+95)/3
);

-- data 검색: select
select * from STU_SCORE;

commit;

-- 1개 데이터 수정: update
update stu_score set name='홍길자' where no=1;

select * from stu_score;

rollback;

select * from stu_score;

desc stu_score;

-- 삭제: delete
delete stu_score where no=1;

select * from stu_score;
-- commit 전까지는 실제 데이터에 반영하진 않아.

commit;
-- 완전 삭제. 복구 불가. 복구 방법 없음.

drop table stu_score;
-- rollback이 없어. 
