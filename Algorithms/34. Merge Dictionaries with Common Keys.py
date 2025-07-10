"""
Problem Description:
Design a Python function named merge_dicts_with_overlapping_keys that merges multiple dictionaries into a single dictionary. 
If a key appears in more than one dictionary, sum up their values.

Input: [{'a': 1, 'b': 2}, {'b': 3, 'c': 4}, {'c': 5, 'd': 6}]
Output: {'a': 1, 'b': 5, 'c': 9, 'd': 6}

Input: [{'x': 10, 'y': 20}, {'y': 30, 'z': 40}, {'z': 50, 'x': 60}]
Output: {'x': 70, 'y': 50, 'z': 90}
"""

#My Code

def merge_dicts_with_overlapping_keys(dicts):
    merge = {}
    for i in dicts:
        for key, value in i.items():
            if key in merge:
                merge[key] += value
            else:
                merge[key] = value
    return merge
        
merge_dicts_with_overlapping_keys([{'a': 1, 'b': 2}, {'b': 3, 'c': 4}, {'c': 5, 'd': 6}])