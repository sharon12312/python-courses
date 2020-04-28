import numpy as np

x = np.arange(9)
print(x)

print('Split the array in 3 equal-sized sub arrays:')
print(np.split(x, 3))

print('Split the array at positions indicated in 1-D array:')
print(np.split(x, [4,7]))

y = np.array([('Germany', 'France', 'Hungary', 'Austria'),
              ('Berlin', 'Paris', 'Budapest', 'Vienna')])
print(y)

# split horizontally
p1, p2 = np.hsplit(y, 2)
print(p1)
print(p2)

# split vertically
p1, p2 = np.vsplit(y, 2)
print(p1)
print(p2)
