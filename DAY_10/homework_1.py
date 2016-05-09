import functools
## 1. lambda operator 를 이용한 소수 구하기 구현
"""
해결 과정
 a. prime 부터 만들자 > filter > 조건 부분은 일단 간단하게 구현해보고 진행
 b. noprimes 만들자 > 잘 안되네... for문 두 개 > 간단한 것 부터 구현 i = 1~4, j = 1~5
		print(list(map(lambda i: list(map(lambda j: i*j, range(1,5))), range(1,6))))
 c. noprimes OK > 전체를 완성해서 primes를 출력해보자 > 이상한 값이 나온다. 왜지? > 확인해보니
		noprime 값이 list 안에 list들이 중첩되어 있는 구조구나... 어떡하지?
 d-1. noprimes를 for문 2개로 전부 읽어서 빈 리스트에 appending? Oh... No....
 d-2. 찾아보니 sum( list_of_lists, [] )를 사용하여 단일 list로 만들 수 있다.
 e. 다시 결과 확인 > 성공적.
"""

MAX = 1000
#noprimes = [
#	j
#	for i
#	in range(2, int(MAX ** 0.5) + 1)
#	for j
#	in range(i*2, MAX, i)
#]
#primes = [
#	x
#	for x
#	in range(2, MAX)
#	if x not in noprimes
#]
noprimes = list(map(
    lambda i: list(map(
        lambda j: j, 
        range(i*2, MAX, i))), 
    range(2, int(MAX ** 0.5) + 1)))

noprimes = functools.reduce(
    lambda x, y: x+y, 
    noprimes
    )

primes = list(filter(lambda x:x not in noprimes, range(2, MAX)))

print(primes)

