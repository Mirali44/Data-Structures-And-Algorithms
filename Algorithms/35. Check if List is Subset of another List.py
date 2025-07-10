"""
Problem Description:
You are given two lists of integers. Write a Python program that checks whether the first list 
is a subset of the second list using a brute-force approach, without using the in keyword. 
A list is considered a subset if all elements of the first list are present in the second list.

Input: lst1 = [1, 2, 3], lst2 = [1, 2, 3, 4, 5]
Output: True

Input: lst1 = [1, 6], lst2 = [1, 2, 3, 4, 5]
Output: False
"""

#My Code

def is_subset(lst1, lst2):
    return all(i in lst2 for i in lst1)

is_subset([1, 2, 3],[1, 2, 3, 4, 5])