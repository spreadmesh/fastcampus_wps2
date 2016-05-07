
# coding: utf-8

# In[14]:

# [1, 2, 3] => [1, 4, 9]

def power_each_list_ver(my_list):
    result = []
    
    for i in my_list:
        result.append(i ** 2)
     
    return result
        
        
        
    


# In[15]:

power_each_list_ver([1,2,3])


# In[12]:

# [1, 2, 3] => [1, 4, 9]

def power_each(*args):
    result = []
    
    for arg in args:
        result.append(arg * arg)
     
    return result
        
        
        
    


# In[13]:

power_each(1,2,3)


# In[ ]:




# In[16]:

def square(x):
    return x**2


# In[17]:

list(map(square, [1,2,3]))


# In[18]:

# map은 첫 번째 인자로 함수, 두 번째 인자로 리스트를 받아


# In[19]:

list(map(lambda x: x**2, [4,5,7,9]))


# In[21]:

numbers = list(range(1,11))


# In[23]:

list(filter(lambda x: x>5, numbers))


# In[26]:

import time

def sleeping_numbers(x):
    """
    1초 쉬고 제곱을 리턴
    """
    time.sleep(1)
    return x**2


# In[25]:

sleeping_numbers(1)


# In[31]:

map(sleeping_numbers, [5,6,7,8,0]) # 맵은 정보만 담겨있다.


# In[37]:

a = map(sleeping_numbers, [5,6,7,8,0])


# In[38]:

for i in a:
    print(i)


# In[39]:

# 정리
# Map => 모든 Elements => 새로운 List
# Filter => 모든 Elements => True 인 Element 만 새로운 List


# In[40]:

# Reduce
# 줄이는 애
# 하나만 남기는 애


# In[41]:

import functools


# In[42]:

# functools.reduce(. . .)


# In[43]:

# [10, 20, 30, 40, 50, 60]


# In[44]:

functools.reduce(lambda x,y: x+y, [10, 20, 30, 40])


# In[45]:

# max를 뽑는 경우 엄청 유용하겠네


# In[46]:

# [참일 때의 값] if [조건문] else [거짓일 때의 값]


# In[47]:

functools.reduce(lambda x,y: x if x>y else y, [5,4,6,3,8,2])


# In[ ]:




# In[49]:

awesome_list = [1,2, "장기수", {}, [], 4, 5]


# In[50]:

# Lambda Operator => 숫자인 애들만 제곱해서 새로운 리스트로 만드는거
isinstance(1, int)


# In[54]:

list(map(
        lambda x: x**2, 
        filter(
            lambda x: isinstance(x, int),
            awesome_list
        )
        )
     )


# In[57]:

[i**2 for i in range(10)]
# list comprehension => map + filter 가능


# In[58]:

list(map(lambda x: x**2, range(10)))


# In[61]:

[i**2 for i in range(10) if i**2 > 50]
# if로 filter가능


# In[ ]:




# In[62]:

# 1-100 까지 숫자 중에서 짝수인 애들의 제곱 리스트


# In[65]:

list(map(lambda x: x**2, filter(lambda x: x%2==0, range(1,101))))


# In[67]:

[i**2 for i in range(1,101) if i%2 == 0]


# In[ ]:




# In[1]:

# list comprehension 을 이용한 소수구하기


MAX = 1000

not_prime_list = [
    j
    for i in range(2, int(MAX**0.5) + 1)  # i => 2, 3, 4, ..., 30,
    for j in range(i*2, MAX+1, i)  # j => i=2; 
]

list(set(not_prime_list))
b
prime_list = [
    i
    for i in range(2, MAX+1)
    if i not in not_prime_list
]
prime_list




# In[ ]:




# In[5]:


awesome_list = [
    (i, j)
    for i in range(8)
    for j in range(4)
]

awesome_list



# In[ ]:

[ i for i in range(2, MAX) if i not in [ j for i in range(2, int(MAX**0.5) + 1) 
    for j in range(i*2, MAX, i) ]]


# In[ ]:

#[ j for i in range(2, int(MAX**0.5) + 1) for j in range(i*2, MAX, i) ]


# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:



