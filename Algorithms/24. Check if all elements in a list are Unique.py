"""
Problem Description:
You are given a list of integers. Write a Python program that checks if all elements in the list are unique. 
If all elements are unique, return True; otherwise, return False.

Input: lst = [1, 2, 3, 4, 5]
Output: True

Input: lst = [1, 2, 3, 3, 4, 5]
Output: False
"""

#My Code

def check_unique(lst):
    return lst == list(set(lst))

check_unique([1, 2, 3, 3, 4, 5])