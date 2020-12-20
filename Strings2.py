# Strings: ordered, immutable, text representation

my_string = "Hello World"
char = my_string[0]
print(char)
lastchar = my_string[-2]
print(my_string)
# """ -> used for multi line strings
# """ -> Used for documentation also

# accessing characters or substrings
substring = my_string[1:5]
# goes from 2 to 5
substring = my_string[0:5]
# goes from beginning to end
substring = my_string[::2]
# jumpts every 2
print(substring)

# concatenation
greeting = "Hello"
name = "Tom"
sentence = greeting + " " + name

# Print each character in string
for i in greeting:
    print(i)

# Checking for substring inside string
if 'ello' in greeting:
    print("Yes")
else:
    print("No")

my_string1 = '    Hello World     '
# Removing white space
my_string1 = my_string1.strip()
print(my_string1)

# concerting to upper case
print(my_string.upper())
print(my_string.lower())
print(my_string.startswith('world'))
print(my_string.endswith('world'))
# returns first index of the letter
print(my_string.find('o'))

print(my_string.count('o'))
print(my_string.replace('World', 'Universe'))
# VERY IMPT: looks for each space and then splits based on that
print(my_string.split(","))
print(my_string)
# join the string and the elements together
new_string = ''.join(my_string)
print(new_string)

my_list = ['a'] * 6
print(my_list)

from timeit import default_timer as timer

my_list * ['a'] * 1000000

# bad code
start = timer()
my_string = ''
for i in my_list:
    my_string += i
stop = timer()
print(stop - start)

# good code
start = timer()
my_string = ''.join(my_list)
stop = timer()
print(stop - start)

# formatting strings
var = "Tom"
my_string = "the variable is %" % var
print(my_string)

var = 3.1234567
var2 = 5.6789
my_string = f"the variable is {var} and {var2}"
print(my_string)



