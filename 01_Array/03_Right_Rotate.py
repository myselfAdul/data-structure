a = [1, 2, 3, 4, 5]
lst_index = len(a) - 1  # 4
lst_item = a[-1]


# while lst_index > 0:
#     a[lst_index] = a[lst_index-1]
#     lst_index -= 1


for i in range(2):
    lst_index = len(a) - 1  # 4
    lst_item = a[-1]
    for i in range(lst_index, -1, -1):
        a[i] = a[i - 1]

    a[0] = lst_item


print(a)


# a = [1, 2, 3, 4, 5]

# for i in range(2):
#     lst_index = len(a)-1 #4
#     lst_item  = a[-1]

#     while lst_index > 0:
#         a[lst_index] = a[lst_index-1]
#         lst_index -= 1

#     a[0] = lst_item

# print(a)
