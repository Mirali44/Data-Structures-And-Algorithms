"""
Problem Description:
You are given two integers n and m. Your task is to find the GCD of these two numbers. 
The GCD is the largest positive integer that divides both numbers without leaving a remainder. 
Do not use any built-in functions and do not use recursion.

Input: n = 48, m = 18
Output: 6
 
Input: n = 56, m = 98
Output: 14
"""

#My Code

def gcd(n, m):
    a = min([n,m])
    
    for i in range(a, 0, -1):
        if n%i == 0 and m%i == 0:
            return i 
            break
        
gcd(48,18)