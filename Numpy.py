import numpy as num

val = num.array([1, 2, 3, 4, 5])
print(val)


# version

import numpy as num
print(num.__version__)

# type

import numpy as num
val = num.array([1, 2, 3, 4, 5])
print(val)
print(type(val))

# 1 dimention

import numpy as num
val = np.array([1, 2, 3, 4, 5])
print(val)


# 2 dimention

import numpy as num
val = num.array([1, 2, 3, 4, 5])
print(val)

# 3 dimention

import numpy as num
val = num.array([[[1, 2, 3], [4, 5, 6]], [[1, 2, 3], [4, 5, 6]]])
print(val)


# higher dimention

import numpy as num
val = num.array([1, 2, 3, 4], ndmin=5)
print(val)
print('number of dimention :', val.ndim)


# concatenate join

    # single line    
import numpy as num
val1 = num.array([1, 2, 3])
val2 = num.array([4, 5, 6])
val = num.concatenate((val1, val2))
print(val)

    #two line     
import numpy as num
val1 = num.array([[1, 2], [3, 4]])
val2 = num.array([[5, 6], [7, 8]])
val= num.concatenate((val1, val2), axis=1)

print(arr)


# search

import numpy as num
val = num.array([1, 2, 3, 4, 5, 4, 4])
x = num.where(val == 4)
print(x)

