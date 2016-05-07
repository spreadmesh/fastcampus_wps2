
# coding: utf-8

# In[1]:

# 1. 1~100 까지의 숫자 중에서 3과 5로 나누어 떨어지는 수를 저장하는 List를 만들어 주세요.
# 2. 3의 배수가 입력되면 fast, 5의 배수가 입력되면 campus, 15의 배수가 입력되면 fastcampus 출력


# In[ ]:




# In[20]:

num = int(input("값을 입력하세요 : "))

if num % 3 == 0 and num % 5 == 0:
    print("fastcampus")
elif num % 3 == 0:
    print("fast")
elif num % 5 == 0:
    print("campus")
else:
    print("3이나 5의 배수가 아닙니다.")



# In[23]:

num = int(input("값을 입력하세요 : "))

result=""
if num % 3 == 0:
    result += "fast"
if num % 5 == 0:
    result += "campus"
    
print(result)


# In[ ]:

list(filter(
    lambda x : x%3==0 or x%5==0,
    range(1,100+1)
))


# In[ ]:

list(filter(
    lambda x : x%3==0 or x%5==0,
    range(1,100+1)
))


# In[17]:

[i for i in range(1,100+1) if i%15==0]


# In[ ]:

my_list=list(range(0,100))
for i in range(len(my_list)):
    if i % 15 ==0:
        my_list[i] = "fastcampus"
    if i % 5 ==0:
        my_list[i] = "campus"
    if i % 3 ==0:
        my_list[i] = "fast"
        
print(my_list)
        
# 으아아아아아아 ㅠㅠ


# In[ ]:

result = []

for i in range(1,100+1):
    word = ""
    if i % 3 == 0:
        word += "fast"
    if i % 5 == 0:
        word += "campus"
    result.append(word)

print(result)


# In[48]:

fast_list = [
    "fast" if x % 3 == 0 else ""
    for x
    in range(1,100+1)   
]


campus_list = [
    "campus" if x % 5 == 0 else ""
    for x
    in range(1,100+1)   
]


# In[ ]:

[
    fast_list[i] + campus_list[i]
    for i
    in range(100)
]


# In[ ]:




# In[2]:

# 전체카운트 3의배수의3 거기에포함될텍스트 5의배수의5, 거기에포함될텍스트
# something(100, 3, "fast", 5, "campus")
# something(100, [(3, "fast"), (5, "campus"), (7, "wps"), (9, "dss")]) 의 확장성이 숙제


# In[13]:

def something(count, first_number, first_word, second_number, second_word):
    first_list = [
        first_word if x % first_number == 0 else ""
        for x
        in range(1,count+1)   
    ]

    second_list = [
        second_word if x % second_number == 0 else ""
        for x
        in range(1,count+1)   
    ]
    
    return [
        first_list[i] + second_list[i]
        for i
        in range(count)
    ]

something(10, 2, "fast", 5, "campus")


# In[ ]:

# palindrom
# 기러기
# 소주만병만주소
# is_palindrom("기러기") => True
# is_palindrom("패캠") => False


# In[25]:

def is_palindrom(word):
    reversed_word = ""
    for i in range(len(word)-1,-1,-1):
        reversed_word += word[i]
        
    return True if word == reversed_word else False


# In[29]:

is_palindrom("기기러기")


# In[24]:

for i in range(2,-1,-1):
    
    print(i)


# In[30]:

# 선생님 풀이
# "정의대로 푸는게 가장 쉬운 방법이다."
# palindrom의 정의 => 문자열을 받아서, 뒤집었을때 같으면 True 틀리면 False


# In[41]:

def reverse(word):
    """
    reversed_word = ""
    for i in range(len(word)):
        reversed_word += word[len(word)-1-i]
    return reversed_word
    """
    return word[::-1]

def is_palindrom(word):
    return word == reverse(word)


# In[ ]:

# len("기러기")

# "기러기"[0] == "기러기"[3-1]
# "기러기"[0+1] == "기러기"[3-1-1]
# "기러기"[0+2] == "기러기"[3-1-2]


# In[44]:

is_palindrom("기러기")


# In[40]:

"기러기는기러디다"[::-1]


# In[ ]:




# In[45]:

def is_palindrom(word):
    return word == word[::-1]


# In[47]:

(lambda x: x == x[::-1])("기러기")

