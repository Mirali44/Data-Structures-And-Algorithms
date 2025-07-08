"""
Problem Description:
You are given a list of integers. Write a Python program to find the maximum difference between two consecutive elements
in the list using a brute-force approach. The difference is defined as the absolute value of the difference between 
two consecutive elements.

Input: lst = [1, 7, 3, 10, 5]
Output: 7

Input: lst = [10, 11, 15, 3]
Output: 12
"""

#My Code

def max_consecutive_difference(lst):
    return max([abs(lst[i] - lst[i + 1]) for i in range(len(lst) - 1)]) if len(lst) > 1 else 0

max_consecutive_difference([1, 7, 3, 10, 5])