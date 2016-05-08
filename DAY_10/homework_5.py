## 5. 피보나치 수를 구하는 함수 구현하기
def fibonacci(num):
    if num == 0:
        return 0
    elif num == 1:
        return 1
    else:
        return fibonacci(num - 1) + fibonacci(num - 2)

print("fibonacci(2) = {}".format(fibonacci(2)))
print("fibonacci(3) = {}".format(fibonacci(3)))
print("fibonacci(4) = {}".format(fibonacci(4)))
print("fibonacci(5) = {}".format(fibonacci(5)))
