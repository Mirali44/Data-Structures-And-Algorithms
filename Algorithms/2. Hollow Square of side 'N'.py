"""
Problem Description: You are given an integer n. Your task is to return a hollow square pattern of size 
n x n made up of the character '*', represented as a list of strings. The hollow square has '*' on the border, 
and spaces ' ' in the middle (except for side lengths of 1 and 2)

Input: 3
Output: ['***', '* *', '***']
 
Input: 5
Output: ['*****', '*   *', '*   *', '*   *', '*****']
"""

# My code

def generate_hollow_square(n):
    lst = ['*' * n] 
    if n >= 2:
        for i in range(n-2):
            lst.append('*' + ' ' * (n-2) + '*')
        lst.append('*' * n)
    
    return lst 

print(generate_hollow_square(3))