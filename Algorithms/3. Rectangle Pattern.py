"""
You are given two integers, n and m. Your task is to return a rectangle pattern of '*', where n 
represents the number of rows (length) and m represents the number of columns (breadth).

Input: n = 4, m = 5
Output: ['*****', '*****', '*****', '*****']
 
Input: n = 3, m = 2
Output: ['**', '**', '**']
"""

# My code

def generate_rectangle(n, m):
    return ["*"*m for _ in range(n)]

print(generate_rectangle(4, 5))