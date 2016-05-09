
# coding: utf-8

# In[42]:

class Student():
    
    def __init__(self, name):
        self.name = name
    def study(self):
        print("공부를 합니다.")
    def introduce(self):
        print("저는 {name} 입니다.".format(name=self.name))
        
class DataScienceStudent(Student):
    def introduce(self):
        print("안녕하세요, 저는 데사스 {name} 입니다.".format(name=self.name))

    
    
    
class WebProgrammingStudent(Student):
    pass


# In[44]:

with open("../../dss.csv", "r") as f:
        dss_list = [
            DataScienceStudent(line.split(",")[0])
            for line
            in f.readlines()
       ]
        
with open("../../wps.csv", "r") as f:
        wps_list = [
            WebProgrammingStudent(line.split(",")[0])
            for line
            in f.readlines()
       ]
        


# In[45]:

for i in dss_list:
    i.introduce()
for i in wps_list:
    i.introduce()


# In[53]:

class Student():
    
    __skills = [] # 외부에서 못 부르게 할 때 => 정보 은닉( information hiding )
    
    def __init__(self, name):
        self.name = name
        self.age = 0
        
    def print_skills(self):
        for skill in self.__skills:
            print("{skill} 일을 할 수 있습니다.".format(skill=skill))
            
    def add_skill(self, skill):
        self.__skills.append(skill)
        
    def get_age(self):  # Getter ( 즉, 정보를 가져오는 메쏘드 )
        return self.age
    
    def set_age(self, age):  # Setter ( 즉, 정보를 입력하는 메쏘드 )
        self.age = age


# In[ ]:




# In[59]:

class Human():
    
    def __init__(self, name):
        self.name = name
        self.age = 0
        print("{name} 이라는 사람이 태어났다.".format(name=self.name))
        
    def after_a_year(self):
        self.age += 1
        print("{name} 이라는 사람이 나이를 1살 더 먹었다.".format(name=self.name))
        
    def __str__(self): # 인스턴스가 출력형태로 불릴 때 
        return "'{name}' 이라는 사람".format(name=self.name)
    
    def __del__(self): # 삭제될 때
        print("{name} 이라는 사람이 메모리에서 잊혀졌다.".format(name=self.name))



# In[65]:

human = Human("장기수")


# In[66]:

print(human)


# In[64]:

# 파이썬이 이 사람을 기억 못할 때 => 더이상 필요없다고 생각했을 때
# 메모리에서 지워버리는 겁니다 +_+


# In[69]:

del human


# In[71]:

# 우리가 지금까지 만든 모든 클래스가 객체화 가능한 애들 
# 학생, 데사스 학생, 웹프스 학생, 동물, 사람, ...

# 동물 클래스 
# 조류 클래스 
# 포유류 클래스 

# "먹을 수 있는" 클래스
# "날다" 클래스
# "생각하다 가 가능한" 클래스 

class Animal():
    pass


# In[72]:

class Chicken(Animal):
    pass


# In[73]:

class Flyable():
    
    def fly(self):
        print("날기가 가능하다.")


class Pigeon(Animal, Flyable):
    pass


class Sparrow(Animal, Flyable):
    pass


# In[74]:

sparrow = Sparrow()


# In[75]:

sparrow.fly()


# In[76]:

class Student():
    pass



# In[77]:

class GoodStudentFeature():
    
    def study(self):
        print("열심히 공부한다.")
        

class ILikeToPlayFeature():
    
    def study(self):
        print("공부 안하고 놀러 다닌다.")



# In[78]:

class GoodStudentButLikeToPlayStudent(Student, ILikeToPlayFeature, GoodStudentFeature):
    pass


# In[79]:

student = GoodStudentButLikeToPlayStudent()


# In[80]:

student.study()


# In[ ]:



