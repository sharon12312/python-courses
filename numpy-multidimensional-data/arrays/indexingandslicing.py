import numpy as np

a = np.arange(11) ** 2  # ** = square operation
print(a)

# indexing
# [  0   1   4   9  16  25  36  49  64  81 100 ] => an array
# [  0   1   2   3   4   5   6   7   8   9  10 ] => positive index
# [-11 -10  -9  -8  -7  -6  -5  -4  -3  -2  -1 ] => negative index
print(a[2])
print(a[-2])

# slicing
print(a[2:7])    # from index 2 to index 7
print(a[2:-2])   # from index 2 to index -2 (9)
print(a[2:])     # from index 2 to the end of the array
print(a[:7])     # from index 0 to index 7
print(a[:11:2])  # from index 0 to index 11, in steps of 2
print(a[::-1])   # stp = -1 means step backwards
print('')
# ---

students = np.array([['Alice', 'Beth', 'Cathy', 'Dorothy'],
                     [65, 78, 90, 81],
                     [71, 82, 79, 92]])

print(students)
print(students[0])
print(students[1])
print(students[2])

# specific cell
print(students[0][1])

# multiple cells
print(students[0:2, 2:4])  # [(rows), (columns)]

print(students[:, 1:2])  # no numbers means all of the rows
print(students[:, 1:3])

# negative practice
print(students[-1, :])  # -1 means the last row, and no number means all of the columns
print(students[-3:-1, -2:])

print(students[0, ...])  # ... means all the columns
print(students[..., 1])  # return the second columns as a list


