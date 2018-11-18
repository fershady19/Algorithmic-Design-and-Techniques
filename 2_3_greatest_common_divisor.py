"""
Task. Given two integers a and b, find their greatest common divisor.
Input Format. The two integers a, b are given in the same line separated by space.
Constraints. 1<=a,b<=2·109.
Output Format. Output GCD(a, b).
"""

def EuclidGCD(a, b):
    if b == 0:
        return a
    else:
        a = a%b
        return EuclidGCD(b, a)

in_ = [int(n) for n in input().split()]
print(EuclidGCD(in_[0], in_[1]))
