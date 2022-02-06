import numpy as np

arr1 = np.random.normal(0,1,15).reshape(5,3)
arr2 = np.random.normal(0,1,6).reshape(3,2)
dot = arr1.dot(arr2)
print(dot,dot.shape)