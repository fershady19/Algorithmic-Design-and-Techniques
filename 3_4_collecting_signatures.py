# -*- coding: utf-8 -*-
"""
Created on Fri Feb 23 09:06:22 2018

@author: frente1x 3_4_covering_segments
"""

def get_data():
    with open('3_4_covering_segments.in', 'r') as data:
        line = [int(x) for x in data.readline().split()]
        n = line[0]
        segments = []
        for i in range(n):
            line = [int(x) for x in data.readline().split()]
            a, b = line[0], line[1]
            segments.append((a, b))
        return segments
    
    
def collecting_signatures(segments):
    n = len(segments)
    b = segments[0][1]
    points = [b]
    for i in range(1,n):
        ai = segments[i][0]
        bi = segments[i][1]
        if ai <= b:
            if bi < b:
                b = bi
                points[-1] = b
        else:
            b = bi
            points.append(b)
    return len(points), points
    

segments = get_data()
segments.sort()
print(segments, '\n')
n, points = collecting_signatures(segments)
print(n)
print(points)
        
    
