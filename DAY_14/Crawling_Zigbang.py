
# coding: utf-8

# In[1]:

import requests


# In[2]:

from bs4 import BeautifulSoup


# In[3]:

BASE_URL= "https://api.zigbang.com/v1/items?detail=true&item_ids=4601198&item_ids=4599175&item_ids=4508159&item_ids=4463473&item_ids=4413148&item_ids=4206525&item_ids=4592322&item_ids=4577103&item_ids=4571118&item_ids=4415510&item_ids=4605554&item_ids=4542176&item_ids=4505100&item_ids=4593590&item_ids=4603013&item_ids=4467689&item_ids=4564400&item_ids=4438426&item_ids=4416073&item_ids=4606928&item_ids=4599955&item_ids=4591357&item_ids=4596010&item_ids=4586828&item_ids=4571852&item_ids=4603701&item_ids=4516115&item_ids=3959019&item_ids=4578990&item_ids=4520711&item_ids=4530634&item_ids=4587412&item_ids=4489421&item_ids=4593822&item_ids=4505885&item_ids=4435512&item_ids=4594054&item_ids=4586430&item_ids=4531701&item_ids=4583946&item_ids=4454577&item_ids=4539717&item_ids=4589612&item_ids=4360296&item_ids=4559931&item_ids=4506592&item_ids=4529295&item_ids=4505755&item_ids=4356408&item_ids=4582180&item_ids=4588134&item_ids=4548101&item_ids=4591774&item_ids=4448746&item_ids=4241248&item_ids=4497166&item_ids=4344909&item_ids=4507030&item_ids=4355236&item_ids=4552754"


# In[4]:

reponse = requests.get(BASE_URL)


# In[5]:

reponse.status_code 


# In[7]:

import json


# In[8]:

room_infomation = json.loads(reponse.text)


# In[13]:

room_infomation["items"][0]["item"]["agent_address1"]


# In[14]:

import pandas as pd

df = pd.DataFrame(columns=["address", "deposit", "rent"])


# In[18]:

# 내꺼 무슨 문제로 안 긁어와져서 선생님이 긁으신거 가져옴

for room_id in range(4461545, 4461545+100):
    BASE_URL = "https://api.zigbang.com/v1/items?detail=true&item_ids=" + str(room_id)
    response = requests.get(BASE_URL)
    room_inforation = json.loads(response.text)
    
    try:
        address = room_inforation["items"][0]["item"]["agent_address1"]
        deposit = room_inforation["items"][0]["item"]["deposit"]
        rent = room_inforation["items"][0]["item"]["rent"]
        print((address, deposit, rent))
        df.loc[len(df)] = [address, int(deposit), int(rent)]
    except:
        pass
    
        


# In[19]:

df


# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:



