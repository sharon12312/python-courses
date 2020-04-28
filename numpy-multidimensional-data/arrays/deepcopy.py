import numpy as np

fruits = np.array(['Apple', 'Mango', 'Grapes', 'Watermelon'])
print(fruits)

basket = fruits.copy()
print(basket)
print(basket is fruits)
print(basket.base is fruits)

basket[0] = 'strawberry'
print(basket)
print(fruits)

basket.shape = 2,2
print(basket)
print(fruits)

