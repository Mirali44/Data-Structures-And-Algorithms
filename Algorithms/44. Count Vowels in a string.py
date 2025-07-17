"""
Problem Description:
You are given a string s. Your task is to count the number of vowels (both uppercase and lowercase) 
in the stringand return the total count.

Input: "Hello, World!"
Output: 3
 
Input: "Python Programming"
Output: 4
"""

#My Code

def count_vowels(s):
    a = ["a", "e", "i", "o", "u"]
    count = 0
    for i in s.lower():
        if i in a:
            count += 1
    return count

count_vowels("Hello, World!")