
# coding: utf-8

# In[2]:

class Timer():
    
    def __init__(self, function):
        self.function = function


# In[5]:

@Timer
def print_hello():
    print("hello world")

# 함수와 클래스 구현이 100% 동일한 예제이다.
# print_hello = Timer(print_hello) # Timer class => Timer object

print_hello() # 이건 안돼


# In[ ]:




# In[7]:

class HelloWorld():
    
    def __init__(self):
        print("init")
        
    def __call__(self):    # 객체가 함수처럼 호출되면, `self()` 될 때, 실행된다.
        print("hello world")


# In[9]:

helloworld = HelloWorld()


# In[10]:

helloworld()


# In[27]:

# Memoization, 기존의 결과값을 어딘가에 저장을 해서
# Factorial ( n! = n * (n-1) * ... * 2 * 1 ) 을 함수로 구현
class YouShouldInputPositiveNumber(Exception):

    def __init__(self,n):
        self.n = n
               
    def __str__(self):
        print( "{n} 값이 이상한데?".format(n=self.n))


result = {}

def factorial(n):
    if n < 1:
        raise YouShouldInputPositiveNumber(n):
    if n == 1:
        result[n] = n
        return 1
    result[n] = n * factorial(n-1)
    return n * factorial(n-1)
        



# In[21]:

factorial(5)


# In[22]:

result


# In[28]:

# result = { 1: 1, 2: 2, 3: 6, 4: 24, 5: 120, 6: 720}


# In[31]:

cache = {}
def factorial_for_class(n):
    if n <= 1:
        result = cache[n] = 1
        return result
    
    if n in cache:
        return cache[n]
    
    result = n *  factorial_for_class(n-1)
    cache[n] = result
    return result


# student = Student()
# student() __call__
# student => __str__


# In[56]:

factorial_for_class(5)
cache

tmp = [
    "{key} == {value}".format(key=key, value=value)
    for key, value
    in cache.items()
]

tmp


# In[50]:

class Factorial():
    def __init__(self):
        self.cache = {}
    
    def __call__(self, n):
        
        if n <= 1:
            result = self.cache[n] = 1
            return result

        if n in self.cache:
            return self.cache[n]

        result = n *  self.__call__(n-1)
        self.cache[n] = result
        return result
    
    def __str__(self):
        return "\n".join([
                "{key}! == {value}".format(key=key, value=value)
                for key, value
                in self.cache.items()
            ])
        


# student = Student()
# student() __call__
# student => __str__


# In[51]:

facto = Factorial()
facto(5)
facto.cache
print(facto)

