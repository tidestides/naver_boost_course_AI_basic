import numpy as np

arr1 = np.array([[5,7],[9,11]],float)
arr2 = np.array([[2,4],[6,8]],float)

concat_1 = np.vstack((arr1,arr2))
print(concat_1)