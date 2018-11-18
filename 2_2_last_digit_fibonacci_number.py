"""
Task. Given an integer 𝑛, find the last digit of the 𝑛th Fibonacci number 𝐹𝑛 (that is, 𝐹𝑛 mod 10). 
Input Format. The input consists of a single integer 𝑛.
Constraints. 0 ≤ 𝑛 ≤ 107.
Output Format. Output the last digit of 𝐹𝑛.
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

