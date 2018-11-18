"""
Problem Description
Task. Given an integer 𝑛, find the 𝑛th Fibonacci number 𝐹𝑛. 
Input Format. The input consists of a single integer 𝑛. 
Constraints. 0 ≤ 𝑛 ≤ 45.
Output Format. Output 𝐹𝑛.
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
