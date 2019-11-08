
# x = input("Enter first name:")
# y = input("Enter second name:")
# import sys
#
# x = 'Raja'
# y = 'Chandra'
#
# print(x, type(x))
# print(y, type(y))
#
# # print(x - y)


# Number -> inter, float, complex
# Strings
# List
# Tuple
# Dict
# Set
# Forzanset
# Boolean
# None

# Mutable & Immutable
## Immutable
# Number -> inter, float, complex
# Strings
# Tuple
# Forzanset
# Boolean
#
# x = 1
# y = 2
# z = 3
# p = 4
# print(x + y ** z ** p)
# print(2**3)
# print(8**4)

# arthematic operators - +, - , * , /, %, //, **
# print( 3**(2**1) )

# # Relational : ==, !=, <=, >=, > , <
# x = 10
# y = 10
#
# print( x == y)  # False
# print( x != y)  # True
# print( x <= y)  # False
# print( x >= y)  # True
# print( x > y )  # True
# print( x < y )  # False

# x = 100
# print('x', x)
# y = x + 1 n
# print('y', y)
# x = x + 1
# print('x+1', x)


# # logical : and , or not
# x = 0
# y = 1
#
# print( x and y )   # 1
# print( x or y )    # 100
# print( not y )     # False

# identity : is, is not
#
# x = 1000
# y = 1000
# print(id(x), id(y))
# print( x is y )
# print( x is not y )

# abs

# x, y, z = 0, 0, 10
# print(abs(x - y))
# print(all([x, y, z]))
# print(any([x, y, z]))
#
# print(hex(100229))
#
# print(ord('A'))
# x = 69
# print(chr(x))
#
# x = 10.0
# print(isinstance(x, float))

# x = '10000000000000'
# print(len(x))

# x = max(10, 9999)
# print(x)


# x = int()
# x = 0
# print(x)

# x = int(100)
# print(x)
# x = 100
# print(x)
# x = 500
# print(x)
#
# x = 10
# y = 10
# print(id(x), id(y))
# print(x, y)
#
# del x
# print(y)
#

# Strings
# Create
# Assign
# Update
# Delete
# Access


# # create empty string
# s = '********'
# # print(s)
# s = "Hello"
# s[1] = 'E'
# print(s)
# s = str('Welcome')
# print(s)

# Access
# 1. index based -> +ve -ve
# 2. Slicing
# # 3. String function
# s = "Hello"
# print(s)
# print('index based +ve')
# print(s[0])
# print(s[1])
# print(s[2])
# print(s[3])
# print(s[4])
#
# print('index based -ve')
# print(s[-1])
# print(s[-2])
# print(s[-3])
# print(s[-4])
# print(s[-5])

# Slicing
# Syntax : [Start:Stop:step]
# s = "Hello"
# print(s)
# print(s[0:4:2])

# s[0] = 'h'
#
# s = "Hello"
# print(s)
# print(id(s))
# s2 = s.upper()
# print(s2)
# print(id(s2))

# s = "Hello"
# s[1] = 'E'


# l = list(s)
# print(l)
# l[2] = 'L'
# print(l, type(l))

# 'join'
# s = str(l)
# print(s, type(s))
# s = 'Hello' + ' Welcome'
# print(s)
# s = " ".join(['Hello', 'Welcome'])
# print(s, type(s))

# print(dir(x))
# 'capitalize', 'casefold', 'center', 'count', 'encode', 'endswith',
# 'expandtabs', 'find', 'format', 'format_map', 'index', 'isalnum',
# 'isalpha', 'isascii', 'isdecimal', 'isdigit', 'isidentifier',
# 'islower', 'isnumeric', 'isprintable', 'isspace', 'istitle',
# 'isupper',  'ljust', 'lower', 'lstrip', 'maketrans',
# 'partition', 'replace', 'rfind', 'rindex', 'rjust', 'rpartition',
# 'rsplit', 'rstrip', 'split', 'splitlines', 'startswith', 'strip',
# 'swapcase', 'title', 'translate', 'upper', 'zfill'
#
#
# s = 'python-course-training'
# l = s.split('-')
# l.remove('course')
# print('-'.join(l))

# Strip
# print(s.rstrip('*'))


# s = 'python coutse o o'
# print(s.zfill(50))
# print(s.replace('o', 'n', 4))
# print(s)

# print(s.center(50, '*'))

# print(s.isspace())
# print('{2}{1}{0}'.format(s, 'Welcome', 'AAAAA'))

# print(s.find(s[4:6]))
# print(s.startswith('Py'))
# print(s.count(s[2:7]))
# print(s.center(30, '*'))
# s = 'python'
# v = s.capitalize()
# print(s)
# print(v)
# s = 'PYTHON'
# print(s.casefold())


# l = ['a', 'b', 'c']
# l.append('d')
# print(l)
# v = l.index('d')
# print(v)


# List
# Create  - [] or list()
# Assign  - v = [] or v = list(), n = v
# Update  - append, insert
# Delete  - pop, remove, del, clear
# Access  - index
#
# l = [10, 20, 30, 40]
# l.append(50)
# print(l)
# l.insert(0, 5)
# print(l)
# l.insert(2, 35)
# print(l)

#
# l = []
# print(l)
# l = list()
# print(l)
#
# l = [10, 20, 30 ,40, 10, 30 ,40]
# print(l)
# s = {10, 20, 30 ,40, 10, 30 ,40}
# print(s)
#

# l = ['Python']
# print(l)
# l = list(['Python'])
# print(l)
#
# l = [10, 20, 30 ,40]
# print(l)
# l = list([10, 20, 30, 40])
# print(l)

# l1 = [10, 20, 30]
# l2 = ['one', 'two', 'three']
# l1.extend(l2)
# print(l1)
#
# l1 = [10, 20, 30]
# print(l1.remove(10))
# print(l1)
# print(l1.pop(0))
# print(l1)

# l1 = [10, 20, 30]
# print(len(l1))
# print(l1)
# print(l1[0:2])
# l1[0:2] = [500, 100, 600, 000, 9000]
# print(l1)
# print(len(l1))

# t1 = (10, 20, 30)
# t1[2] = 300
# print(t1)

# l1 = [10, 30, 50, 40, 40, 30]
# print(l1.count(30))
# print(l1.index(400))

# clear, pop, remove, del
# l1 = [10, 30, 50, 40, 40, 30]
# v = l1.clear()
# v = l1.pop()
# v = l1.remove(30)
# del l1
# print(l1)

l1 = [10, 30, 50, 40, 40, 30]
# v = l1.sort()
v = l1.reverse()
print(v, l1)

# v = sorted(l1, reverse=True)
v = list(reversed(l1))
print(v)


# deleting
# 'append', 'clear', 'copy', 'count', 'extend',
# 'index', 'insert', 'pop', 'remove', 'reverse', 'sort'

# Functions
#
# def display():
#     print('Calling display')
#     # return "Display"
#
# v = display()
# print(v)

