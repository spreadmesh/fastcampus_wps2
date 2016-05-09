
# coding: utf-8

# In[1]:

# 복습 Class ( 붕어빵틀 ) => 객체 ( Object; 붕어빵 )


# In[8]:

class Student():
    
    def __init__(self, name):
        self.name = name
        
    def study(self):
        print("일반 학생이 공부를 시작합니다.")
    
    def coding(self):
        print("일반 학생은 코딩을 할 수 없습니다.")
        
# class WebProgrammingStudent():
    
#     def __init__(self, name):
#         self.name = name
        
#     def study(self):
#         print("일반 학생이 공부를 시작합니다.")
    
#     def coding(self):
#         print("웹 개발 코딩을 시작합니다.")
        
class DataScienceStudent(Student):
    
    def coding(self): # Class 의 함수 => "Method"  => 메쏘드를 덮어쓰는 행위 => 메쏘드 오버라이딩(overriding)
        print("데이터 사이언스에 대한 코딩을 시작합니다.")
    
#     def __init__(self, name):
#         self.name = name
        
#     def study(self):
#         print("일반 학생이 공부를 시작합니다.")
    
#     def coding(self):
#         print("데이터 사이언스에 대한 코딩을 시작합니다.")


# In[5]:

web_programming_student = WebProgrammingStudent("웹개발학생")
web_programming_student.study()
web_programming_student.coding()


# In[9]:

data_science_student = DataScienceStudent("데이터사이언스학생")
data_science_student.study()
data_science_student.coding()


# In[12]:

dss = DataScienceStudent("데사쓰")
dss.coding()

