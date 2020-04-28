import numpy as np

fruits = np.array(['Apple', 'Mango', 'Grapes', 'Watermelon'])
print(fruits)

basket_1 = fruits.view()
basket_2 = fruits.view()

print(basket_1)
print(basket_2)

print('ids for the arrays are different.')
print("id for fruits is: ", id(fruits))
print(f'ids for baskets is: {id(basket_1)}, {id(basket_2)}')
print(basket_1 is fruits)       # False
print(basket_1.base is fruits)  # True

basket_2[0] = 'Strawberry'
print(basket_2)
print(fruits)    # base array was affected by the view
print(basket_1)  # also the second view was affected

basket_1 = np.array(['Peach', 'Pineapple', 'Banana', 'Orange'])
print(basket_1)

basket_2.shape = 2,2
print(basket_2)
print(fruits)  # the original base array hasn't been affected
