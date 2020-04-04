#task 1

import numpy as np
old = np.array([[1, 1, 1],
                [1, 1, 1]])

new = old
new[0, :2] = 0

print(old)

#task 2

old = np.array([[1, 1, 1],
                [1, 1, 1]])

new = old.copy()
new[:, 0] = 0

print(old)
