# Dictionary: Key Value pairs, Unordered, Mutable
# Key Value Pairs
mydict = {"name": "Max", "age": 28, "city": "New York"}
print(mydict)

# Each value pair maps key to value
# 2nd dictionary value -> Do not need to use nodes for your keys
my_dict2 = dict(name="Mary", age=27, city="Boston")
print(my_dict2)

# Can get a KeyError exception
value = mydict["age"]
print(value)

mydict["email"] = "max@xyz.com"
print(mydict)

# Overriding
mydict["email"] = "coolmax@xyz.com"
print(mydict)

# To delete
mydict.pop["age"]

# Remove last inserted value
mydict.popitem()

if "name" in mydict:
    print(mydict["name"])

try:
    print(mydict["lastname"])
except:
    print("Error")

# returns a list with all the keys
# for key in mydict.key():
#    print(key)
# returns the values
for value in mydict.values():
    print(value)

mydict_cpy = mydict
print(mydict_cpy)
mydict_cpy["email"] = "max@xyz.com"

mydict.update(my_dict2)
print(mydict)

my_dict = {3: 9, 6: 36, 9: 81}
print(my_dict)
value = my_dict[3]
print(value)
# cannot use a list as it is mutable
mytuple = (8,7)
mydict = {mytuple: 15}







