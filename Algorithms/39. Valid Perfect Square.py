"""
Problem Description:
You are given a positive integer num. Your task is to check whether num is a 
perfect square or not. A perfect square is an integer that is the square of 
an integer (e.g., 1, 4, 9, 16, ...). Return True if num is a perfect square, and False otherwise.

Input: num = 16
Output: True
 
Input: num = 14
Output: False
"""

#My Code

def is_perfect_square(num):
    i = 1 
    
    while i*i <= num:
        if i*i == num:
            return True
        i += 1 
    return False
            
is_perfect_square(16)
