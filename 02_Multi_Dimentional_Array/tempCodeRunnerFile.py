
import numpy as np

#  3D array
arr0 = np.array([[[1, 2, 3], [4, 5, 6]], [[1, 2, 3], [4, 5, 6]]])

print(arr0.ndim)


# 2D array
arr1 = np.array([[1,2,3], [4,5,6]])
print(arr1.ndim)


# 1D array

arr2 = np.array([1,2,3])
print(arr2.ndim)

arr3 = np.array(10)
print(arr3.ndim)


arr = np.array([1, 2, 3, 4], ndmin=5)

print(arr)
print('number of dimensions :', arr.ndim)

