import functools

def make_fib_to_n_times(fib_num):
    """
    fibonacci 리스트 생성 
    """
    i = 0
    while fib[i] < fib_num:
        fib.append(fib[i] + fib[i+1])
        i += 1


# 변수 초기화
fib = [0, 1]
fib_num = int(input("자애로운 자여, 몇 명이나 먹이려고 하는고? : "))
result = 0

make_fib_to_n_times(fib_num)

if fib_num in fib:
    result = fib[fib.index(fib[len(fib)-1])-2]
else: 
    n = fib_num
    data = []
    index_list = []

    if n not in fib: # 리스트에 있니?
        while n not in fib: # 없으면 입력 받은 값보다 바로 작은 피보나치 수 찾아봐 12받으면 8을 찾아
            n -= 1 # 찾아졌어? 그러면 리스트에 넣자

        data.append(n)
        i = fib.index(n)-1
        index_list.append(i)
        while functools.reduce(lambda x, y: x+y, data) != fib_num and i > 0: # 담아둔게 입력값과 다르고 i가 0보다 큰동안
            if functools.reduce(lambda x, y: x+y, data) + fib[i] <= fib_num:
                data.append(fib[i])
                index_list.append(i-1)
            i -= 1

    for i in index_list:
        result += fib[i]

print("그렇다면 {result}마리를 시키거라. 능히 {fib_num}명을 먹이는데 부족함이 없느니라.".format(result=result, fib_num=fib_num))
