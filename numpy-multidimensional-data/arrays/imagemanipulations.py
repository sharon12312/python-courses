import numpy as np
import matplotlib.pyplot as plt
from scipy import ndimage
from scipy import misc


f = misc.face()

print(f.shape)
print(type(f))
print(f)

# plt.imshow(f)
# plt.show()

# select only a portion of the array which represents the image
a = f[384:, 512:, :]

# plt.imshow(a)
# plt.show()

a1, a2 = np.split(f, 2)

# plt.imshow(a1)
# plt.show()
# plt.imshow(a2)
# plt.show()

b1, b2 = np.split(f, 2, axis=1)

# plt.imshow(b1)
# plt.show()
# plt.imshow(b2)
# plt.show()

# # concat the 2 vertical parts of the image
# plt.imshow(np.concatenate((a1, a2)))
# plt.show()

# # concat the 2 horizontal parts of the image - NOT GOOD
# plt.imshow(np.concatenate((b1, b2)))
# plt.show()

# # concat the 2 horizontal parts of the image - GOOD
# plt.imshow(np.concatenate((b1, b2), axis=1))
# plt.show()


