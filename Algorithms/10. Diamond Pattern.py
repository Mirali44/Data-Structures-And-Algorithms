"""
Problem Description:

You are given an integer n. Your task is to return a diamond pattern of '*' with n rows for the upper part 
(the widest row will have 2n - 1 stars), and the lower part is the mirrored version of the upper part. 
Each row should be centered with appropriate spaces.

Input: 3
Output: ['  *  ', ' *** ', '*****', ' *** ', '  *  ']
 
Input: 5
Output: ['    *    ', '   ***   ', '  *****  ', ' ******* ', '*********', ' ******* ', '  *****  ', '   ***   ', '    *    ']
"""

# My code

def generate_diamond(n):
    pattern = []

    for i in range(n): 
       star = "*"*(2*i+1)
       space = " "*(n-i-1)
       pattern.append(space + star + space)
    
    half = pattern[:-1][::-1]
    pattern.extend(half)
    return pattern

print(generate_diamond(3))