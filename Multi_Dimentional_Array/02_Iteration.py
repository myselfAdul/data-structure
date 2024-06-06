import numpy as np

arr3d = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])

arr2d = np.array([[1, 2, 3], [4, 5, 6]])

rsum = 0

# iterate
for i in arr2d:
    for j in i:
        # print(j)
        pass


for i in arr3d:
    for j in i:
        for k in j:
            # print(k)
            pass
    pass


#  row wise iteration
def print_row(m):
    for i in m:
        for j in i:
            print(j, end=" ")
        print("\n")


# Example usage
m = np.array([[2, 3, 4], [3, 2, 1]])

# print_row(m)


# column wise iteration
def print_column(m):
    rlen = len(m)
    clen = len(m[0])
    
    for i in range(clen):
        for j in range(rlen):
            print(m[j,i])
    
    pass

print_column(m)

