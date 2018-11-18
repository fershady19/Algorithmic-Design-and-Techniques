"""
Task. Given two integers 𝑎 and 𝑏, find their least common multiple.
Input Format. The two integers 𝑎 and 𝑏 are given in the same line separated by space.
Constraints. 1≤𝑎,𝑏≤2·109.
Output Format. Output the least common multiple of 𝑎 and 𝑏.
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
