"""
Task. Given two integers 𝑎 and 𝑏, find their greatest common divisor.
Input Format. The two integers 𝑎, 𝑏 are given in the same line separated by space.
Constraints. 1≤𝑎,𝑏≤2·109.
Output Format. Output GCD(𝑎, 𝑏).
"""

def EuclidGCD(a, b):
    if b == 0:
        return a
    else:
        a = a%b
        return EuclidGCD(b, a)

in_ = [int(n) for n in input().split()]
print(EuclidGCD(in_[0], in_[1]))
