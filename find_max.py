# You will have to figure out what parameters to include
# 🚨 All functions must use recursion 🚨

# This function returns the largest number in a given array.

# def find_max(l):
#     if len(l) == 1:
#         return l[0]
#     else:
#         m = find_max(l[1:])
#         return m if m > l[0] else l[0]
#     pass

# print(find_max([1, 4, 45, 6, -50, 10, 2]))
# => 45

""" pete's solution """
import math

def find_max(l, current_max = -math.inf):
    if len(l) == 0:
        return current_max

    if l[0] > current_max:
        new_current_max = l[0]
    else:
        new_current_max = current_max
    
    return find_max(l[1:], new_current_max)

print(find_max([1, 4, 45, 6, -50, 10, 2]))