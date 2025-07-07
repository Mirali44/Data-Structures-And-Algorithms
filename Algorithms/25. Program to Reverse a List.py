"""
Problem Description:
You are given a list of integers. Write a Python program that reverses the list without using slicing (lst[::-1]). 
The program should return the reversed list.

Input: lst = [1, 2, 3, 4, 5]
Output: [5, 4, 3, 2, 1]
"""

#My Code

def reverse_list(lst):
    lst.reverse()
    return lst


reverse_list([1, 2, 3, 4, 5])