
# coding: utf-8

# In[1]:

import requests


# In[2]:

from bs4 import BeautifulSoup


# In[23]:

BASE_URL = "https://search.naver.com/search.naver?where=post&sm=tab_pge&query=클래스팅&st=sim&date_option=0&date_from=&date_to=&dup_remove=1&post_blogurl=&post_blogurl_without=&srchby=all&nso=&ie=utf8&start="


# In[31]:

response_list = [                                               # 이 작업을 할 때 random하게 sleep을 추가
    requests.get(BASE_URL + str(i *10 + 1))
    for i
    in range(10)
]


# In[30]:

response_list[0].status_code


# In[15]:

# DOM = BeautifulSoup(response.content, "html.parser")
DOM_list = [
    BeautifulSoup(response_list[i].content, "html.parser")
    for i
    in range(10)
]


# In[16]:

import pandas as pd


# In[17]:

df = pd.DataFrame(columns=["title", "url"])


# In[20]:

DOM_list[0].select("li.sh_blog_top")


# In[34]:

for i in range(10):
    for j in range(10):
        title = DOM_list[i].select("li.sh_blog_top")[j].select_one("a.sh_blog_title").text
        url = DOM_list[i].select("li.sh_blog_top")[j].select_one("a.sh_blog_title").get("href")
        print((title,url))
        df.loc[len(df)] = [title, url]


# In[33]:

df


# In[ ]:




# In[ ]:




# In[ ]:




# In[47]:

df


# In[ ]:

for post_elements 


# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:



