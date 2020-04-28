# A Python program to print all
# permutations using library function
from itertools import permutations
# A Python program to print all
# combinations of given length
from itertools import combinations

# Get all combinations of [1, 2, 3]
# and length 2
comb = combinations([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17], 7)

size = 0
# Print the obtained combinations
for i in list(comb):
    print(i)
    size += 1

print('Size: ', size)

print('')
# Get all permutations of [1, 2, 3]
perm = permutations([1, 2, 3], 2)

# Print the obtained permutations
for i in list(perm):
    print(i)