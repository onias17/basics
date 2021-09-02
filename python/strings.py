# STRINGS

# Basics
'hello'
"hello"
"I'm a man"

# Indexing
my_string = 'abcdef'
print(my_string[0])
print(my_string[1])
print(my_string[2])
print(my_string[-1])
print(my_string[-2])

# Slicing
print(my_string[4:]) # ef
print(my_string[:3]) # abc
print(my_string[2:5]) # cde
print(my_string[:]) # abcdef
print(my_string[::]) # abcdef
print(my_string[::1]) # abcdef
print(my_string[::2]) # ace

# Basic Methods
x = my_string.upper()
print(x)
print(x.lower())
print(x.capitalize())
l = 'onias'
print(l.split('i'))

# Print Formatting
v = 'insert another string: {}'.format('onias')
print(v)
k = 'item one {} and item two {}'.format('onias', 'israel')
print(k)
g = 'item one {x} and item two {y}'.format(y = 'onias', x = 'israel')
print(g)