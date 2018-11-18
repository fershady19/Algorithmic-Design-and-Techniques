"""
Task. The goal in this problem is to find the minimum number of coins needed to change the input value (an integer) into coins with denominations 1, 5, and 10.
Input Format. The input consists of a single integer m.
Constraints. 1 <= m <= 103.
Output Format. Output the minimum number of coins with denominations 1, 5, 10 that changes m.
"""

def money_change(m):
    tens = m//10
    m %= 10
    fives = m//5
    ones = m%5
    print(tens, fives, ones)
    return tens+fives+ones

print(money_change(999))
