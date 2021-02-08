import numpy as np 

a = np.arange(24).reshape(4,6)

print(a)

#column array
print(np.c_[1,0,4])

print(np.reshape(a,(6,4)))