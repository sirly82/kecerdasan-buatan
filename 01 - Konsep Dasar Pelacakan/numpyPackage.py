# Cara import 1
# import numpy as np
# # print(numpy.__file__)
# print(np.subtract(3,4))

# Cara import 2
# from numpy._core import subtract
# print(subtract(10, 5))

# Cara import 3
from numpy._core import subtract as sub
print(sub(100,35))