import numpy as np

a = np.arange(30)
print(a)

# -1 means that we don't know the particular dimension
a.shape = 2, -1, 3

# we will get (2 * 5 * 3) array shape
print(a)
print(a.shape)
print('')

a.shape = 2, 3, -1
print(a)
print(a.shape)
print('')

