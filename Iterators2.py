# Itertools: product, permutations, combinations, accumulate, groupby, infinite iterators

from itertools import product

a = {1, 2}
b = {3, 4}
prod = product(a, b, repeat=2)
print(list(prod))

from itertools import permutations, accumulate, groupby, count, cycle, repeat
from itertools import combinations, combinations_with_replacement

a = [1, 2, 3]
perm = permutations(a, 2)
print(list(perm))
comb = combinations(a, 2)
print(list(comb))
# combination with replacement
comb_wr = combinations_with_replacement(a, 2)
print(list(comb_wr))

# accumulate
a = [1, 2, 3, 4]
# return the max for each comparison
acc = accumulate(a, function=max)
print(a)
print(list(acc))


# group by
def smaller_than_3(x):
    return x < 3


# grouping based on age or based on their number
persons = [{'name': 'Tim', 'age': 25}, {'name': 'Dan', 'age': 26},
           {'name': 'Lisa', 'age': 24}]
a = [1, 2, 3, 4]
group_obj = groupby(a, key=lambda x: x['age'])
for key, value in group_obj:
    print(key, list(value))

# lambda
# lambda x: x['age']
# small one line function -> have an input. does expression. return an output
# lambda x: x<3

# infinite iterators => count, cycle, repeat
# 10 is the start value
a = [1, 2, 3]
for i in count(10):
    print(i)
    if i == 15:
        break

# cycle
a = [1, 2, 3]
for i in cycle(a):
    # cycle infinitely
    print(i)

# cycle
a = [1, 2, 3]
for i in repeat(1, 4):
    # cycle infinitely
    print(i)

