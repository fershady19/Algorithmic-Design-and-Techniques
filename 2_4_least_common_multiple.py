"""
Task. Given two integers a and b, find their least common multiple.
Input Format. The two integers a and b are given in the same line separated by space.
Constraints. 1<=a,b<=2·109.
Output Format. Output the least common multiple of a and b.
"""

def EuclidGCD(a, b):
    if b == 0:
        return a
    else:
        a = a%b
        return EuclidGCD(b, a)

def LCM(a, b):
    return a*b//EuclidGCD(a, b)


in_ = [int(n) for n in input().split()]
print(LCM(in_[0], in_[1]))
