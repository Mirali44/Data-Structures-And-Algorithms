"""
Problem Description: You are given an integer n. Your task is to return a square pattern of size n x n made up 
of the character '*', represented as a list of strings.

Input: 3
Output: ['***', '***', '***']
 
Input: 5
Output: ['*****', '*****', '*****', '*****', '*****']
"""

# My Code
def generate_square(n):
    return ["*"*n for _ in range(n)]


print(generate_square(3))