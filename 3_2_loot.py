# -*- coding: utf-8 -*-
"""
Created on Thu Feb 22 16:32:52 2018

@author: frente1x
"""


import random


def get_data():
    with open('3_2_loot.in', 'r') as data:
        line = [int(x) for x in data.readline().split()]
        cases = line[0]
        W = line[1]
        items = []
        for i in range(cases):
            line = [int(x) for x in data.readline().split()]
            value, weight = line[0], line[1]
            items.append({'value':value, 'weight':weight})
        return W, items
    

def get_vpu_list(items):
    vpus = []
    for item in items:
        value, weight = item['value'], item['weight']
        vpu = value / weight
        vpus.append((weight, vpu))
    vpus.sort(key=lambda i: i[1])
    return vpus


def max_val_loot(W, wei_vpu):
    tot = 0
    wei_vpu_copy = wei_vpu[:]
    for item in wei_vpu_copy:
        pair = wei_vpu.pop()
        wei = pair[0]
        vpu = pair[1]
        if wei <= W:
            W -= wei
            tot += (vpu*wei)
        elif W > 0:
            tot += vpu*W
            break
        else:
            break
    return tot
            

W, items = get_data()
wei_vpu = get_vpu_list(items)
print(max_val_loot(W, wei_vpu))

#L = [{random.random()*10:random.random()*100},
#     {random.random()*10:random.random()*100},
#     {random.random()*10:random.random()*100},
#     {random.random()*10:random.random()*100},
#     {random.random()*10:random.random()*100},
#     {random.random()*10:random.random()*100},
#     {random.random()*10:random.random()*100},
#     {random.random()*10:random.random()*100},
#     {random.random()*10:random.random()*100},]
#
#print(L,'\n')
#
#L.sort(key=lambda x: x.keys())
#
#print(L)