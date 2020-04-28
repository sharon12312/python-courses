import numpy as np

salaries = np.genfromtxt('../data/salary.csv', delimiter=',')
print(salaries)
print(salaries.shape)
print(np.argmax(salaries))  # index of the max value - result: 8
print(salaries[8])
print(np.argmin(salaries))  # index of the min value - result: 0
print(salaries[0])
print(np.argsort(salaries))  # return the indices of the sorted values
print(np.argsort(salaries, kind='mergesort'))

sorted_array_indices = np.argsort(salaries, kind='mergesort')
print(salaries[sorted_array_indices])

greater_than_1000 = np.where(salaries > 1000)  # return indices
print(len(greater_than_1000[0]))
print(salaries[greater_than_1000])

condition = salaries > np.mean(salaries)
print(np.mean(salaries))
print(salaries[condition])              # option 1
print(np.extract(condition, salaries))  # option 2
