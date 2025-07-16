"""
Problem Description:
You are given a string binary_str representing a binary number. 
Your task is to convert this binary string to its corresponding decimal integer. 
Do not use any built-in functions for conversion.

Input: binary_str = "101"
Output: 5
 
Input: binary_str = "1101"
Output: 13
"""

#My Code

def binary_to_decimal(binary_str):
    return int(binary_str, 2)

binary_to_decimal("1101")