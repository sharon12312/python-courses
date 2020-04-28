import numpy as np
import matplotlib.pyplot as plt

print(np.histogram([1, 2, 1], bins=[0, 1, 2, 3]))

mu, sigma = 2, 0.5
data = np.random.normal(mu, sigma, 10000)
print(data)

(n, bin_edges) = np.histogram(data, bins=50)
print(n)  # how many times a specific bin is displayed
print(bin_edges)  # the values of the bins

# plt.plot(bin_edges[1:], n)
# plt.show()
