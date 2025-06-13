"""
Problem Description: You are given an integer n. Your task is to return a right-angled triangle pattern 
where each row contains repeated digits. The first row contains the number 1 repeated once, the second row 
contains the number 2 repeated twice, and so on until the nth row contains the number n repeated n times.

Input: 5
Output: ['1', '22', '333', '4444', '55555']
 
Input: 3
Output: ['1', '22', '333']
"""

# My code

def generate_number_triangle(n):
    return [f"{i}"*i for i in range(1, n+1)]

print(generate_number_triangle(3))