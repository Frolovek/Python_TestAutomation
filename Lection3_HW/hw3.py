# https://www.python.org/dev/peps/pep-0570/#logical-ordering
# Positional-only parameters also have the (minor) benefit of enforcing some logical order when
# calling interfaces that make use of them. For example, the range function takes all its
# parameters positionally and disallows forms like:

# range(stop=5, start=0, step=2)
# range(stop=5, step=2, start=0)
# range(step=2, start=0, stop=5)
# range(step=2, stop=5, start=0)

# at the price of disallowing the use of keyword arguments for the (unique) intended order:

# range(start=0, stop=5, step=2)
"""
Write a function that accept any sequence (list, string, tuple) of unique values and then
it behaves as range function:


import string


assert = custom_range(string.ascii_lowercase, 'g') == ['a', 'b', 'c', 'd', 'e', 'f']
assert = custom_range(string.ascii_lowercase, 'g', 'p') == ['g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o']
assert = custom_range(string.ascii_lowercase, 'p', 'g', -2) == ['p', 'n', 'l', 'j', 'h']

"""
from typing import Sequence
import string


def custom_range(seq: Sequence, *args) -> list:
    result = []
    if len(args) == 1:
        if type(args[0]) == str:
            return list(seq[:seq.index(args[0])])
        elif type(args[0]) == int:
            return list(seq[:args[0]])
    if len(args) == 2:
        if type(args[0]) == str and type(args[1]) == str:
            return list(seq[seq.index(args[0]):seq.index(args[1])])
        if type(args[0]) == int and type(args[1]) == int:
            return list(seq[args[0]:args[1]])
    if len(args) == 3:
        if type(args[0]) == str and type(args[1]) == str:
            return list(seq[seq.index(args[0]):seq.index(args[1]):args[2]])
        if type(args[0]) == int and type(args[1]) == int:
            return list(seq[args[0]:args[1]:args[2]])

