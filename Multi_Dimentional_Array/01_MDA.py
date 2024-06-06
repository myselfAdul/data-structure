import numpy as np

arr = np.array([[1,2,3,4,5], [6,7,8,9,10]])

print('2nd element on 1st row: ', arr[0][1])

print("2ns row 5th column:", arr[1][4])

arr3 = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])

print("3rd element of the 2nd array of the 1st array:", arr3[0, 1, 2] )


print(arr[1][-1])