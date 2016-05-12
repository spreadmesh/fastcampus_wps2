
# coding: utf-8

# In[1]:

# Decorator - function, class
# 장점: decorator 도 의미있는 데이터와, 메쏘드들로 묶을 수 있다. ( "모듈화" 할 수 있다. )


# In[2]:

import time



def timer(function):
    def wrapper(*args, **kwargs):  # packing => 함수 정의부
        start_time = time.time()
        print(args)
        print(kwargs)
        # print("args => {my_args}".format(my_args=args))
        # print("kwargs => {my_kwargs}".format(my_kwargs=kwargs))
        result = function(*args, **kwargs)  # unpacking => tuple => ... / dict => key,value...
                                            # 함수 호출부
        end_time = time.time()
        print("{time}s".format(time=end_time-start_time))
        return result
    return wrapper  # 새로운 함수를 만들고, 그 함수를 return 하는 함수 => decorator 함수


# In[3]:

@timer
def print_hello():
    print("hello world")


# In[4]:

print_hello()  # print_hello 라는 이름을 가지고 있기는 하지만, 사실상의 timer => wrapper function이 실행


# In[33]:

def print_goodbye():
    print("good bye")
    
aaa = timer(print_goodbye)   # 사실상 decorator 는 기존의 정의된 함수를 한번 묶는 것과 100% 동일하다.
# print_goodbye = timer(print_goodbye) # 사실 이렇게 많이 쓰지


# In[26]:

aaa()
# print_goodbye()


# In[8]:

# args, kwargs

def hello_items(**kwargs):   # 함수를 정의하는 시점에 사용하는 kwargs ( **kwargs ) => packing
    for key, value in kwargs.items():
        print("{key} => {value}".format(key=key, value=value))


# In[9]:

hello_items(name="dobestan", age=24)


# In[10]:

information = {"name": "dobestan", "age": 24}
hello_items(**information)  # dict => key, value => unpacking
# 함수를 호출하는 시점에서 사용하는 kwargs ( **kwargs )


# In[11]:

@timer
def print_student_info(name, course, age):
    pass


# In[13]:

print_student_info("dobestan", "wps", 24) # => *args => packing


# In[ ]:

# 여기서 packing / unpacking을 볼 수 있어


# In[ ]:




# In[46]:

# bold , italic decorator 구현하기 2개
# 함수 아무거나 2개 구현하셔서어~

def bold(func):
    def a(*args, **kwargs):
        return "<b>" + func(*args, **kwargs) + "</b>"
    return a


# In[52]:

def my_str():
    return "hello_world"

my_str= bold(my_str)
# 이거랑


# In[ ]:

# 이거랑 완전히 같아.
@bold
def my_str():
    return "hello_world"


# In[50]:

my_str()


# In[ ]:




# In[40]:

my_str = bold(my_str)


# In[41]:

my_str("bbd")


# In[ ]:



