import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

gdp_16 = pd.read_csv('../data/gdp_pc.csv')['2016'].values
print(type(gdp_16))
print(gdp_16.shape)

# plt.plot(gdp_16)
# plt.show()

print(np.median(gdp_16))  # result: nan, because there are non values in the data

# filter non values
gdp_16 = gdp_16[~np.isnan(gdp_16)]
print(gdp_16)
print(gdp_16.shape)

print(np.median(gdp_16))
print(np.mean(gdp_16))

# filtering by condition
print(gdp_16[gdp_16 > 40000])
print(np.count_nonzero((gdp_16 > 40000) & (gdp_16 < 50000)))  # & = AND operation

print(np.sort(gdp_16)[:10])   # the first 10 values
print(np.sort(gdp_16)[228:])  # the last 10 values

