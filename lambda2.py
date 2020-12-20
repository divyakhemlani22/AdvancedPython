# lambda function: arguments then colon then expressions
add10 = lambda x: x + 10
print(add10())


def add10_func(x):
    return x + 10


# can also have multiple arguments
# used only once in your code
mult = lambda x, y: x + y
print(mult(2, 7))

points2D = [{1, 2}, {15, 1}, {5, -1}, {10, 4}]
points2D_sorted = sorted(points2D, key=lambda x: x[0] + x[1])
print(points2D)
print(points2D_sorted)


def sort_by_y(x):
    return x[1]


print(points2D)
print(points2D_sorted)

a = [1,2,3,4,5]
b = map(lambda x: x*2, a)
print(list(b))

# syntax to print c
c = [x*2 for x in a]
print(c)

# filter function - returns all elements
b = filter(lambda x: x % 2 == 0, a)
print(list(b))

c = [x for x in a if x%2 == 0]
print(c)

from functools import reduce
# Reduce function - Reduces to a single value
a = [1, 2, 3, 4, 5, 6]
product_a = reduce(lambda x, y: x*y, a)
print(product_a)
