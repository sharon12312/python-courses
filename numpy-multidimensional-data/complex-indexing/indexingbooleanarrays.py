import numpy as np

a = np.arange(16).reshape(4, 4)
print(a)

index_bool = a > 9
print(index_bool)
print(a[index_bool])

print(np.count_nonzero(a < 6))
print(np.sum(a < 6))

# condition in a row-wise major
print(np.sum(a < 6, axis=1))
# result: [4, 2, 0, 0] means there were 4 elements which are greater than 6 in the first row,
# 2 in the second row and none in the other rows.

print(np.any(a > 8))
print(np.all(a < 10))
print(np.all(a < 100))
print(np.all(a < 9, axis=1))

