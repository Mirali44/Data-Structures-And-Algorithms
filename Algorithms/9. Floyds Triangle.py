"""
Problem Description: You are given an integer n. Your task is to return the first n rows of Floyd’s Triangle, 
represented as a list of strings. Floyd's Triangle is a triangular array of natural numbers where the first 
row contains 1, the second row contains 2 and 3, the third row contains 4, 5, and 6, and so on.

Input: 5
Output: ['1', '2 3', '4 5 6', '7 8 9 10', '11 12 13 14 15']
 
Input: 3
Output: ['1', '2 3', '4 5 6']
"""

# My code

def generate_floyds_triangle(n):
    pattern = []
    current = 1 
    
    for i in range(1, n+1):
       row = [] 
       for _ in range(i):
           row.append(str(current))
           current +=1 
       pattern.append(' '.join(row))
    return pattern

print(generate_floyds_triangle(3))