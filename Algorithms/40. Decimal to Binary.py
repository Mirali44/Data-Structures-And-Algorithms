"""
Problem Description:
You are given an integer n. Your task is to return its binary representation as a string. 
Do not use any built-in functions for conversion.

Input: n = 5
Output: "101"
 
Input: n = -5
Output: "-101"
"""

#My Code

def int_to_binary(n):
    if n == 0:
        return '0'
    x = ''
    b = n
    n = abs(n)
    while n>0:
        a = n%2
        n = n//2
        x = str(a) + x
        
    return '-' + x if b<0 else x

int_to_binary(5)
