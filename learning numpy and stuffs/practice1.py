import numpy as np

a = np.array(
    [
        [1, 2, 3, 4, 5],
        [6, 7, 8, 9, 10],
        [11, 12, 13, 14, 15],
        [16, 17, 18, 19, 20],
        [21, 22, 23, 24, 25],
        [26, 27, 28, 29, 30],
    ]
)
# print(a[2:4, 0:2])

print(a[[0, 4, 5], 3:5])

b = np.array([[4, 5, 6, 8, 665, 33, 42], [1, 2, 2, 1, 2, 44, 55]])

# print(a[0, -1:1:-2])

b[0, 4] = 69

c = np.zeros((5, 2), dtype="int32")
# print(c, type(c[0, 1]))
d = np.ones((1, 2, 3))
# print(d)

e = np.full((2, 3), 40)
# print(e)

# random
f = np.random.rand(2, 10)  # can do random.randint(start, stop, size(x, y))
# print(f)

# identity matrix
# print(np.identity(3))

# print(
#     np.concatenate(
#         (
#             np.ones((1, 5), dtype="int32"),
#             np.full((1, 5), (1, 0, 0, 0, 1)),
#             np.full((1, 5), (1, 0, 9, 0, 1)),
#             np.full((1, 5), (1, 0, 0, 0, 1)),
#             np.ones((1, 5), dtype="int32"),
#         ),
#         axis=0,
#     )
# )


# u can use math functions on numpy arrays
# print(a + 2)
# print(b - 10)
# print(np.sin(a))

# there are also functions for linear algebra like matrix multiply and finding determenent


# u can index with a list in numpy
k = np.array([1, 2, 3, 4, 5, 7, 8])
print(k[[3, 5]])

# can also check if some values in ur nd array is greater or less than sth
print(k > 4)

# can also do boolean index but need to be array length
print(k[[True, True, False, False, True, True, False]])
