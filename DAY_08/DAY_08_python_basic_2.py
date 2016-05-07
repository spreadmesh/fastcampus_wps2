
# coding: utf-8

# In[2]:

# ./ => 현재 폴더
# ../ => 상위 폴더

# ./test.txt => 현재 폴더에 있는 test.txt
# ../test.txt => 상위 폴더에 있는 test.txt
# ../../test.txt => 상위 폴더의 상위 폴더에 있는 test.txt

f = open("../animals.txt", "r") # mode = "r" | "w" | "a" ( append )


# In[ ]:

# read, readline, readlines


# In[3]:

f.read()


# In[15]:

f = open("../animals.txt", "r") # mode = "r" | "w" | "a" ( append )


# In[14]:

f.readlines()


# In[18]:

f.readline()


# In[23]:

f = open("./animals.txt", "w")


# In[24]:

f.write("아 덥다\n")


# In[25]:

f.write("덥다 진짜.\n ")


# In[26]:

f.close()


# In[27]:

with open("./animals.txt", "w") as f:
    f.write("""with open("./animals.txt", "w") as f:""")


# In[ ]:




# In[ ]:



