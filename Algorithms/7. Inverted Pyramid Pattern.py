"""
Problem Description: You are given an integer n. Your task is to return an inverted pyramid pattern of '*', 
where each side has n rows, represented as a list of strings. The first row has 2n - 1 stars, the second row 
has 2n - 3 stars, and so on, until the last row has 1 star, with each row centered using spaces.

Input: 3
Output: ['*****', ' *** ', '  *  ']
 
Input: 5
Output: ['*********', ' ******* ', '  *****  ', '   ***   ', '    *    ']
"""

# My code

def generate_inverted_pyramid(n):
    pattern = []
    
    for i in range(n-1, -1, -1):
       star = "*"*(2*i + 1)
       space = " "*(n-i - 1)
       pattern.append(space + star + space)
    return pattern

print(generate_inverted_pyramid(3))