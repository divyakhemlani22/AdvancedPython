import sys
import timeit

mytuple = ("Max",28,"Boston")
print(mytuple)

# Using type to print data type in a tuple
mytuple1 = ("Max")
# will print <class 'str'>
print(type(mytuple1))

item = mytuple[-2]
print(item)

mytuple[0] = "Tim"

for i in mytuple:
    print(i)

if "Max" in mytuple:
    print("yes")
else:
    print("no")

my_tuple = ('a','p','p','l','e')
print(len(my_tuple))
print(my_tuple.count('p'))
print(my_tuple.index('p'))

my_list = list(my_tuple)
print(my_list)

my_tuple2 = tuple(my_list)
print(my_tuple2)

a = (1,2,3,4,5,6,7,8,9,10)

# number 3, 4, 5 in tuple b
b = a[2:5]
print(b)

# reversing array b
b = a[::-1]
print(b)

my_tuple = "Max",20,"Boston"

# number of elements here must match the number of elements in the tuple
name, age, city = my_tuple
print(name)
print(age)
print(city)

my_tuple = (0,1,2,3,4)
# use *tuple to print the tuple in the middle or the side
i1,*i2, i3 = my_tuple
print(i1)
print(i2)
print(i3)

# append a tuple and a list
my_list = [0,1,2,"hello",True]
my_tuple = [0,1,2,"hello",True]
print(sys.getsizeof(my_list),"bytes")
print(sys.getsizeof(my_tuple),"bytes")

# used to get a specific number of times
print(timeit.timeit(stmt="[0,1,2,3,4,5]", number=1000000))
print(timeit.timeit(stmt="[0,1,2,3,4,5]", number=1000000))







