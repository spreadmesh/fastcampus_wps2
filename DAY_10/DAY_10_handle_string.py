
# coding: utf-8

# In[1]:

# "패스트캠퍼스 스쿨 과정은 참 좋다"
# => ["패스트캠퍼스", "스쿨",  "과정은", "참", "좋다"]


# In[26]:

def word_split(sentence):
    output = []
    buf=""
    for i in sentence:
        
        if i != ' ':
            buf += i
        else:
            output.append(buf)
            buf=""
        
    return output

#def word_split(sentence, seperate):
  #  pass


# In[28]:

word_split("패스트캠퍼스 스쿨 과정은 참 좋다")
# 맨 마지막에는 스페이스가 없잖아... 어쩔까


# In[57]:

# by 안수찬 강사님
def word_split_by_an(sentence, seperate=' '):
    # 앞에서 부터 한 글자 한 글자 읽으면서 => " "(스페이스)가 나올 때 까지 기다렸다가,
    # 이게나오면 모아뒀던 단어들을 리스트에 추가한다.
    
    word_list = []
    word = ""
    
    # for i in range(len(sentence)):
    for char in sentence:
        if char == seperate:
            word_list.append(word)
            word = " "
        else:
            word += char
    #이 시점에서 word 가 비어있지 않은 상태
    if word != "":
        word_list.append(word)
        
    return word_list



# In[ ]:




# In[52]:

word_split_by_an("패스트캠퍼스 스쿨 과정은 참 좋다")


# In[54]:

# word_split => 문장을 받아 단어 리스트
# word_join   => 단어 리스트를 받아서 문장으로 만드는


# In[56]:

def word_join(word_list, seperate=' '):
    sentence=''
    
    for word in word_list:
        sentence += word
        sentence += seperate
    
        
    return sentence


# In[59]:

word_join(['패스트캠퍼스', ' 스쿨', ' 과정은', ' 참', ' 좋다'])


# In[ ]:




# In[62]:

word_list =  "패스트캠퍼스는 참 좋다   ".split(" ")
print(word_list)


# In[64]:

[word for word in word_list if not word == ""]
# 전처리에 참 좋구나


# In[66]:

# word_join(문자 리스트, 구분자)
" ".join(["패스트캠퍼스", "참", "좋구나"])


# In[68]:

"****".join(["패스트캠퍼스", "참", "좋구나"])


# In[70]:

# word_replace
"패스트캠퍼스".replace("패스트", "Fast")


# In[ ]:

def word_replace(word, before, after):
    

