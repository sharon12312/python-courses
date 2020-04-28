import numpy as np

a = np.array([('Germany', 'France', 'Hungary', 'Austria'),
              ('Berlin', 'Paris', 'Budapest', 'Vienna')])

print(a)
print(a.shape)  # (rows, columns) => (2, 4)
print(a.ravel())  # flatten an  N-D array to a 1-D array
print(a.T)  # transpose of an array: rows become columns and columns become rows
print(a.T.ravel())
print('')

# reshape an array
print('before reshape:')
print(a)
print('after reshape')
print(a.reshape(4,2))
print('')

# ---
print(np.arange(15).reshape(3, 5))
print(np.arange(15).reshape(5, 3))
print('')

# ---
countries = np.array(['Germany', 'France', 'Hungary', 'Austria', 'Italy', 'Denmark'])
print(countries)
print(countries.reshape(-1, 3))  # -1 means unknown rows dimension
print(countries.reshape(3, -1))  # -1 means unknown columns dimension

