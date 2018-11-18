# -*- coding: utf-8 -*-
"""
Created on Fri Feb 23 10:53:41 2018

@author: frente1x
"""

def get_data():
    with open('3_6_largest_number.in', 'r') as data:
        data.readline()
        a = sorted([int(x) for x in data.readline().split()])
        return a


def grp_by_d(num_lis):
    grp_by_digits = [[] for _ in range(10)]
    for num in num_lis:
        dig = str(num)[0]
        idx = int(dig)
        grp_by_digits[idx].append(num)
    return grp_by_digits
    

def maxi(dig_grps):
    for l in dig_grps:
        for i in range(1, len(l)-1):
            
num_lis = get_data()
grp = grp_by_d(num_lis)
print(grp)
    