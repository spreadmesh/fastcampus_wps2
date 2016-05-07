
# coding: utf-8

# In[23]:

# List, Dict

animals = ["강아지", "고양이", "이구아나", "물고기", "참새"]
my_informations = {"name": "spreadmesh", "phonenumber": "010-2912-0007","email":"spreadmesh@gmail.com"}


# In[4]:

for animal in animals:
    print(animal)


# In[11]:

for i in my_informations:
    print(i + " :", end="")
    print(" " +my_information[i])


# In[14]:

for my_information in my_informations.items():
    key, value = my_information
    print(key, value)


# In[16]:

for key, value in my_informations.items():
    print(key, value)


# In[22]:

animals = ['강아지', '고양이', '이구아나', '물고기', '참새']

# 하나씩 출력을 하는데,
# index 가 2번인 애는 "파이썬" 으로 변경하자.

for i in range(len(animals)):
    if i == 2:
        animals[i] = "파이썬"
    print(animals[i])


# In[26]:

animals = ['강아지', '고양이', '이구아나', '물고기', '참새']

for animal in animals:
    index = animals.index(animal)    
    if index == 2:
        animals[index] = "파이썬"
        
    print(animals[index])


# In[27]:

for something in enumerate(animals):
    print(something)


# In[28]:

for index, value in enumerate(animals):
    print(index)
    print(value)


# In[29]:

animals = ['강아지', '고양이', '이구아나', '물고기', '참새']

for index, value in enumerate(animals):
    if index == 2:
        animals[index] = "파이썬"
    print(animals[index])


# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:



