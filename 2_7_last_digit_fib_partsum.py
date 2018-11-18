"""
Task. Given two non-negative integers m and n, where m <= n, find the last digit of the sum Fm + Fm+1 + ···+Fn.
Input Format. The input consists of two non-negative integers m and n separated by a space.
Constraints. 0 <= m <= n <= 1018.
Output Format. Output the last digit of Fm + Fm+1 + · · · + Fn.
"""

def last_digit_fib(n, memo={}):
    if n == 0 or n == 1:
        return n
    try:
        return memo[n]
    except KeyError:
        result = (last_digit_fib(n-1, memo)
                  +last_digit_fib(n-2, memo))%10
        memo[n] = result
        return result


def last_digit_fib_partsum(m,n):
    m %= 60
    n %= 60
    n += 60
    sum_ = 0
    for i in range(m, n+1):
        sum_ += last_digit_fib(i)
        sum_ %= 10
    return sum_


in_ = [int(i) for i in input().split()]
print(last_digit_fib_partsum(in_[0], in_[1]))
