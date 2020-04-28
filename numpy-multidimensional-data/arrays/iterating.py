import numpy as np

# 1D array
a = np.arange(11) ** 2
print(a)

for i in a:
    print(i ** (1/2))  # power of 0.5 is square

# 2D array
students = np.array([['Alice', 'Beth', 'Cathy', 'Dorothy'],
                     [65, 78, 90, 81],
                     [71, 82, 79, 92]])

# print only the rows
for i in students:
    print(i)

# print all the element of each row
for element in students.flatten():
    print(element)

# print all the elements of each columns
for element in students.flatten(order='F'):
    print(element)

x = np.arange(12).reshape(3, 4)
print(x)

# print all the element of each row
for i in np.nditer(x):
    print(i)

# print all the element of each column
for i in np.nditer(x, order='F'):
    print(i)

# external_loop will present the matrix in a column major order
for i in np.nditer(x, order='F', flags=['external_loop']):
    print(i)

# in general 'nditer' allows us only to perform read operation
# to change it, we will use the op_flags parameter
for arr in np.nditer(x, op_flags=['readwrite']):
    arr[...] = arr * arr

print(x)
