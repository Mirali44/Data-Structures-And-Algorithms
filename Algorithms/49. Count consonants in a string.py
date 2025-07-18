"""
Problem Description:
You are given a string s. 
Your task is to count the number of consonants in the string and return the total count. 
A consonant is any alphabetic character that is not a vowel (a, e, i, o, u).

Input: "Hello, World!"
Output: 7
 
Input: "Python Programming"
Output: 13
"""

#My Code

def count_consonants(s):
    return sum([1 for i in s.upper() if i in "BCDFGHJKLMNPQRSTVWXYZ"])


count_consonants("Python Programming")