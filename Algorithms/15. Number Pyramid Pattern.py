"""
Problem Description: You are given an integer n. Your task is to return a pyramid pattern of numbers, where 
each row contains increasing numbers starting from 1 up to the row number, and the pyramid is centered with 
leading spaces.


Input: 4
Output: ['   1   ', '  1 2  ', ' 1 2 3 ', '1 2 3 4']
 
Input: 3
Output: ['  1  ', ' 1 2 ', '1 2 3']
"""

# My code

def generate_number_pyramid(n):
    pattern = []

    for i in range(1, n+1): 
        new_list = []
        space = " "*(n-i)
        current = 1
        for _ in range(i):
            new_list.append(str(current))
            current +=1
        pattern.append(space + " ".join(new_list) + space)

    return pattern

print(generate_number_pyramid(4))