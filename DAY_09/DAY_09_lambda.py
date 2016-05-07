
# coding: utf-8

# In[1]:

# Lambda
# 이름이 없는 함수 ( 익명 함수 )


# In[2]:

def increment(x):
    return x + 1


# In[3]:

increment(55)


# In[4]:

increment_lambda = lambda x: x+1


# In[6]:

increment_lambda(33)


# In[8]:

(lambda x: x+1)(34) # 이게 하이라이트야 쓰고 버려


# In[10]:

(lambda x,y: x**y)(5,5) 


# In[ ]:



