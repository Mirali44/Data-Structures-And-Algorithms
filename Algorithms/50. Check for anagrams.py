"""
Problem Description:
You are given two strings s and t. Your task is to determine if string t is an anagram of string s. 
An anagram is a word or phrase formed by rearranging the characters of a different word or phrase, 
using all the original characters exactly once.

Input: s = "anagram", t = "nagaram"
Output: True
 
Input: s = "rat", t = "car"
Output: False
"""

#My Code

def is_anagram(s, t):
    return sorted(s) == sorted(t)

is_anagram('anagram', 'nagaram')