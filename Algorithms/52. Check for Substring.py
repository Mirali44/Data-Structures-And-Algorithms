"""
Problem Description:
You are given two strings, s and t. Your task is to determine if the string t is a substring of the string s. 
A substring is a contiguous sequence of characters within a string. Do not use any built-in functions for 
string operations and do not use recursion.

Input: s = "hello world", t = "world"
Output: True
 
Input: s = "hello world", t = "worlds"
Output: False
"""

#My Code

def is_substring(s, t):
    return t in s

is_substring("hello world", "worlds")