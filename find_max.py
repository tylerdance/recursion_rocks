# You will have to figure out what parameters to include
# 🚨 All functions must use recursion 🚨

# This function returns the largest number in a given array.

def find_max(l):
    if len(l) == 1:
        return l[0]
    else:
        m = find_max(l[1:])
        return m if m > l[0] else l[0]
    pass

print(find_max([1, 4, 45, 6, -50, 10, 2]))
# => 45