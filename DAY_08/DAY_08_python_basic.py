
# coding: utf-8

# In[ ]:

# 작업 자동화
# 우리가 반복적으로 사용할 어떤 특정 기능들에 대해서 => "재사용 가능한 코드 덩어리"


# In[1]:

def greeting():
    username = input()
    print("{username}님, 가입을 축하드립니다.".format(username=username))


# In[2]:

greeting()


# In[7]:

def print_pretty_star(count):
    """
    이 함수는 별찍기 함수입니다.
    """
    for i in range(count):
        print("*" * (i + 1))


# In[5]:

print_pretty_star(5)


# In[8]:

get_ipython().magic('pinfo print_pretty_star')

