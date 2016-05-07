
# coding: utf-8

# In[2]:

# 소수 구하기 ( prime Number )


# In[3]:

def get_prime_numbers(number):
# 1과 자기 자신으로만 나눌 수 있는 -> 1, 자신 말고 나눠지지 않으면 체크
    prime_number_list = [2]
    for i in range(3, number):
        check = 0
        for j in range(2,i-1):
            if i % j == 0: check = 1 # 나눠지면 체크
        if check == 0: prime_number_list.append(i)
    
    return prime_number_list


# In[4]:

output = get_prime_numbers(1000)
# [2, 3, 5, 7, 11, 13, ..., 997]
print(output)


# In[5]:

def is_prime(number):
    # 2부터 number-1 까지의 숫자로 각각 나눠서 체크해본다.
    for i in range(2, number):
        if (number % i == 0):
            return False
    return True


# In[6]:

def get_prime_numbers2(number):
    # number만큼 for 문을 돌면서,
    # 각각의 숫자가 소수인지/아닌지 체크를
    # 빈 리스트 하나 만들어서,
    # 소수면, => 빈 리스트에 추가하고
    # for 끝나는 시점에 빈 리스트를
    
    prime_numbers = []
    for i in range(2, number):
        if is_prime(i):
            prime_numbers.append(i)
    return prime_numbers


# In[7]:

get_prime_numbers2(100)


# In[8]:

for i in range(2,2):
    print(i)


# In[9]:

def is_prime_obtimized(number):
    # 2부터 number-1 까지의 숫자로 각각 나눠서 체크해본다.
    for i in range(2, int(number**0.5) + 1):
        if (number % i == 0):
            return False
    return True


# In[14]:

def get_prime_numbers_obtimized(number):
    # number만큼 for 문을 돌면서,
    # 각각의 숫자가 소수인지/아닌지 체크를
    # 빈 리스트 하나 만들어서,
    # 소수면, => 빈 리스트에 추가하고
    # for 끝나는 시점에 빈 리스트를
    
    prime_numbers = []
    for i in range(2, number):
        if is_prime_obtimized(i):
            prime_numbers.append(i)
    return prime_numbers


# In[11]:

get_prime_numbers_obtimized(100)


# In[15]:

import time

start_time = time.time()
get_prime_numbers_obtimized(30000)
end_time = time.time()
end_time - start_time



# In[13]:


start_time2 = time.time()
get_prime_numbers2(30000)
end_time2 = time.time()
end_time2 - start_time2


# In[ ]:



