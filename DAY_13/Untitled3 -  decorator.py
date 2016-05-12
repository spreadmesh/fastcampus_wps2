
# coding: utf-8

# In[1]:

class FastcampusPerson():  # 패스트캠퍼스에 있는 사람 한명 한명
    # 학생과 매니저가 구분될 수 있어야 합니다.
    # 대성님 => 1기 데사스, 2기 웹프스
    # 재근님 => 1기 수강생 => 매니저에 의해서 매니저로 임명
    
    def __init__(self, name, is_manager=False):
        self.name = name
        self.is_manager = is_manager
    
    def __str__(self):
        return self.name


# In[2]:

# class IsManager():
    
#     def __init__(self, function):
#         self.function = function
        
#     def __call__(self, *args, **kwargs):
#         manager, student = args
#         if not manager.is_manager:
#             raise PermissionDeniedError(manager)
#         return self.function(self, *args, **kwargs)

def IsManager(function):
    def wrapper(*args, **kwargs):
        school, manager, student = args               # 범용성을 위해서 수정되어야 합니다.
        if not manager.is_manager:
            raise PermissionDeniedError(manager)
        return function(*args, **kwargs)
    return wrapper
        
        
class FastcampusSchool():  # 패스트캠퍼스 스쿨 관리 클래스
    
    def __init__(self, name, *args, **kwargs):
        self.name = name
        self.students = set()
        
        self.tuition = kwargs.get("tuition", 480)  # 수강료가 따로 입력되지 않으면, 기본으로 480만원
        # manager_list = []
    
    @IsManager
    def add_student(self, manager, student):  
            print("{manager} 가 {student} 을 추가했습니다.".format(
                manager=manager.name,
                student=student.name,
            ))
            self.students.add(student)
        
    def show_students(self, manager):
        if not manager.is_manager:
            raise PermissionDeniedError(manager)
        print("--------------------------------------------------------------")
        print("--------- Student/Manager List--------")
        print("--------------------------------------------------------------")
        message = "\n".join([
                "{name}({role})".format(
                name=student.name,
                role="Manager" if student.is_manager else "Student")
                for student
                in self.students
            ])
        print(message)
        
        # "______ 매니저가 학생들을 조회했습니다." 라고 메시지 출력
        # 단, 학생이 학생 정보를 출력하려고 하면 => 에러가 발생해야 합니다.
        pass
        
    def show_revenue(self, manager):
        # 전체 매출을 구하는 애 ( 학생 수 * 360 )
        # 학생이 전체 매출을 구하려고 하면, => 에러가 발생해야 합니다.
        total_revenue = len(self.students) * self.tuition
        print("----------------------------")
        print("{total_students} 명 * {tuition} 만원".format(total_students=len(self.students), tuition=self.tuition))
        print("=> {total_revenue} 만원".format(total_revenue=total_revenue))
        print("----------------------------")

    
    def __str__(self):
        return self.name


# In[ ]:




# In[3]:


wps = FastcampusSchool("웹 프로그래밍 SCHOOL")
print(wps)


# In[4]:


suchan = FastcampusPerson("안수찬")  # 학생
jkpark = FastcampusPerson("박준영", is_manager=True)  # 매니저
kisu = FastcampusPerson("장기수")  # 학생


# In[10]:


wps.add_student(jkpark, suchan)
wps.add_student(jkpark, kisu)
wps.add_student(jkpark, kisu)


# In[11]:

donguk = FastcampusPerson("동욱")  # 학생
wps.add_student(suchan, donguk)


# In[12]:

class PermissionDeniedError(Exception):
    
    def __init__(self, person):
        self.person = person
    
    def __str__(self):
        return "{name} 은 매니저가 아니라서, 권한이 없습니다.".format(
            name=self.person.name,
        )


# In[13]:

wps.show_students(jkpark)
wps.show_revenue(jkpark)


# In[ ]:




# In[ ]:




# In[ ]:



