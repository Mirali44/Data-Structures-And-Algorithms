"""
Problem Description:
Design a Python function named count_word_frequency to count the frequency of words in a sentence and store the counts in a dictionary.

Input: "hello world hello"
Output: {'hello': 2, 'world': 1}

Input: "the quick brown fox jumps over the lazy dog"
Output: {'the': 2, 'quick': 1, 'brown': 1, 'fox': 1, 'jumps': 1, 'over': 1, 'lazy': 1, 'dog': 1}
"""

#My Code

def count_word_frequency(sentence):
    if not sentence:
        return {}
    merge = {word:sentence.count(word) for word in sentence.split()}
    return merge

count_word_frequency("hello world hello")