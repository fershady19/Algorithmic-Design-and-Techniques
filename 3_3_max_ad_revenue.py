# -*- coding: utf-8 -*-
"""
Created on Fri Feb 23 08:03:27 2018

@author: frente1x
"""

def get_data():
    with open('3_3_dot_product20180216.in', 'r') as data:
        line = [int(x) for x in data.readline().split()]
        n = line[0]
        a = []
        b = []
        line = [int(x) for x in data.readline().split()]
        a = sorted(line)
        line = [int(x) for x in data.readline().split()]
        b = sorted(line)
        return a, b


def max_val_revenue(n,a,b):
    tot = 0
    for i in range(n):
        tot += a.pop()*b.pop()
    return tot


a, b = get_data()
n = len(a)
print(max_val_revenue(n, a, b))

    
