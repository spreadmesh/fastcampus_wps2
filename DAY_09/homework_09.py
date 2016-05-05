# list comprehension to rambda 

# list comprehension
MAX = 1000

not_prime_list = [
    j
    for i in range(2, int(MAX**0.5) + 1)  # i => 2, 3, 4, ..., 30,
    for j in range(i*2, MAX+1, i)  # j => i=2; 
]

a = list(set(not_prime_list))

prime_list = [
	i
	for i in range(2, MAX+1)
    if i not in not_prime_list
]

b = prime_list

##############################################################################

# lambda

MAX = int(input("소수를 구하는 프로그램입니다. MAX값을 입력하세요. : "))

output = list(map(lambda x: x, filter(lambda x: x not in sum(list(map(lambda i : list(map(lambda j : j, range(i*2, MAX+1, i))), range(2, int(MAX**0.5) + 1))),[]), range(2, MAX+1))))

print(output)


"""
답을 얻기 까지의 과정
1. 복습 - list comprehension > map, filter, reduce > lambda
2. list comprehension 분석 - 한 줄씩 변환을 시도 > 중첩된 for문에서 막힘 > lambda의 중첩에 대해서 공부 (http://caisbalderas.com/blog/iterating-with-python-lambdas/) 
3. 중첩된 list(map(lambda ... 을 이용하면 list in list 가 만들어져 조건확인에 사용이 어려움 > sum( iterable , [])이라는 방법을 확인하여 적용함 
"""
