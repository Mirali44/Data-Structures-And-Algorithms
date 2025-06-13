"""
Problem Description: You are given an integer n. Your task is to return a right-angled triangle 
pattern of '*', where each row contains stars aligned to the right. The first row has one star, the second 
row has two stars, and so on, until the nth row has n stars.

Input: 4
Output: ['   *', '  **', ' ***', '****']
 
Input: 3
Output: ['  *', ' **', '***']
"""

# My code

def generate_right_angled_triangle(n):
    pattern = []

    for i in range(1, n+1): 
        star = "*"*i
        space = " "*(n-i)
        pattern.append(space + star)
    return pattern

print(generate_right_angled_triangle(['   *', '  **', ' ***', '****']))