
# coding: utf-8

# In[ ]:

name = "KIsu Jang"
age = 24


from IPython import embed
embed()


# In[ ]:

for i in range(3):
    a = i * 7
    b = i + 2
    c = a * b
    
    embed()


# In[ ]:

# 출력을　하기는　합니다．
# 다만，　print로　직접　하지는　않아요．
# 로그를 쌓는다 ( Log ) => logging


# In[2]:

import logging


# In[9]:

logging.warning("hello world")
# 주피터　노트북에서는　사용자한테는　안보여지고　서버？에　로그가　남는다．
# WARNNING:root:hello world


# In[8]:

# Error
# 실행　자체가　되지　않습니다．
# 문법　자체의　오류　＝＞ SyntaxError ( ParsingError )

if True
    print("hello world")
# SyntaxError는　안생기면　제일　좋다．


# In[10]:

# ３가지　이상의　Exception이　뜨도록


# In[19]:

"asdf".index(5)
2 + "기수"


# In[18]:

a


# In[17]:

list = [1,2,3]
list.index(4)


# In[21]:

with open("./not_exist_file", "r") as f:
    pass


# In[22]:

# Excption => 좋은거 => 일단 우리가　남이　의도하지　않은　방향대로　뭔가　（클래스，　함수，　객체　등）를　쓰고　있기


# In[ ]:




# In[ ]:



