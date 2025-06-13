"""
Problem Description: You are given an integer n. Your task is to return a hollow inverted right-angled 
triangle pattern of '*', where the first row contains n stars, while the inner rows contain a star at the 
beginning and end, with spaces in between. The triangle should be left-aligned.

Input: 4
Output: ['****', '* *', '**', '*']
 
Input: 5
Output: ['*****', '*  *', '* *', '**', '*']
"""

# My code

def generate_hollow_inverted_right_angled_triangle(n):
    pattern = []

    for i in range(n, 0, -1): 
       star = "*"*i
       if i>2 and i<n:
           space = " "*(i-2)
           pattern.append("*"+ space + "*")
       else:
           pattern.append(star)

    return pattern

print(generate_hollow_inverted_right_angled_triangle(['****', '* *', '**', '*']))