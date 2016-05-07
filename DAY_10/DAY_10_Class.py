
# coding: utf-8

# In[1]:

# 절차 지향 프로그래밍
# 데이터, 데이터 처리하는 함수

# 객체 지향 프로그래밍 ( Object Oriented Programming )
# 절차 <<<< 객체
# 객체(데이터, 각가의 데이터를 처리하는 방법) <=> 객체 : 메시지를 전달

# 함수형 프로그래밍 => 모든 객체 자체를 함수로 본다? / Lambda Operator, List Comprehension


# In[2]:

# 장기수 학생을 만들려면
# 학생이 무엇인가?

class Student():
#    name = ""
#   age = ""
    
    __campus = "패스트캠퍼스"
    
    def __init__(self, name, age):
        # init => initalize ( 초기화하다 )
        # Student() => __init__ 함수가 실행되는 것
        self.name = name
        self.age = age
        
        print("학생 {name}({age}) 가 태어났습니다.".format(
            name=self.name,
            age=self.age
        ))
    
    # 자기소개를 할 수 있다.
    def introduce(self):
        print("안녕하세요, 저는 {campus}에 다니는 {age}살 {name}입니다.".format(
                age=self.age,
                name=self.name,
                campus=self.__campus
            ))


# In[3]:

# 이름을 입력을 안했을 때, => 객체가 만들어지지 않도록 해야합니다.
spreadmesh = Student("장기수", 29)
#spreadmesh = Student()


#spreadmesh.name = "장기수"
#spreadmesh.age = 29


# In[4]:

print(spreadmesh.name)


# In[5]:

spreadmesh.introduce()


# In[6]:

dir(spreadmesh)
# spreadmesh._Student__campus = " 다른 캠퍼스 " # 이렇게 바꾸는게 가능하지만 그러지 않는것이 일반이다. 다른 프로그래밍언어에선 private이 있음


# In[ ]:




# In[ ]:




# In[32]:

class Rectangle():
    width = ""
    height = "" 
    
    def __init__(self, width, height):
        self.width = width
        self.height = height 
    
    def area(self):    # 넓이
        return self.width  * self.height
    
    def girth(self):    # 둘레
        return self.width * 2 + self.height * 2
    
    def is_bigger(self, another):
        print("내가 더 큼") if self.area() >= another.area() else print("내가 더 작음")


# In[33]:

nemo1 = Rectangle(10, 20)


# In[34]:

nemo1.area()


# In[35]:

nemo1.girth()


# In[36]:

nemo2 = Rectangle(15, 20)


# In[61]:

nemo1.is_bigger(nemo2)


# In[ ]:




# In[ ]:




# In[ ]:




# In[43]:

#데이터 불러오기 
with open("../../users.csv", "r") as f:
        data_list = [
            {
                "name": line.split(",")[0],
                "address": line.split(",")[1].replace("\n",""),
            }
            for line
            in f.readlines()
        ]
        
print(data_list[2])


# In[48]:

class Student():
    
    def __init__(self, name, address):
        # init => initalize ( 초기화하다 )
        # Student() => __init__ 함수가 실행되는 것
        self.name = name
        self.address = address
        
    
    # 자기소개를 할 수 있다.
    def introduce(self):
        print("안녕하세요, 저는 {address}에 사는 {name}입니다.".format(
                address=self.address,
                name=self.name,
            ))


# In[56]:

student = Student(data_list[0]['name'],data_list[0]['address'])
student.introduce()


# In[54]:

data_list[0]['name']


# In[58]:

# 객체 초기화 하자
student_list = [
    Student(i['name'],i['address'])
    for i
    in data_list
]


# In[62]:

for student in student_list:
    student.introduce()
    


# In[72]:

with open("../../users.csv", "r") as f:
    student_list2 = [
        
            Student(
                line.split(",")[0],
                line.split(",")[1].replace("\n","")
            )
        
        for line
        in f.readlines()
    ]


# In[73]:

for student in student_list2:
    student.introduce()
    

