class Fibonacci_dp():
    
    def __init__(self):
        self.cache = {}

    def __call__(self, n):
        
        if n <= 0:
            result = self.cache[n] = 0
            return result
        if n == 1:
            result = self.cache[n] = 1
            return result
        if n in self.cache:
            return self.cache[n]
        if len(self.cache)-1 >= n:
            result = self.cache[n] = n
            return result
        if len(self.cache)-1 < n:
            result = self.__call__(n-1) + self.__call__(n-2)
            self.cache[n] = result
            return result

    def __str__(self):
        return "\n".join([
            "{key}번째 == {value}".format(key=key, value=value)
            for key, value
            in self.cache.items()
        ])

fib = Fibonacci_dp()
fib(5)

print(fib)
