
# coding: utf-8

# In[1]:

# Exception Handling
# 예외를 처리하는 방법 => NameError, FileNotFoundError, AttributeError, ...

# 우리가 직접 예외를 만드는 방법 ( FibonacciShouldGetPositiveNumberError => 우리만의 예외 )


# In[17]:

def append_string_to_hello(string):
    # 예외처리가 가능한 장소
    try :
        return "hello, " + string
    except TypeError as err: # err = 파이썬　내부적으로　만들어진　예외　객체를　err 변수로　부른다．
        print("send_sms")
        return err
    finally:
        print("어쨌든　끝남")


# In[19]:

append_string_to_hello("world")


# In[5]:

append_string_to_hello("python")


# In[7]:

awesome_list = ["world", "python", "programming", 5736, "fastcampus"]


# In[13]:

for awesome in awesome_list:
    # 예외처리가 가능한 장소 (1)
    print(append_string_to_hello(awesome))


# In[18]:

for awesome in awesome_list:
    # 예외처리가 가능한 장소 (1)
    print(append_string_to_hello(awesome))


# In[ ]:




# In[14]:

def fib(n):
    if n < 0:
#        error = FibonacciShouldNotHaveNagativeNumberError()
#        raise err
            raise FibonacciShouldNotHaveNagativeNumberError(n)
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fib(n-1) + fib(n-2)


# In[15]:

fib(5)


# In[16]:

# Exception Class

class FibonacciShouldNotHaveNagativeNumberError(Exception):

    def __init__(self, n):
        self.n = n
    
    def __str__(self):
        return "피보나치 수열은 index 값으로 양수를 받아야 합니다. ( 입력받은 값: {n} )".format(n=self.n)
        


# In[17]:

fib(-1)


# In[ ]:

# 예외처리를 포함하여，
# factorial(n) 함수를 구현하세요. n! = n * (n-1) * ... * 2 * 1


# In[37]:

def factorial(n):
    if n <=0:
        raise FactorialShouldNotHaveNagativeNumberError(n)
    if n == 1:
        return 1
    return n*factorial(n-1)


# In[40]:

factorial(0)


# In[39]:

class FactorialShouldNotHaveNagativeNumberError(Exception):
    def __init__(self, n):
        self.n = n
    def __str__(self):
        return "factorial function should get positive index. ( input: {n} )".format(n=self.n)

    


# In[ ]:



