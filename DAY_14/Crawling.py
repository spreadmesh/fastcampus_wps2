
# coding: utf-8

# In[ ]:

# Crawling


# In[ ]:

# Crawling => "데이터를 모으는 과정" ... => Google bot


# In[ ]:

# 웹 문서 ( HTML ) Crawling

# 1. Crawling => 모든 정보를 쌩으로 다 가져오는 작업 ( 의미 X )
    # 2. Scraping => 링크 + 어떤 특정 정보를 걸러내는 거 
# 3. Parsing => 의미있는 정보를 뽑는 과정


# In[ ]:

# 1. Crawling => urllib, urllib2, ..., requests ( HTTP Request/Response )
# 2. Scraping => 
#   2.1. 직접 Crawling 한 결과 => a 태그를 찾아서 => 다시 클롤링
#   2.2. Scrapy
# 3. Parsing =>
#   3.1. Regular Expression ( 정규 표현식 )
#   3.2. BeautifulSoup
#   3.3. lxml ( xml )

# Crawling => requests
# Parsing => BeautifulSoup

# Framework => 기능들의 집합 ( 라이브러리 집합 ) => "틀" => 목표
# Library => 기능들


# In[ ]:

import requests


# In[2]:

from bs4 import BeautifulSoup


# In[3]:

BASE_URL= "https://search.naver.com/search.naver?where=post&sm=tab_jum&ie=utf8&query=%EC%9D%B4%EC%83%89%EB%8D%B0%EC%9D%B4%ED%8A%B8"


# In[4]:

# 1. requests
#      Crawling
#     Requests : HTTP for Humans
reponse = requests.get(BASE_URL)


# In[6]:

reponse.headers


# In[8]:

reponse.status_code 
# 2XX => Successful ( 200 => OK)
# 3XX => Redirection ( 200 => OK)
# 4XX => Failed ( 403 => forbbiden)


# In[9]:

reponse.content


# In[10]:

reponse.text


# In[11]:

dom = BeautifulSoup(reponse.content, "html.parser")
# dom ( 돔 ) => Document Object Model
# html > div > h1 > p > ul > li > ...


# In[12]:

get_ipython().magic('pinfo BeautifulSoup')


# In[13]:

dom


# In[14]:

get_ipython().set_next_input('post_elements = dom.select');get_ipython().magic('pinfo dom.select')


# In[15]:

post_elements = dom.select("li.sh_blog_top")


# In[16]:

len(post_elements)


# In[22]:

post_element = post_elements[0]
post_element

title_element = post_element.select_one("a.sh_blog_title")


# In[21]:

title_element


# In[23]:

title_element


# In[24]:

title_element.text


# In[25]:

title_element.get("href")


# In[26]:

for post_element in post_elements:
    title_element = post_element.select_one("a.sh_blog_title")
    title = title_element.get("title")
    url = title_element.get("href")
    print((title, url))


# In[27]:

import pandas as pd


# In[32]:

df = pd.DataFrame(columns=["title", "url"])


# In[33]:

df


# In[34]:

for post_element in post_elements:
    title_element = post_element.select_one("a.sh_blog_title")
    title = title_element.text
    url = title_element.get("href")
    
    df.loc[len(df)] = [title, url]


# In[35]:

df


# In[36]:

df.to_csv("2color_data_course.csv")


# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:



