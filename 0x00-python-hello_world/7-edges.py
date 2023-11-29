#!/usr/bin/python3
# This script defines a string 'word' and extracts its first 3 letters, last 2 letters, and the middle word.
word = "Holberton"
word_first_3 = word[:3]  # Extract the first 3 letters of 'word'
word_last_2 = word[-2:]  # Extract the last 2 letters of 'word'
middle_word = word[1:-1]  # Extract the middle word of 'word'
print(f"First 3 letters: {word_first_3}")
print(f"Last 2 letters: {word_last_2}")
print(f"Middle word: {middle_word}")
