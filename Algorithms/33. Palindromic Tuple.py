"""
Problem Description:
Design a Python function named is_palindromic_tuple to check if a tuple is palindromic, 
meaning it reads the same forwards and backwards.

Input: (1, 2, 3, 2, 1)
Output: True

Input: ('a', 'b', 'c', 'b', 'a')
Output: True

Input: (1, 2, 3, 4, 5)
Output: False

Input: ('x', 'y', 'z', 'x')
Output: False

Input: ('a',)
Output: True
"""

#My Code

def is_palindromic_tuple(tup):
    a = list(tup)
    b = list(tup)
    a.reverse()
    
    return a == b

is_palindromic_tuple((1, 2, 3, 2, 1))