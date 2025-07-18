"""
Problem Description:
You are given a string s. Your task is to find the length of the longest word in the string. 
A word is defined as a sequence of characters separated by spaces. 
Do not use any built-in functions for string manipulation.

Input: s = "The quick brown fox jumps over the lazy dog"
Output: 5
 
Input: s = "Hello World"
Output: 5
"""

#My Code

def longest_word_length(s):
    a = []
    if s == " ":
        return False
    else:
        for i in s.split():
            a.append(len(i))
        return max(a)

longest_word_length("The quick brown fox jumps over the lazy dog")