
# coding: utf-8

# In[1]:

# 크롤링 숙제


# In[2]:

import requests


# In[3]:

from bs4 import BeautifulSoup


# In[4]:

BASE_URL = "https://search.naver.com/search.naver?where=post&sm=tab_jum&ie=utf8&query=%EB%8D%B0%EC%9D%B4%ED%8A%B8+%EC%9E%A5%EC%86%8C+%EC%B6%94%EC%B2%9C"


# In[5]:

reponse = requests.get(BASE_URL)


# In[9]:

reponse.status_code


# In[16]:

get_ipython().magic('pinfo reponse.content')


# In[ ]:




# In[17]:

get_ipython().magic('pinfo reponse.text')


# In[18]:

DOM = BeautifulSoup(reponse.content, "html.parser")


# In[19]:

DOM


# In[21]:

post_elements = DOM.select("li.sh_blog_top")


# In[23]:

post_elements[0]


# In[29]:

post_elements[0].select_one("a.sh_blog_title")


# In[30]:

post_elements[0].select("a.sh_blog_title")


# In[31]:

for post_element in post_elements:
    title_element = post_element.select_one("a.sh_blog_title")
    title = title_element.text
    url = title_element.get("href")
    print((title, url))


# In[32]:

import pandas as pd


# In[33]:

df = pd.DataFrame(columns=["title","url"])


# In[34]:

df


# In[36]:

for post_element in post_elements:
    title_element = post_element.select_one("a.sh_blog_title")
    title = title_element.text
    url = title_element.get("href")
#    print((title, url))
    df.loc[len(df)] = [title, url]


# In[37]:

df


# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:



