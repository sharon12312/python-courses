import numpy as np
import csv

a = np.arange(12) ** 2
print(a)

print(a[2])
print(a[6])
print(a[8])

index_1 = [2, 6, 8]
print(a[index_1])

# even though the array is 1D and the index is 2D
# it's still presents the values in these indexes
index_2 = np.array([[2, 4], [8, 10]])
print(index_2)
print(a[index_2])

food = np.array([['blueberry', 'strawberry', 'cherry', 'blackberry'],
                 ['pinenut', 'hazelnuts', 'cashewnut', 'coconut'],
                 ['mustard', 'paprika', 'nutmeg', 'clove']])

print(food)

# row contains all the information of the rows
# row contains all the information of the column
# combine each index together => (row in index 0, column in index 0)
# you can read it as column: (0,0), (0,3), (2,0), (2,3)
row = np.array([[0, 0], [2, 2]])
col = np.array([[0, 3], [0, 3]])

print(food[row, col])
print(food[2, 0])

food[row, col] = '000'
print(food)
