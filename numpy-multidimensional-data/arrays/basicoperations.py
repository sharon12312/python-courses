import numpy as np

a = np.array([10, 10, 10])
b = np.array([5, 5, 5])

# in case the 2 arrays have the same dimensions
print(a + b)
print(a - b)
print(a * b)
print(a / b)
print(a % 3)
print(a < 35)

A = np.array([[1, 1], [0, 1]])
B = np.array([[2, 0], [3, 4]])

print('A:\n', A)
print('B:\n', B)
print('')
print(A * B)
print('')
print(A.dot(B))
print(np.dot(A, B))
print('')

a *= 3
print(a)
print('')

ages = np.array([12, 15, 18, 20])
print(ages.sum())
print(ages.min())
print(ages.max())
print('')

numbers = np.arange(12).reshape(3, 4)
print(numbers)
print(numbers.sum(axis=0))  # axis=0 => column
print(numbers.sum(axis=1))  # axis=1 => row
print(numbers.min(axis=1))







