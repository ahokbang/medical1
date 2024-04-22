select * from employees;

select employee_id, emp_name from employees;

select salary from employees;

-- 타입이 number일 때는 사칙여산(+, -, *, /) 가능
select salary, salary*1400, salary*1400*12 from employees;
-- column이 하나의 변수로 넘어와.
-- salaty*1400, salary*1400*12의 경우 길고 복잡하고 한번에 알기 어려우므로 아래와 같이 별칭으로 표현 가능(as 변수명 단, as 생략 가능).
select salary, salary*1400 as k_sal, salary*1400*12 as y_sal from employees;

select * from stu_score;

select no, name, kor, eng, math, total, avg, rank from stu_score;

-- 파이썬

select department_id from employees;
-- null --> 0으로 바꾸기: nvl(department_id(해당 열), 0(바꿀 숫자)), nvl는 null value를 의미
select nvl(department_id,0) from employees;

select * from employees;

-- 월급 = 월급+(월급*커미션)
select salary + (salary*commission_pct) from employees; -- ==> null 숫자로 바꿔주어야 해

-- 별칭:  as 사용, "": 키워드를 있는 그대로 사용
select salary, salary + (salary * nvl(commission_pct, 0)) Real_sal from employees; -- as 생략
-- select salary, salary + (salary * nvl(commission_pct, 0)) as real_sal from employees;
-- 오라클은 대소문자 구분하지 않아. 대문자로 작성하고 싶으면 아래와 같이 "" 사용.
select salary, salary + (salary * nvl(commission_pct, 0)) "Real_sal" from employees; 
-- *를 변수에 넣고 싶을 때도 "" 사용
select salary, salary + (salary * nvl(commission_pct, 0)) "real_sal*" from employees; 
-- 한글도 가능하지만 한글 사용을 권하지 않음. "" 사용 가능하며, 사용하지 않아도 출력됨.
select salary 연봉 from employees; 


select * from departments;

-- 부서번호, 부서이름을 출력하시오.
select department_id, department_name from departments;

-- concat: 여러개의 데이터를 1개로 합쳐서 넘겨야 할 경우 ==> 두개 이상의 데이터를 합칠 때 사용
-- 아래의 방법으로 합치는데, concat을 사용
a+","+b+","

-- concat(||): 홍길동, 유관순, 이순신, 강감찬, 김구 ==> split으로 분리 가능 
-- split(",")" 분리
select * from stu_score;
-- concat ||
select kor||','||eng||','||math stu from stu_score;
-- 아래와 같이 + 사용 가능
select kor+eng+math as total from stu_score;
select kor+eng+math as total, (kor+eng+math)/3 from stu_score;

-- distinct : 중복 제거
-- where: 조건절 not 제거하고 검색하려면 is not null
select distinct department_id from employees where department_id is not null; -- null값 제거하고 출력

-- manager_id
select distinct manager_id from employees;
-- null 제거
select distinct manager_id from employees where manager_id is not null;


select employee_id,salary from employees
where employee_id = 200;

-- 201도 보고 싶다면,
select employee_id,salary from employees
where employee_id = 200 or employee_id = 201;

-- 이상일 때
select* from employees
where employee_id >=200; 
-- 200 이상 203이하
select*from employees
where employeed_id >= 200 and employee_id <= 203;
-- 150 이하, 200이상
select * from employees
where employee_id <=150 or employee_id >=200;

-- 조건절 : where 컬럼 연산자 비교대상값

-- department_id 10, 30, 50에 해당하는 사원 출력
select employee_id, department_id from employees
where department_id=10 or department_id = 30 or department_id = 50;
select * from employees;
-- 월급이 6000달러 이상 9000달러 이하인 사원 출력하시오.
-- order by 컬럼명 asc : 순차정렬
-- order by 컬럼명 desc: 역순정렬
select employee_id, emp_name, salary from employees
where salary >= 6000 and salary<= 9000 order by salary asc;
-- 월급이 6000, 7000, 8000인 사원 출력
select employee_id, emp_name, salary from employees
where salary = 6000 or salary = 7000 or salary = 8000;
-- 부서번호가 50번이면서, 월급이 8000 이상인 사원을 출력하시오.
select employee_id, emp_name, department_id, salary from employees
where department_id = 50 and salary >= 8000;

-- stu_score 이름이 홍길동인 사람 출력
select * from stu_score where name = '홍길동';

-- 순차정렬
select hire_date from employees order by hire_date asc;
-- 역순정렬
select hire_date from employees order by hire_date desc;

-- [ 날짜 비교 ]
-- 2002년 이후에 입사한 사람 출력
select emp_name, hire_date from employees 
where hire_date >= '02/01/01'
order by hire_date asc
;
-- 날짜 더하기
select hire_date, hire_date+100 from employees;
-- 날짜 빼기
-- 반올림 : round(반올림 할 숫자, 소숫점자리)
select round(sysdate - hire_date, 2) from employees;

select * from employees;
-- 이름, 이메일 열 합치기 ==> 문자합치기: + 연산자 불가능, concat(||) 명령어 사용
select emp_name || email from employees;

-- 사원 테이블에서 입사일 05년 이상 06년 이하이면서 월급이 6000 달러 이상인 사원 역순정렬로 출력
select * from employees
where hire_date>='05/01/01' and hire_date<='06/12/31' and salary >= 6000
order by hire_date desc
;

-- !=, <>, ^=, not
select department_id from employees
where department_id != 10 and department_id != 50
-- 순차정렬의 경우 asc 생략 가능
order by department_id 
;

-- !=은 아래와 같이 작성 가능(위와 동일) and not 컬럼 = 값
select department_id from employees
where department_id != 10 and not department_id = 50
order by department_id ;

