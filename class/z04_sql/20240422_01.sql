select * from employees;

select employee_id, emp_name from employees;

select salary from employees;

-- Ÿ���� number�� ���� ��Ģ����(+, -, *, /) ����
select salary, salary*1400, salary*1400*12 from employees;
-- column�� �ϳ��� ������ �Ѿ��.
-- salaty*1400, salary*1400*12�� ��� ��� �����ϰ� �ѹ��� �˱� �����Ƿ� �Ʒ��� ���� ��Ī���� ǥ�� ����(as ������ ��, as ���� ����).
select salary, salary*1400 as k_sal, salary*1400*12 as y_sal from employees;

select * from stu_score;

select no, name, kor, eng, math, total, avg, rank from stu_score;

-- ���̽�

select department_id from employees;
-- null --> 0���� �ٲٱ�: nvl(department_id(�ش� ��), 0(�ٲ� ����)), nvl�� null value�� �ǹ�
select nvl(department_id,0) from employees;

select * from employees;

-- ���� = ����+(����*Ŀ�̼�)
select salary + (salary*commission_pct) from employees; -- ==> null ���ڷ� �ٲ��־�� ��

-- ��Ī:  as ���, "": Ű���带 �ִ� �״�� ���
select salary, salary + (salary * nvl(commission_pct, 0)) Real_sal from employees; -- as ����
-- select salary, salary + (salary * nvl(commission_pct, 0)) as real_sal from employees;
-- ����Ŭ�� ��ҹ��� �������� �ʾ�. �빮�ڷ� �ۼ��ϰ� ������ �Ʒ��� ���� "" ���.
select salary, salary + (salary * nvl(commission_pct, 0)) "Real_sal" from employees; 
-- *�� ������ �ְ� ���� ���� "" ���
select salary, salary + (salary * nvl(commission_pct, 0)) "real_sal*" from employees; 
-- �ѱ۵� ���������� �ѱ� ����� ������ ����. "" ��� �����ϸ�, ������� �ʾƵ� ��µ�.
select salary ���� from employees; 


select * from departments;

-- �μ���ȣ, �μ��̸��� ����Ͻÿ�.
select department_id, department_name from departments;

-- concat: �������� �����͸� 1���� ���ļ� �Ѱܾ� �� ��� ==> �ΰ� �̻��� �����͸� ��ĥ �� ���
-- �Ʒ��� ������� ��ġ�µ�, concat�� ���
a+","+b+","

-- concat(||): ȫ�浿, ������, �̼���, ������, �豸 ==> split���� �и� ���� 
-- split(",")" �и�
select * from stu_score;
-- concat ||
select kor||','||eng||','||math stu from stu_score;
-- �Ʒ��� ���� + ��� ����
select kor+eng+math as total from stu_score;
select kor+eng+math as total, (kor+eng+math)/3 from stu_score;

-- distinct : �ߺ� ����
-- where: ������ not �����ϰ� �˻��Ϸ��� is not null
select distinct department_id from employees where department_id is not null; -- null�� �����ϰ� ���

-- manager_id
select distinct manager_id from employees;
-- null ����
select distinct manager_id from employees where manager_id is not null;


select employee_id,salary from employees
where employee_id = 200;

-- 201�� ���� �ʹٸ�,
select employee_id,salary from employees
where employee_id = 200 or employee_id = 201;

-- �̻��� ��
select* from employees
where employee_id >=200; 
-- 200 �̻� 203����
select*from employees
where employeed_id >= 200 and employee_id <= 203;
-- 150 ����, 200�̻�
select * from employees
where employee_id <=150 or employee_id >=200;

-- ������ : where �÷� ������ �񱳴��

-- department_id 10, 30, 50�� �ش��ϴ� ��� ���
select employee_id, department_id from employees
where department_id=10 or department_id = 30 or department_id = 50;
select * from employees;
-- ������ 6000�޷� �̻� 9000�޷� ������ ��� ����Ͻÿ�.
-- order by �÷��� asc : ��������
-- order by �÷��� desc: ��������
select employee_id, emp_name, salary from employees
where salary >= 6000 and salary<= 9000 order by salary asc;
-- ������ 6000, 7000, 8000�� ��� ���
select employee_id, emp_name, salary from employees
where salary = 6000 or salary = 7000 or salary = 8000;
-- �μ���ȣ�� 50���̸鼭, ������ 8000 �̻��� ����� ����Ͻÿ�.
select employee_id, emp_name, department_id, salary from employees
where department_id = 50 and salary >= 8000;

