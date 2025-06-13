"""
Problem Description: You are given an integer n. Your task is to return a right-angled triangle pattern of '*' 
where each side has n characters, represented as a list of strings. The triangle has '*' characters, starting
with 1 star in the first row, 2 stars in the second row, and so on until the last row has n stars.

Input: 3
Output: ['*', '**', '***']
 
Input: 5
Output: ['*', '**', '***', '****', '*****']
"""

# My code

def generate_triangle(n):
    return ["*"*(i+1) for i in range(n)]

print(generate_triangle(3))