-- salary 5000 이상 9000 이하 (순차정렬)
select * from employees
where salary >= 5000 and salary <= 9000
order by salary
;

-- 평균이 99점 이상인 학생 검색
select * from stu_score
where avg >= 99 
;


select * from students;
update students set name='관순스'
where no=10
;
commit;

-- students
-- 국어 70점 이상이면서 평균이 75점 이상 학생 출력
select * from students
where kor>= 70 and avg >= 75
;

-- 국어 80점, 국어 70점, 국어 90점인 학생을 출력하시오.
select * from students
where kor = 80 or kor = 70 or kor = 90
;

update students set kor=100  
where no=1
;
-- 국어만 바뀌고 total, avg 바뀌지 않음.
select * from students
where no=1
;
-- 그래서 값 되돌리고,
rollback;

-- 아래와 같이 수정해야 함.
update students set kor=100, total = 100+eng+math, avg = (100+eng+math)/3
where no=1
;
select * from students where no=1;

-- 국어점수가 70점 이상~90점 이하 학생 출력
select * from students
where kor>= 70 and kor<=90
;

-- between a and b : a와 b 사이(이상, 이하의 의미로 값이 a, b 값이 포함되어 있을 때 사용 가능)
-- a보다 크거나 같고 b보다 작거나 같은 것 검색
-- between을 사용해서 위의 코드(190~191행)를 아래와 같이 표현할 수 있음
select * from students
where kor between 80 and 90
;
-- not between a and b : a 보다 작거나 b보다 큰 것 검색 ==> a보다 작거나 b보다 클 경우 사용(a, b 미포함)
select * from students
where kor not between 70 and 90
;

-- between a and b : 날짜도 가능
 select hire_date from employees
 order by hire_date
 ;

-- 입사일이 99년 보다 크거나 같고, 01년 보다 작거나 같은 사원 검색
select * from employees
where hire_date between '99/01/01' and '01/12/31'
order by hire_date 
;

-- in : 동일한 필드가 여러개의 값 중에 하나를 검색할 경우 ==> 해당값인 열 출력
select name, kor from students
where kor in (80, 70, 90);

-- not in : 해당 값 제외하고 검색
select name, kor from students
where kor not in (80, 70, 90);


-- 이름 검색
select * from students
where name='홍길동'
;

-- like 검색: 특정 단어가 포함되어 있는 것을 검색
-- name(열)에 홍이라는 글자가 들어가있는 열 출력. %는 무한대 의미
-- 홍% : 홍으로 시작하는 단어 검색
select * from students
where name like '홍%'
;
-- %순 : 순으로 끝나는 단어 검색
select * from students
where name like '%순'
;
-- %길% : 특정 단어가 포함되어 있는 단어 검색, 길이 포함되어 있는 단어 검색 
select * from students
where name like '%길%'
;
-- _ : 한 공간을 사용
select * from students
where name like '_길%' -- 길 앞에는 무조건 한 글자가있으면서 길이 포함되어 있는 단어 검색
;

-- 이름에 세번재 자리에 t가 들어간 모든 이름 출력
select * from students
where name like '__t%'
;
-- 이름이 4자리이고, 3번째 자리에 r이 들어가 있는 이름 검색
select * from students
where name like '__r_'
;

-- 이름 길이가 4자리인 것 검색
select name from students
where length(name) = 4
;

-- length를 사용하면 아래와 같이 작성 가능
select * from students
where name like '__r%' and length(name)=4
;

-- 이름이 A로 시작되는 학생 검색
select * from students
where name like 'A%'
;

-- 이름에 a가 들어가 있는 학생 검색 ==> A는 나오지 않아
select * from students
where name like '%a%'
;

-- 대소문자 구분없이 a가 들어가 있는 학생 검색 ==> 소문자 치환
-- lower(소문자 치환), upper(대문자 치환), (initcap) 첫글자만 대문자 
select * from students
where lower(name) like '%a%'
;

-- a가 포함되지 않은 이름을 검색
select * from students
where lower(name) not like '%a%'
;

select manager_id from employees;

-- manager_id 가 100인 사원 검색
select * from employees
where manager_id = 100
;
-- null은 등가 비교가 안됨 ==> null은 위와 같이 검색되지 않아.
select * from employees
where manager_id = null
;
-- null값은 is null 명령어 사용
select * from employees
where manager_id is null
;
-- null이 아닌 값 출력 시에는 is not null 사용
select * from employees
where manager_id is not null
;

-- [5장 정렬]
-- 오름차순, 내림차순, 한글도 정렬 가능
select * from stu_score;
-- 이름 내림차순
select * from stu_score
order by name desc
;
-- 이름 오름차순
select * from stu_score
order by name asc
;
-- 2개 조건 이상일 때의 정렬
-- 국어점수로 역순정렬 후 같은 점수일 경우 영어점수로 순차정렬 진행.
select * from students
order by kor desc, eng asc
;

-- total로 역순정렬
select * from students
order by total desc
;

-- column 추가
alter table students add rank number(3);

-- colum type
desc students;

select * from students;

update students set rank=0;

commit;

-- 등수 ==> 보여는지지만 저장은 되지 않아. 저장 시켜야 해
select no, name, total, rank() over(order by total desc) as rank from students
;

(select no, ranks from (select no, rank() over(order by total desc) as ranks from students) s2
;

select * from students; -- 등수 저장되어 있지 않아. 다 0으로 보여. ==> 쿼리문 2번 돌아야 해 위의 코드값을 다시 넣어줘야 해

-- 등수 수정 방법, 1개의 값
update students set rank=13 where no=1;

-- 등수 수정 방법, 전체 값 ==> 이중쿼리
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

-- select * from(테이블);
select * from (select * from students where avg >= 80)
where kor >= 70
;
