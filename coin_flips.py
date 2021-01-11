# You will have to figure out what parameters to include
# 🚨 All functions must use recursion 🚨`

# This function returns an array of all possible outcomes from flipping a coin N times.
# Input type: Integer 
# H stands for Heads and T stands for tails
# Represent the two outcomes of each flip as "H" or "T"

# n = 2
# toss = list('-' * n)

# def coin_flips(n):
#     if type(n) != int:
#         raise TypeError('Value must be an integer')
#     global toss
#     if n == 1:
#         toss[-n] = 'T'
#         print(''.join(toss))
#         toss[-n] = 'H'
#         print(''.join(toss))
#     else:
#         toss[-n] = 'T'
#         coin_flips(n-1)
#         toss[-n] = 'H'
#         coin_flips(n-1)

    # coin_flips(n)
    
# print(coin_flips(2)) 
# => ["HH", "HT", "TH", "TT"]

""" pete's solution """
def coin_flips(n):
    if n == 1:
        return ['H', 'T']

    already_flipped = coin_flips(n - 1)
    
    history_plus_heads = list(map(lambda x: x + 'H', already_flipped))
    history_plus_tails = list(map(lambda x: x + 'T', already_flipped))

    return history_plus_heads + history_plus_tails

print(coin_flips(3))