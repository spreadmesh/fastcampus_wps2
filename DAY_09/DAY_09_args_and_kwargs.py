
# coding: utf-8

# In[1]:

def sum(a, b):
    return a + b


# In[2]:

result = sum(1, 3)


# In[5]:

print(sum(1, 3))


# In[6]:

result


# In[13]:

# 입력받은 모든 숫자를 더해주는 'sum' 이라는 함수를 만들어라.
def sum(list):
    sum = 0
    for i in list:
        sum += i
    return sum


# In[16]:

print(sum([1,6,4,9])) # => print(sum(1,6,4,9)) 으로 바꿔보자


# In[18]:

def sum(*args):    # * (별표)를 주의깊게 보자
    total = 0
    for arg in args:
        total += arg
    return total


# In[20]:

print(sum(1,6,4,9))


# In[21]:

def greeting(name,course):
    print("{name}님, {course} 등록을 축하드립니다.".format(name=name, course=course))
    
greeting("장기수", "웹프스")


# In[22]:

values = ("장기수", "웹프스")


# In[25]:

greeting(*values)


# In[31]:

def greeting3(name, course, reason):
    print("{name}님, {course} 등록을 축하드립니다.\n{reason}을/를 목적으로 수강하셨군요".format(name=name, reason=reason, course=course))
    


# In[32]:

values = ("장기수", "웹프스", "개발능력증진")


# In[34]:

greeting3(*values)


# In[35]:

# unnamed => *args ( tuple )
# named     => **kwargs ( dict )


# In[36]:

def greeting(name,course):
    print("{name}님, {course} 등록을 축하드립니다.".format(name=name, course=course))
    


# In[38]:

greeting(name="장기수", course="웹프스")


# In[41]:

value = {
    "name": "장기수",
    "course": "웹프스"
}


# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[43]:

def print_all_informations(**kwargs):
    for key, value in kwargs.items():
        print("{key} => {value}".format(key=key, value=value))


# In[46]:

informations = {
    "name": "장기수",
    "email": "spreadmesh@gmail.com",
    "phonenumber": "01029120007",
}


# In[48]:

print_all_informations(**informations)


# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:



