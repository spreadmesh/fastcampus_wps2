
# coding: utf-8

# In[27]:

import time
class Timer():
    
    def __init__(self, function):
        self.function = function
    
    def __call__(self, *args, **kwargs):
        start_time = time.time()
        result = self.function(*args, **kwargs)
        end_time = time.time()
        print("{time} 초 걸렸습니다.".format(time=end_time - start_time))
        return result

@Timer
def print_hello(name= "world"):
    print("hello, " + name)
    
print_hello()

