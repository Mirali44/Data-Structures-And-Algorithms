"""
Problem Description:
You are given two strings s and t. Your task is to determine if string t is a subsequence of string s. 
A subsequence of a string is a new string that is formed from the original string 
by deleting some (or no) characters without changing the order of the remaining characters.

Input: s = "abcde", t = "ace"
Output: True
 
Input: s = "abcde", t = "aec"
Output: False
"""

#My Code

def is_subsequence(s, t):
    later = ""
    for i in s:
        if i in t:
            later += i
    if later == t:
        return True
    return False

is_subsequence("abcde", "ace")