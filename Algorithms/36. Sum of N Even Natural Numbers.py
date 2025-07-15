"""
Problem Description:
You are given an integer n. Your task is to calculate and return the sum of the first
n even natural numbers. The even natural numbers are: 2, 4, 6, 8, ...

Input: n = 3
Output: 12  # (2 + 4 + 6)
 
Input: n = 5
Output: 30  # (2 + 4 + 6 + 8 + 10)
"""

#My Code

def sum_of_even_numbers(n):
    x = 0
    b = 0
    for _ in range(n):
        x += 2
        b += x
    return b
    
sum_of_even_numbers(3)