-- stu_score �̸��� ȫ�浿�� ��� ���
select * from stu_score where name = 'ȫ�浿';

-- ��������
select hire_date from employees order by hire_date asc;
-- ��������
select hire_date from employees order by hire_date desc;

-- [ ��¥ �� ]
-- 2002�� ���Ŀ� �Ի��� ��� ���
select emp_name, hire_date from employees 
where hire_date >= '02/01/01'
order by hire_date asc
;
-- ��¥ ���ϱ�
select hire_date, hire_date+100 from employees;
-- ��¥ ����
-- �ݿø� : round(�ݿø� �� ����, �Ҽ����ڸ�)
select round(sysdate - hire_date, 2) from employees;

select * from employees;
-- �̸�, �̸��� �� ��ġ�� ==> ������ġ��: + ������ �Ұ���, concat(||) ��ɾ� ���
select emp_name || email from employees;

-- ��� ���̺��� �Ի��� 05�� �̻� 06�� �����̸鼭 ������ 6000 �޷� �̻��� ��� �������ķ� ���
select * from employees
where hire_date>='05/01/01' and hire_date<='06/12/31' and salary >= 6000
order by hire_date desc
;

-- !=, <>, ^=, not
select department_id from employees
where department_id != 10 and department_id != 50
-- ���������� ��� asc ���� ����
order by department_id 
;

-- !=�� �Ʒ��� ���� �ۼ� ����(���� ����) and not �÷� = ��
select department_id from employees
where department_id != 10 and not department_id = 50
order by department_id ;

-- salary 5000 �̻� 9000 ���� (��������)
select * from employees
where salary >= 5000 and salary <= 9000
order by salary
;

-- ����� 99�� �̻��� �л� �˻�
select * from stu_score
where avg >= 99 
;


select * from students;
update students set name='������'
where no=10
;
commit;

-- students
-- ���� 70�� �̻��̸鼭 ����� 75�� �̻� �л� ���
select * from students
where kor>= 70 and avg >= 75
;

-- ���� 80��, ���� 70��, ���� 90���� �л��� ����Ͻÿ�.
select * from students
where kor = 80 or kor = 70 or kor = 90
;

update students set kor=100  
where no=1
;
-- ��� �ٲ�� total, avg �ٲ��� ����.
select * from students
where no=1
;
-- �׷��� �� �ǵ�����,
rollback;

-- �Ʒ��� ���� �����ؾ� ��.
update students set kor=100, total = 100+eng+math, avg = (100+eng+math)/3
where no=1
;
select * from students where no=1;

-- ���������� 70�� �̻�~90�� ���� �л� ���
select * from students
where kor>= 70 and kor<=90
;

-- between a and b : a�� b ����(�̻�, ������ �ǹ̷� ���� a, b ���� ���ԵǾ� ���� �� ��� ����)
-- a���� ũ�ų� ���� b���� �۰ų� ���� �� �˻�
-- between�� ����ؼ� ���� �ڵ�(190~191��)�� �Ʒ��� ���� ǥ���� �� ����
select * from students
where kor between 80 and 90
;
-- not between a and b : a ���� �۰ų� b���� ū �� �˻� ==> a���� �۰ų� b���� Ŭ ��� ���(a, b ������)
select * from students
where kor not between 70 and 90
;

-- between a and b : ��¥�� ����
 select hire_date from employees
 order by hire_date
 ;

-- �Ի����� 99�� ���� ũ�ų� ����, 01�� ���� �۰ų� ���� ��� �˻�
select * from employees
where hire_date between '99/01/01' and '01/12/31'
order by hire_date 
;

-- in : ������ �ʵ尡 �������� �� �߿� �ϳ��� �˻��� ��� ==> �ش簪�� �� ���
select name, kor from students
where kor in (80, 70, 90);

-- not in : �ش� �� �����ϰ� �˻�
select name, kor from students
where kor not in (80, 70, 90);


