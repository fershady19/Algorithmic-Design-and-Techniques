"""
Task. Given an integer 𝑛, find the last digit of the sum 𝐹0 +𝐹1 +···+𝐹𝑛. Input Format. The input consists of a single integer 𝑛.
Constraints. 0 ≤ 𝑛 ≤ 1014.
Output Format. Output the last digit of 𝐹0 + 𝐹1 + · · · + 𝐹𝑛.
"""
def last_digit_fib(n, memo={}):
    if n == 0 or n == 1:
        return n
    try:
        return memo[n]
    except KeyError:
        result = (last_digit_fib(n-1, memo) + last_digit_fib(n-2, memo))%10
        memo[n] = result
        return result


def last_digit_fib_sum(n):
    n %= 60
    sum_ = 0
    for i in range(0, n+1):
        sum_ += last_digit_fib(i)
        sum_ %= 10
    return sum_


n = int(input())
print(last_digit_fib_sum(n))
