"""
Task. Given two non-negative integers 𝑚 and 𝑛, where 𝑚 ≤ 𝑛, find the last digit of the sum 𝐹𝑚 + 𝐹𝑚+1 + ···+𝐹𝑛.
Input Format. The input consists of two non-negative integers 𝑚 and 𝑛 separated by a space. Constraints. 0 ≤ 𝑚 ≤ 𝑛 ≤ 1018.
Output Format. Output the last digit of 𝐹𝑚 + 𝐹𝑚+1 + · · · + 𝐹𝑛.
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
