# Lists: ordered, mutable, allows duplicate elements
mylist = ["banana","cherry","apple"]
print(mylist)

#creating a list
# Goes to the last item in the list
item = mylist[-1]
print(item)

# using a loop to print the list
for x in mylist:
    print(x)

# checking if element is inside the list
if "banana" in mylist:
    print("yes")
else:
    print("no")

# checking number of elements inside the list
print(len(mylist))

# adding another element to the list
mylist.append("lemon")
print(mylist)

# pop element
mylist.pop()
print(mylist)

# removing element
mylist.remove("cherry")
print(mylist)

# clearing list
mylist.clear()
print(mylist)

# reversing list
mylist.reverse()

# printing 2 elements in the list
mylist = [1,2,3,4,5,6,7,8,9]
a = mylist[::2]
print(a)

new_list = sorted(mylist)
print(mylist)
print(new_list)
mylist = [0] * 5
print(mylist)

mylist2 = [1,2,3,4,5]
new_list = mylist + mylist2
print(new_list)

# printing range from 1 to 5 exclude the first
mylist3 = [1,2,3,4,5,6,7,8,9]
a = mylist3[1:5]
print(a)

# reversing a list - printing every last 1 backwards
mylist4 = [1,2,3,4,5,6,7,8,9]
a = mylist4[::-1]
print(a)

# making a copy of a list
list_org = ["banana","cherry","apple"]
list_cpy = list_org
print(list_cpy)

# appending to the copy of the list
list_cpy.append("lemon")
print(list_cpy)
print(list_org)

a = [1,2,3,4,5,6]
b = [i*i for i in mylist]
print(mylist)
print(b)
