-- �̸� �˻�
select * from students
where name='ȫ�浿'
;

-- like �˻�: Ư�� �ܾ ���ԵǾ� �ִ� ���� �˻�
-- name(��)�� ȫ�̶�� ���ڰ� ���ִ� �� ���. %�� ���Ѵ� �ǹ�
-- ȫ% : ȫ���� �����ϴ� �ܾ� �˻�
select * from students
where name like 'ȫ%'
;
-- %�� : ������ ������ �ܾ� �˻�
select * from students
where name like '%��'
;
-- %��% : Ư�� �ܾ ���ԵǾ� �ִ� �ܾ� �˻�, ���� ���ԵǾ� �ִ� �ܾ� �˻� 
select * from students
where name like '%��%'
;
-- _ : �� ������ ���
select * from students
where name like '_��%' -- �� �տ��� ������ �� ���ڰ������鼭 ���� ���ԵǾ� �ִ� �ܾ� �˻�
;

-- �̸��� ������ �ڸ��� t�� �� ��� �̸� ���
select * from students
where name like '__t%'
;
-- �̸��� 4�ڸ��̰�, 3��° �ڸ��� r�� �� �ִ� �̸� �˻�
select * from students
where name like '__r_'
;

-- �̸� ���̰� 4�ڸ��� �� �˻�
select name from students
where length(name) = 4
;

-- length�� ����ϸ� �Ʒ��� ���� �ۼ� ����
select * from students
where name like '__r%' and length(name)=4
;

-- �̸��� A�� ���۵Ǵ� �л� �˻�
select * from students
where name like 'A%'
;

-- �̸��� a�� �� �ִ� �л� �˻� ==> A�� ������ �ʾ�
select * from students
where name like '%a%'
;

-- ��ҹ��� ���о��� a�� �� �ִ� �л� �˻� ==> �ҹ��� ġȯ
-- lower(�ҹ��� ġȯ), upper(�빮�� ġȯ), (initcap) ù���ڸ� �빮�� 
select * from students
where lower(name) like '%a%'
;

-- a�� ���Ե��� ���� �̸��� �˻�
select * from students
where lower(name) not like '%a%'
;

select manager_id from employees;

-- manager_id �� 100�� ��� �˻�
select * from employees
where manager_id = 100
;
-- null�� � �񱳰� �ȵ� ==> null�� ���� ���� �˻����� �ʾ�.
select * from employees
where manager_id = null
;
-- null���� is null ��ɾ� ���
select * from employees
where manager_id is null
;
-- null�� �ƴ� �� ��� �ÿ��� is not null ���
select * from employees
where manager_id is not null
;

-- [5�� ����]
-- ��������, ��������, �ѱ۵� ���� ����
select * from stu_score;
-- �̸� ��������
select * from stu_score
order by name desc
;
-- �̸� ��������
select * from stu_score
order by name asc
;
-- 2�� ���� �̻��� ���� ����
-- ���������� �������� �� ���� ������ ��� ���������� �������� ����.
select * from students
order by kor desc, eng asc
;

-- total�� ��������
select * from students
order by total desc
;

-- column �߰�
alter table students add rank number(3);

-- colum type
desc students;

select * from students;

update students set rank=0;

commit;

-- ��� ==> ������������ ������ ���� �ʾ�. ���� ���Ѿ� ��
select no, name, total, rank() over(order by total desc) as rank from students
;

(select no, ranks from (select no, rank() over(order by total desc) as ranks from students) s2
;

select * from students; -- ��� ����Ǿ� ���� �ʾ�. �� 0���� ����. ==> ������ 2�� ���ƾ� �� ���� �ڵ尪�� �ٽ� �־���� ��

-- ��� ���� ���, 1���� ��
update students set rank=13 where no=1;

-- ��� ���� ���, ��ü �� ==> ��������
update students s1 set rank = (
select ranks from (select no, rank() over(order by total desc) as ranks from students) s2
where s1.no = s2.no)
;

select * from students;

update students s1 set rank = 13
where no = 1
;

select * from students
where kor >= 70
;

-- select * from(���̺�);
select * from (select * from students where avg >= 80)
where kor >= 70
;
