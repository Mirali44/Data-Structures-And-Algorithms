"""
Problem Description: You are given an integer n. Your task is to return a hollow right-angled triangle 
pattern of '*', where the first and last rows contain stars, while the inner rows contain a star at the 
beginning and end, with spaces in between. The triangle should be right-aligned.

Input: 4
Output: ['*', '**', '* *', '****']
 
Input: 5
Output: ['*', '**', '* *', '*  *', '*****']
"""

# My code

def generate_hollow_right_angled_triangle(n):
    pattern = []

    for i in range(1, n+1): 
        star = "*"*i
        if i>2 and i<n:
           space = " "*(i-2)
           pattern.append("*"+ space + "*")
        else:
           pattern.append(star)

    return pattern

print(generate_hollow_right_angled_triangle(['*', '**', '* *', '****']))