"""
Task. Given an integer n, find the last digit of the nth Fibonacci number Fn (that is, Fn mod 10). 
Input Format. The input consists of a single integer n.
Constraints. 0 <= n <= 107.
Output Format. Output the last digit of Fn.
"""

def last_digit_fib(n):
    a, b = 0, 1
    if n < 2:
        return n
    else:
        for i in range(1,n):
            fib = (a + b)%10
            a, b = b, fib
        return fib
n = int(input())
print(last_digit_fib(n))

