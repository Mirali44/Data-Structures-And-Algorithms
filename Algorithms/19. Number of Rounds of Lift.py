"""
Problem Description:
You are given n, the total number of people, and capacity, the maximum number of people the lift can carry at a time. 
All people want to go from the ground floor to the top floor. 
Your task is to calculate the number of rounds the lift has to make to transport all the people to the top floor.

Input: n = 10, capacity = 3
Output: 4
 
Input: n = 7, capacity = 4
Output: 2
"""

#My Code

def calculate_lift_rounds(n, capacity):
    return (n+capacity-1)//capacity

calculate_lift_rounds(8, 4)