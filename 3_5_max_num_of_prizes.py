# -*- coding: utf-8 -*-
"""
Created on Fri Feb 23 10:22:02 2018

@author: frente1x
"""
n = 182414564
def max_num_of_prizes(n):
    i = 1
    prizes = []
    while i < n-i:
        prizes.append(i)
        n -= i
        i += 1
    prizes.append(n)
    k = len(prizes)
    return k, prizes

k, prizes = max_num_of_prizes(n)
print(k)