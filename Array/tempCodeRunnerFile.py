a = [1, 2, 3, 4, 5]

# Right shift

for i in range(len(a)-1, 0, -1):
    a[i] = a[i-1]
    a[i-1] =0

print(a)

# left shift
for i in range(5):

    for i in range(0, len(a)-1):
        a[i] = a[i+1]
        a[i+1] =0

    print(a)

