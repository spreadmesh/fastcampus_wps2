
# coding: utf-8

# In[3]:

{
    "name": "장기수",
    "address": "..."
}


# In[37]:

user_list = [
    ["장기수", "서울"],
    ["울랄라", "대전"],
    ["샬랄라", "대구"],
    ["어허라", "부산"],
    ["장기철", "찍고"]
]

user_list[0][0]
# list의 list => dict의 list로 변경하기


# In[34]:

my_dict = {}
my_list = []

for i in user_list:
    # 이거슬 리스트에 너허야 하는데
    my_dict["name"] = i[0]
    my_dict["address"] = i[1]
    my_dict["어렵네"] = "dict 사용이 말야"
    my_list.append(my_dict)
    my_dict={}
    
my_list


# In[32]:

test_dict = [
    {"장기수", "주소1"},
    {"울랄라", "주소1"},
    {"샬랄라", "주소1"},
    {"어허라", "주소1"},
    {"장기철", "주소2"}
]

test_dict


# In[35]:

# 안수찬 강사님이 구현하신 방법
# 1. for 문을 돌리는 방법
user_dict_list = []

for user in user_list:
    name = user[0]
    address = user[1]
    user_dict = {
        "name": name,
        "address": address,
    }
    user_dict_list.append(user_dict)
    
user_dict_list


# In[41]:

user_list = [
    ["장기수", "서울"],
    ["울랄라", "대전"],
    ["샬랄라", "대구"],
    ["어허라", "부산"],
    ["장기철", "찍고"]
]

[
    {
        "name": user[0],
        "address": user[1],
    }
    for user
    in user_list
]


# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[69]:

with open("../../users.csv", "r") as f:
        data_list = [
            {
                "name": line.split(",")[0],
                "address": line.split(",")[1].replace("\n",""),
            }
            for line
            in f.readlines()
        ]
        
print(data_list[2])


# In[93]:

def preprocess(phonenumber):
    hangul_to_number_dict = {
        "공" : 0,
        "영" : 0,
        "일" : 1,
        "이" : 2,
        "삼" : 3,
        "사" : 4,
        "오" : 5,
        "육" : 6,
        "칠" : 7,
        "팔" : 8,
        "구" : 9,
        " " : "",
        "-" : "",
    }
    
    for key, value in hangul_to_number_dict.items():
        phonenumber = phonenumber.replace(key, str(value))
        
    return phonenumber
        
preprocess("공01-29일이-00공칠")


# In[98]:


with open("../phonenumber.txt", "r") as input_file:
    result = [
        #line.replace(hangul_to_number_dict()"일","1")
        preprocess(line.replace("\n", ""))
        for line
        in input_file.readlines()
    ]
    
print(result)


# In[97]:

# 선생님 코드
with open("../phonenumber.txt", "r") as input_file:
    with open("../phonenumber_proprocessed.txt", "w") as output_file:
        [
            output_file.write(
                preprocess(line.replace("\n", "")) + "\n"
            )
            
            for line
            in input_file.readlines()
        ]

