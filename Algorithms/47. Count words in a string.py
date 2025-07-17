"""
Problem Description:
You are given a string s. Your task is to count the number of words in the string and return the total count. 
A word is defined as a sequence of characters separated by spaces.

Input: "Hello, World!"
Output: 2
 
Input: "Python programming is fun."
Output: 4
"""

#My Code

def count_words(s):
    return len(s.split())


count_words("Hello, World!")