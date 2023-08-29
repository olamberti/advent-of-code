import numpy as np
x = np.uint16(123)
y = np.uint16(456)

# test numpy bitwise
print(x & y)
print(x | y)
print(x << 2)
print(y >> 2)
print(~x)
print(~y)

# code comes here