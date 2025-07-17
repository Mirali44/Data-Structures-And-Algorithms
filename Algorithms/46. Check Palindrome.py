"""
Problem Description:
You are given a string s. Your task is to check if the string is a palindrome. 
A string is considered a palindrome if it reads the same forward and backward, ignoring spaces, punctuation, and case.

Input: "A man a plan a canal Panama"
Output: True
 
Input: "Hello, World!"
Output: False
"""

#My Code

def is_palindrome(s):
    a = s.split()
    return "".join(a).lower() == "".join(a)[::-1].lower()

is_palindrome("A man a plan a canal Panama")