# Sets: unordered, mutable, no duplicates
myset = {1,2,3,4,5}
print(myset)

myset2 = set([1,2,3,4])

myset3 = set("Hello")
print(myset3)
print(type(myset3))

# creating an empty set
myset.add(1)
myset.add(2)
myset.add(3)

myset.remove(4)
myset.discard(4)
myset.clear()
print(myset.pop())

print(myset)

for x in myset:
    print(x)

if 1 in myset:
    print("Yes")
else:
    print("No")

odds = {1,3,5,7,9}
evens = {0,2,4,6,8}
primes = {2,3,5,7}

# Joining two sets together
u = odds.union(evens)
print(u)

i = odds.intersection(evens)
print(i)

setA = {1,2,3,4,5,6,7,8,9}
setB = {1,2,3,10,11,12}

# difference of two sets
diff = setA.difference(setB)
print(diff)

# symmetric difference of two sets -> Updates by keeping elements in both sets but not common
diff = setB.symmetric_difference(setA)
print(diff)

# Update the set by adding elements in the other set
setA.update(setB)
print(setA)

# update set by keeping elements in both sets
setA.intersection_update(setB)
print(setA)

# updates by removing what is already in the other set
setA.difference_update(setB)

# ALl the elements in first set must also be in the second set
print(setA.issubset(setB))

# superset
print(setA.issuperset(setB))

# Sets does not have anything in common
print(setA.isdisjoint(setB))

# Popping sets
# making a copy not replacing it
setB = setA.copy()
setB.add(7)
print(setB)
print(setA)

# frozenset - cannot add, delete etc
a = frozenset([1,2,3,4])
a.add(2) # invalid
print(a) # invalid








