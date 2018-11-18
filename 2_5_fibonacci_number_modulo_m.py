"""
Task. Given two integers n and m, output Fn mod m (that is, the remainder of Fn when divided by m).
Input Format. The input consists of two integers n and m given on the same line (separated by a space).
Constraints. 1<=n<=1018,2<=m<=105.
Output Format. Output Fn mod m.
"""

def pisano(m):
    period = 0
    a, b, = 0, 1
    c = 0
    if m < 2:
        return 1
    else:
        while not(a == 0 and c == 1): 
            c = (a + b) % m
            a = b
            b = c
            period += 1
        return period


def fib(n):
    fib_n = 0
    a, b = 0, 1
    if n == 0 or n == 1:
        return n
    else:
        for _ in range(1,n):
           fib_n = a + b
           a = b
           b = fib_n
        return fib_n


def fib_mod_m(n, m):
    n = n % pisano(m)
    return fib(n) % m


in_ = [int(i) for i in input().split()]
print(fib_mod_m(in_[0], in_[1]))