"""
Problem Description:
You are given two sorted lists of integers. Write a Python function to merge these two sorted lists into one sorted list. 
The resulting list should also be in non-decreasing order.

Input: list1 = [1, 3, 5], list2 = [2, 4, 6]
Output: [1, 2, 3, 4, 5, 6]

Input: list1 = [1, 4, 7], list2 = [2, 3, 5, 8]
Output: [1, 2, 3, 4, 5, 7, 8]
"""

#My Code

def merge_two_sorted_lists(list1, list2):
    list1.extend(list2)
    return sorted(list1)

merge_two_sorted_lists([1, 3, 5], [2, 4, 6])