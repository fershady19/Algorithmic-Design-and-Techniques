"""
Problem Description
Task. Given an integer n, find the nth Fibonacci number Fn. 
Input Format. The input consists of a single integer n. 
Constraints. 0 <= n <= 45.
Output Format. Output Fn.
"""

#python3
# Fibonacci number
def fib(n):
    fibs = [0, 1]
    if n > 1:
        for i in range(2,n+1):
            fibs.append(fibs[i-1]+fibs[i-2])
    return fibs[n]
n = int(input())
print(fib(n))
