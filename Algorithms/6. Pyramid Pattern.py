"""
Problem Description: You are given an integer n. Your task is to return a pyramid pattern of '*' where 
each side has n rows, represented as a list of strings. The pyramid is centered, with 1 star in the first row, 
3 stars in the second row, and so on, increasing by 2 stars per row until the base row has 2n - 1 stars.

Input: 3
Output: ['  *  ', ' *** ', '*****']
 
Input: 5
Output: ['    *    ', '   ***   ', '  *****  ', ' ******* ', '*********']
"""

# My code

def generate_pyramid(n):
    pattern = []
    for i in range(n):
        star = "*"*(2*i+1)
        space = " "*(n-i-1)
        pattern.append(space + star + space)
    return pattern

print(generate_pyramid(3))