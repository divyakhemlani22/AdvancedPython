# collections: counter, namedtuple, ordereddict, defaultdict, deque

from collections import Counter, OrderedDict, DefaultDict, NamedTuple, Deque

f

a = "aaaabbbbcccc"
my_counter = Counter(a)
print(my_counter)
# this gets the counter for each element
print(my_counter.most_common(1)[0][0])
# print all the elements
print(list(my_counter.elements()))

Point = NamedTuple('Point','x,y')
pt = Point(1,-4)
# print the values for x and y
print(pt.x)
print(pt.y)

# ordered dictionary
ordered_dict = OrderedDict()
ordered_dict['a'] = 1
ordered_dict['b'] = 2
ordered_dict['c'] = 3
ordered_dict['d'] = 4
print(ordered_dict)

# default dictionary
d = DefaultDict(list)
d = {}
d['a'] = 1
d['b'] = 2
print (d['c'])

d = Deque()

d.append(1)
d.append(2)
# if only append - will append to the right else use appendleft
d.appendleft(3)
print(d)

d.pop()
print(d)

# if only extend - will append to the right else use extendleft
d.extendleft([4,5,6])
print(d)

# rotate 1 place to the left
# for rotate to the right - give -1 (1 to the right)
d.rotate(1)
print(d)
