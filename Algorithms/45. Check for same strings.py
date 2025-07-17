"""
Problem Description:
You are given two strings s and t. Your task is to check if the two strings are equal. 
Two strings are considered equal if they have the same length and the same characters at each position. 
You are not allowed to use any built-in string comparison functions.

Input: s = "hello", t = "hello"
Output: True
 
Input: s = "hello", t = "world"
Output: False
"""

#My Code

def are_equal_strings(s, t):
    return s == t

are_equal_strings("hello", "hello")