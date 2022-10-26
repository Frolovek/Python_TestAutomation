# 1. Implement a function that flatten incoming data:
# non-iterables and elements from iterables (any nesting depth should be supported)
# function should return an iterator (generator function)
# don't use third-party libraries

def merge_elems(*elems):
    for elem in elems:
        if hasattr(elem, '__iter__'):
            for i in elem:
                if hasattr(i, '__iter__') and not isinstance(i, str):
                    yield from merge_elems(i)
                else:
                    yield i
        else:
            yield elem



# example input
a = [1, 2, 3]
b = 6
c = 'zhaba'
d = [[1, 2], [3, 4]]

for _ in merge_elems(a, b, c, d):
    print(_, end=' ')

print('\n' + 'zhaba is finally in a swamp and feel comfortable')

# output: 1 2 3 6 z h a b a 1 2 3 4

# 2. Implement a map-like function that returns an iterator (generator function)
# extra functionality: if arg function can't be applied, return element as is + text exception

def map_like(fun, *elems):
    for elem in elems:
        if hasattr(elem, '__iter__'):
            yield fun(elem)
        else:
            print(str(elem) + ':', f"'{type(elem).__name__}'", "object is not subscriptable")


# example input
a = [1, 2, 3]
b = 6
c = 'zhaba'
d = True
fun = lambda x: x[0]

for _ in map_like(fun, a, b, c, d):
    print(_)

# output:
# 1
# 6: 'int' object is not subscriptable
# z
# True: 'bool' object is not subscriptable