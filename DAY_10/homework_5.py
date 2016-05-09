## 5. 피보나치 수를 구하는 함수 구현하기
def fibonacci(num):
    if num == 0:
        return 0
    elif num == 1:
        return 1
    else:
        return fibonacci(num - 1) + fibonacci(num - 2)

# print("fibonacci(2) = {}".format(fibonacci(2)))
# print("fibonacci(3) = {}".format(fibonacci(3)))
# print("fibonacci(4) = {}".format(fibonacci(4)))
# print("fibonacci(5) = {}".format(fibonacci(5)))

fib_list = [0, 1]
def fibonacci_dp(x):
    if x <= 0:
        return 0
    if x == 1:
        return 1
    if len(fib_list)-1 >= x:
        return memo[x]
    if len(fib_list)-1 < x:
        new_number = fibonacci_dp(x - 1) + fibonacci_dp(x - 2)
        fib_list.append(new_number)
        return new_number

