import numpy as np

array_one = np.array([1, 2, 3])
print(array_one)

array = [4, 5, 6]
array_two = np.array(array)
print(array_two)

array_of_zeros = np.zeros((3, 4))  # input: shape of the array (row, columns)
print(array_of_zeros)

array_of_ones = np.ones((3, 4))
print(array_of_ones)

array_of_ones_int = np.ones((3, 4), dtype=np.int16)
print(array_of_ones_int.dtype)

empty_array = np.empty((2, 3))
print(empty_array)

array_eye = np.eye(3)
print(array_eye)

array_of_evens = np.arange(2, 20, 2)  # (start, end, index jump)
print(array_of_evens)

array_of_floats = np.arange(0, 2, 0.3)
print(array_of_floats)

array_2d = np.array([(2, 4, 6), (3, 5, 7)])
print(array_2d)
print(array_2d.shape)

print(np.arange(6))

array_nd = np.arange(6).reshape(3, 2)
print(array_nd)

# will ignore this statement,because 3 * 4 = 12 != 6
# cannot reshape array of size 6 into shape (3, 4)
# array_nd = np.arange(6).reshape(3, 4)
# print(array_nd)

array_ones = np.ones_like(array_nd)  # will create the same shape with 1s values
print(array_ones)

# print arrays

c = np.arange(24).reshape(2, 3, 4)
print(c)

# will not print all the values
print(np.arange(10000).reshape(100, 100))

# # numpy configuration?
# np.set_printoptions(threshold=np.nan)
# print(np.arange(10000).reshape(100, 100))

