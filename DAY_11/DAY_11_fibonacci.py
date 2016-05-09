
# coding: utf-8

# In[1]:

# In[88]:

def fibonacci(n):
    # 현재값(i), 이전의 피보나치값(i-1) => i+1 
    prev_n, cur_n = 0, 1
    i=1
    
    while i<n:
        # temp_n 가 필요없이 바로 관계가 있는 2개의 값을 바꿀 수 있습니다.
        cur_n, prev_n = cur_n + prev_n, cur_n  
        i += 1
    return cur_n


# 재귀 함수 ( recursive function )
# f(n) = f(n-1) + f(n-2)


# In[89]:

fibonacci(7)


# In[2]:

# In[91]:

def fibonacci_re(x):
    if x <= 0:
        return 0
    if x == 1:
        return 1
    return fibonacci_re(x-1) + fibonacci_re(x-2)


# In[97]:

fibonacci_re(5)


# In[3]:

# In[134]:

#  1 2 3 4 5 6 7 8   9.... 메모의 길이
# [0 1 2 3 4 5 6 7   8 ...] 
# [0,1,1,2,3,5,8,13,21....] 피보나치 수열의 결과값
memo = []
@get_timer
def fibonacci_dp(x):
    if x <= 0:
        return 0
    if x == 1:
        return 1
    if len(memo)-1 >= x:
        return memo[x]
    if len(memo)-1 < x:
        new_number = fibonacci_dp(x-1) + fibonacci_dp(x-2)
        memo.append(new_number)
        return new_number

fibonacci_dp(2)


# In[4]:

# In[137]:

# 1. 2, 3 각각의 시간을 측정해볼게요. => 측정하는 함수
# 1-100 까지의 피보나치 수열을 구하는 시간

[fibonacci(i) for i in range(20)]

import time






# In[5]:

print(fibonacci_re(20))


# In[6]:

def get_timer(function, n):
    import time
    start_time = time.time()
    function(n)
    end_time = time.time()
    
    return end_time - start_time
    


# In[7]:

get_timer(fibonacci, 10)


# In[8]:

get_timer(fibonacci_re, 10)


# In[9]:

get_timer(fibonacci_dp, 10)


# In[10]:

# fibonacci 그냥 알아서 타이머가 실행되면 좋겠네
# decorator


# In[11]:

# 함수를입력받아 => 새로운 함수를 리턴하는 함수

def get_timer(function):
    def wrapper(*arg, **kwargs):
        start_time = time.time()
        result = function(*arg, **kwargs)
        end_time = time.time()
        print("{time}s 초 걸렸습니다.".format(time=end_time-start_time))
        return result
    return wrapper


# In[32]:

#@get_timer
@before_execute
def fibonacci_re(x):
    if x <= 0:
        return 0
    if x == 1:
        return 1
    return fibonacci_re(x-1) + fibonacci_re(x-2)


# In[17]:

fibonacci_dp(5)


# In[85]:

# @before_execute => "_________ 함수를 실행을 시작합니다."
# @after_execute => " _________함수 실행을 종료합니다."
# @ timer => " ____________s 초 걸렸습니다."

def timer(function):
    def wrapper(*arg, **kwargs):
        start_time = time.time()
        result = function(*arg, **kwargs)
        end_time = time.time()
        print("{name}을 실행하는데 {time}s 초 걸렸습니다.".format(name=function.__name__, time=end_time-start_time))
        return result
    return wrapper

def before_execute(function):
    def wrapper(*arg, **kwargs):
        print("{name} 함수를 실행합니다.".format(name=function.__name__))
        return function(*arg, **kwargs)
    return wrapper

def after_execute(function):
    def wrapper(*arg, **kwargs):
        result = function(*arg, **kwargs)
        print("{name} 함수를 실행합니다.".format(name=function.__name__))
        return result
    return wrapper


# In[89]:

@after_execute
@before_execute
def my_func(n):
    sum = 0
    for i in range(n+1):
        sum += i
    
    print("This is something")
    return sum
        
my_func(10)


# In[108]:

@bold
@italic
def introduce(name, course):
    return "안녕하세요, 저는 {name}입니다. {course} 에서 공부하고 있습니다.".format(
        name=name,
        course=course,
    )
print(introduce("장기수", "훌랄라"))


# In[107]:

def bold(function):
    def wrapper(*args, **kwargs):
        
        return "</b>" + function(*args, **kwargs) + "</b>"
    return wrapper

def italic(function):
    def wrapper(*args, **kwargs):
        
        return "</i>" + function(*args, **kwargs) + "</i>"
    return wrapper


# In[ ]:




# In[ ]:



