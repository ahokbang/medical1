class Student :   
    def __init__(self, name="", total=0) : 
        self.name = name
        self.__total = total # 클래스 내부에서만 접근
    
    def __str__(self):
        return f"이름 : {self.name}, 합계 : {self.__total} "
    
    def set_total(self, total, login_id) : # 캡슐화, 프라이빗(접근제한), 권한있는 사람만 total 수정할 수 있도록
        if login_id == 'admin' : 
            self.__total = total
        else :
            print("admin 관리자가 아니면 수정이 불가능합니다.")
    
    def get_total(self) :
        return self.__total
    
    # def __gt__(self, s1) :
    #     return self.total > s1.total
    
    def stu_print(self) :
        print("학생성적을 출력합니다.")


s1 = Student("홍길동", 95) # 객체선언할 때 무조건 init() 함수 호출
s2 = Student("유관순", 100)

# s1.total = 300
s1.set_total(400, 'admin')
# print(s1.total) # error 접근 불가
print(s1.get_total())

# print(s2)
# print(s1 == s2) # False
# # print(s1 > s2) # error
#                  # s1 과 s2는 주소값이므로 비교가 될 수 없어.
# print(s1.total > s2.total) # 이렇게 써주어야 비교 가능 # False
# #또는 def __gt__(sefl, s1) 함수 사용해서 아래와 같이 표현 가능
# print(s1>s2) # False 