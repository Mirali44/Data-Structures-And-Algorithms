"""
Problem Description:
You are given a list of integers and an integer k. Write a Python function to rotate the list to the right by k positions 
without using slicing. A rotation shifts elements from the end of the list to the front.

Input: lst = [1, 2, 3, 4, 5], k = 2
Output: [4, 5, 1, 2, 3]

Input: lst = [10, 20, 30, 40, 50], k = 3
Output: [30, 40, 50, 10, 20]
"""

#My Code

def rotate_list(lst, k):
    if not lst:
        return []
        
    for _ in range(k%len(lst)):
        num = lst.pop()
        lst.insert(0, num)
    return lst
        
rotate_list([1, 2, 3, 4, 5], 2)