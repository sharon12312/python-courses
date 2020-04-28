import datetime
import math

value = 4 * 20
print(f'the value is {value}')

print(f'The current time is {datetime.datetime.now().isoformat()}.')
print(f'Math constants: pi={math.pi:.3f}, e={math.e:.3f}')


# list = range(1,11)
list = [1, 2, 3, 4, 5, 6]
print(list[-1])
print(list[1: 3])
print((list[1: -1]))
print(list[2:])
print(list[:2])
print(list[:])

other_list = list
print(other_list is list)

other_list = list[:]
print(other_list is list)
print(other_list == list)

other_list = list.copy()
print(other_list is list)
print(other_list == list)

print([0] * 10)
print([1, 2] * 2)

s = [[-1, 1]] * 5
print(s)
s[2].append(0)
print(s)

s = [2,1,4,6]
s.reverse()
print(s)
s.sort()
print(s)
