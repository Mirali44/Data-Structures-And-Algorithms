"""
Problem Description: You are given an integer n. Your task is to return a sandglass pattern of '*', where 
the first row contains 2n - 1 stars and each subsequent row decreases the number of stars by 2, until the last 
row contains a single star. After reaching the smallest width, the pattern then continues with the same 
number of stars increasing back to 2n - 1. The stars in each row should be centered.

Input: 3
Output: ['*****', ' *** ', '  *  ', ' *** ', '*****']
 
Input: 4
Output: ['*******', ' ***** ', '  ***  ', '   *   ', '  ***  ', ' ***** ', '*******']
"""

# My code

def generate_sandglass(n):
    pattern = []

    for i in range(n, 0, -1): 
       star = "*"*(2*i-1)
       space = " "*(n-i)
       pattern.append(space + star + space)
       
    half = pattern[:-1][::-1]
    pattern.extend(half)
    return pattern

print(generate_sandglass(['*****', ' *** ', '  *  ', ' *** ', '*****']))