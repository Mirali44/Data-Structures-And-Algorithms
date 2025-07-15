"""
Problem Description:
You are given an integer n. Your task is to check whether the number is prime or not. 
A prime number is a number greater than 1 that has no divisors other than 1 and itself. 
Return True if the number is prime, and False otherwise.

Input: n = 5
Output: True
 
Input: n = 4
Output: False
"""

#My Code

def is_prime(n):
    for i in range(2, int(n*0.5)+1):
        if n%i == 0:
            return False
    
    return True
        
is_prime(5)
