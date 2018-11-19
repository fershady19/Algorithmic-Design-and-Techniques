"""
Task. The goal in this code problem is to check whether an input sequence contains a majority element.
"""

def majority_element(L):
    if len(L) == 2:
        return L[0] == L[1]
    else:
        middle = len(L)//2
        print (middle)
        print("list1: ", L[:middle])
        print("list2: ", L[middle:])
        return 0 #majority_element(L[:middle]) or majority_element(L[middle:])

print(majority_element([1, 2, 3, 2, 2]))