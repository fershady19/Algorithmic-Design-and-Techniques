"""
Task. Given two integers 𝑛 and 𝑚, output 𝐹𝑛 mod 𝑚 (that is, the remainder of 𝐹𝑛 when divided by 𝑚). Input Format. The input consists of two integers 𝑛 and 𝑚 given on the same line (separated by a space). Constraints. 1≤𝑛≤1018,2≤𝑚≤105.
Output Format. Output 𝐹𝑛 mod 𝑚.
"""

def fib(n, memo={}):
    if n == 0 or n == 1:
        return n
    try:
        return memo[n]
    except KeyError:
        result = fib(n-1, memo) + fib(n-2, memo)
        memo[n] = result
        return result


def get_period_len(m):
    pisa = [0,1,1]
    i = 3
    while 1:
        nxt = fib(i)%m
        if nxt == 0:
            nxt1 = fib(i+1)%m
            nxt2 = fib(i+2)%m
            if nxt1 == 1 and nxt2 == 1:
                break
        pisa.append(nxt)
        i += 1
    return len(pisa)


def pisano(n, m):
    if n < m:
        return fib(n)%m
    len_ = get_period_len(m)
    n = n%len_
    return fib(n)%m


in_ = [int(i) for i in input().split()]
print(pisano(in_[0], in_[1]))
