import numpy as np

a = np.array([1, 2, 3, 4, 5])
b = np.array([10, 10, 10, 10, 10])  # act as a scalar

print(a * b)

c = 10  # scalar
print(a * c)

one = np.ones((4, 3))
print(one)
print(one * c)

# ---

heights = [165, 170, 168, 183, 172, 169]
weights = [61, 76, 56, 81, 62, 60]

student_bio = np.array([heights, weights])
print(student_bio)

factor_1 = np.array([0.0328084, 2.20462])
print(factor_1)

print(factor_1.shape)
print(student_bio.shape)

# will get an error: we cannot broadcast with different shapes
# print(student_bio * factor_1)

factor_2 = np.array([[0.0328084], [2.20462]])
print(factor_2)
print(factor_2.shape)

# will work: (2, 6) * (2, 1) => if the values in index 0 are equal
# and the values in index 1 are different, but one has the value of 1
# we an perform broadcasting
print(student_bio * factor_2)
