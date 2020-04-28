import numpy as np

x = np.array([['Germany', 'France'], ['Berlin', 'Paris']])
y = np.array([['Hungary', 'Austria'], ['Budapest', 'Vienna']])

print(x)
print(x.shape)

print(y)
print(y.shape)

# column-wise joining (axis = 0)
print('Joining two arrays along axis 0:')
print(np.concatenate((x, y)))

# row-wise joining (axis = 1)
print('Joining two arrays along axis 1:')
print(np.concatenate((x, y), axis=1))

# ---
a = np.array([1, 2, 3])
b = np.array([2, 3, 4])

# joining 2 arrays
# stack wil be column-wise by default when joining 2 arrays
print(np.stack((a, b)))

# ---
studentId = np.array([1, 2, 3, 4])
name = np.array(['Alice', 'Beth', 'Cathy', 'Dorothy'])
scores = np.array([65, 78, 90, 81])

# stack column-wise
print(np.stack((studentId, name, scores)))
print(np.stack((studentId, name, scores)).shape)

# stack row-wise
print(np.stack((studentId, name, scores), axis=1))
print(np.stack((studentId, name, scores), axis=1).shape)

# vertical stack
print(np.vstack((studentId, name, scores)))
# horizontal stack
print(np.hstack((studentId, name, scores)))
