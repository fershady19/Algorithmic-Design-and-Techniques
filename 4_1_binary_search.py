"""
Task. The goal in this code problem is to implement the binary search algorithm.
Input Format. The first line of the input contains an integer n and a sequence a0 < a1 < . . . < an−1 of n pairwise distinct positive integers in increasing order. 
The next line contains an integer k and k positive integers b0, b1, . . . , bk−1.
Constraints. 1<=n,k<=104;1<=ai <=109 forall0<=i<n;1<=bj <=109 forall0<=j<k; OutputFormat. Forall i from0 to k−1,output an index 0<=j<=n−1 such that
aj = bi or −1 if there is no such index.
"""
import math as m

with open("4_1_binary_search.in") as data:
    f_line = [int(i) for i in data.readline().split(' ')]
    s_line = [int(i) for i in data.readline().split(' ')]
    n = f_line[0]
    a = list(f_line[1:])
    k = s_line[0]
    b = list(s_line[1:])


def binary_search(e, L):
    start = 0
    end = len(L)-1
    for _ in range(int(m.log(len(L), 2)) + 1):
        middle_idx = (end + start) // 2
        print("start: {0}, end: {1}, middle: {2}".format(start, end, middle_idx))
        if e == L[middle_idx]:
            return middle_idx
        elif e > L[middle_idx]:
            start = middle_idx
        else:
            end = middle_idx
    return -1

def recursive_binary_search(elem, start, end, L):
    if start == end:
        if elem == L[end]:
            return end
        else:
            return -1
    else:
        mid = (start + end) // 2
        if elem > L[mid]:
            return recursive_binary_search(elem, mid+1, end, L)
        else:
            return recursive_binary_search(elem, start, mid, L)


a.sort()

suma = 0
for i in range(k):
    if recursive_binary_search(b[i], 0, len(a), a) >= 0:
        suma += 1

print(suma)