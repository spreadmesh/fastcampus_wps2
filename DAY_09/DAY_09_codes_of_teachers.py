
# coding: utf-8

# In[20]:

# Map => 모든 Elements => 새로운 List
# Filter => 모든 Elements => True 인 Element 만 새로운 List


# In[21]:

# Reduce
# 줄이는 애
# 하나만 남기는 애


# In[22]:

import functools


# In[23]:

# functools.reduce(...)


# In[24]:

# [10, 20, 30, 40, 50, 60]


# In[25]:

functools.reduce(lambda x,y: x+y, [10, 20, 30, 40])


# In[26]:

def sum(x, y):
    print((x, y))
    return x + y


# In[27]:

functools.reduce(sum, [10, 20, 30, 40, 50])


# In[30]:

# 리스트에서 최대값을 뽑는 함수


def max(numbers):
    max_number = numbers[0]
    for number in numbers:
        if number > max_number:
            max_number = number
    return max_number


# In[31]:

max([1, 9, 2, 3, 7, 11, 4])


# In[37]:

functools.reduce(lambda x,y: x if x>y else y, [1, 9, 2, 3, 7, 11, 4])


# In[33]:

3 if True else 5


# In[34]:

3 if False else 5


# In[35]:

# [참일 때의 값] if [조건문] else [거짓일때의 값]


# In[38]:

awesome_list = [1, 2, "안수찬", {}, [], 4, 5]


# In[40]:

# Lambda Operator => 숫자인 애들만 제곱해서 새로운 리스트로 만드는거
# [1, 4, 16, 25]

isinstance(1, int)


# In[44]:

list(map(
    lambda x: x**2, 
    filter(
        lambda x: isinstance(x, int),
        awesome_list
    )
))


# In[ ]:




# In[ ]:




# In[ ]:




# In[51]:

[i**2 for i in range(10) if i > 5]


# In[49]:

list(map(lambda x: x**2, range(10)))


# In[52]:

# 1-100 까지 숫자 중에서 짝수인 애들의 제곱 리스트


# In[57]:

[i**2 for i in range(1, 100+1) if i%2 == 0]


# In[58]:

awesome_list = [i for i in range(0, 9+1)]


# In[59]:

awesome_list


# In[61]:

filter(lambda x: x>5, awesome_list)


a = map(
    lambda x: x**2, 
    filter(lambda x: x>5, awesome_list)
)


# In[62]:

list(a)


# In[63]:

[i**2 for i in range(0, 9+1) if i>5]


# In[65]:

# 소수가 아닌 애들
# 1~n - 소수가 아닌 애들


# In[78]:

MAX = 1000

not_prime_list = [
    j
    for i in range(2, int(MAX**0.5) + 1)  # i => 2, 3, 4, ..., 30,
    for j in range(i*2, MAX+1, i)  # j => i=2; 
]

list(set(not_prime_list))

prime_list = [
    i
    for i in range(2, MAX+1)
    if i not in not_prime_list
]
prime_list


# In[79]:

awesome_list = [
    (i, j)
    for i in range(8)
    for j in range(4)
]

awesome_list


# In[ ]:




# In[ ]:




# In[ ]:



