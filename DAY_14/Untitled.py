
# coding: utf-8

# In[21]:

def get_infomation(filename):
    with open(filename, "r") as f:
        return f.read()


# In[22]:

info_file = get_infomation("../../info.csv")
informations = info_file.split("\n")

# information = f.readlines()


# In[23]:

informations


# In[28]:

def preprocess(infomation):
    return infomation[:-7] + "*" * 7

assert preprocess("안수찬, 940223-1704201") == "안수찬, 940223-*******"
assert preprocess("안사, 940223-1704215") == "안사, 940223-*******"


# In[29]:

[
    preprocess(information)
    for information
    in informations
]


# In[30]:

#정규표현식 ( = Regular Expression; Regex )
# 기본 원리 => 다 적용할 수 있습니다. ( 근데 기본 원리가 많음)

info_file


# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:



