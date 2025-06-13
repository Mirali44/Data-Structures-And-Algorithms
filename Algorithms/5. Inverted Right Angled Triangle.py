"""
Problem Description: You are given an integer n. Your task is to return an inverted right-angled triangle 
pattern of '*' where each side has n characters, represented as a list of strings. The first row should have 
n stars, the second row n-1 stars, and so on, until the last row has 1 star.

Input: 3
Output: ['***', '**', '*']
 
Input: 5
Output: ['*****', '****', '***', '**', '*']
"""

# My code

def generate_inverted_triangle(n):
    return ["*"*i for i in range(n,0,-1)]

print(generate_inverted_triangle(3))