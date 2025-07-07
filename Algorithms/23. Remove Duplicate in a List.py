"""
Problem Description:
You are given a list of integers. Write a Python program that removes any duplicate elements from the list and 
returns a new list with only unique elements. The order of elements in the list should be maintained.

Input: lst = [1, 2, 2, 3, 4, 4, 5]
Output: [1, 2, 3, 4, 5]

Input: lst = [4, 5, 5, 4, 6, 7]
Output: [4, 5, 6, 7]
"""

#My Code

def remove_duplicates(lst):
    return list(set(lst))

remove_duplicates([1, 2, 2, 3, 4, 4, 5])