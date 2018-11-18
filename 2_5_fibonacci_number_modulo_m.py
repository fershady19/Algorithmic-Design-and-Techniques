"""
Task. Given two integers n and m, output Fn mod m (that is, the remainder of Fn when divided by m).
Input Format. The input consists of two integers n and m given on the same line (separated by a space).
Constraints. 1<=n<=1018,2<=m<=105.
Output Format. Output Fn mod m.
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
