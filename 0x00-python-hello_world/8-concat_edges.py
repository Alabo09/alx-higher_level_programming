#!/usr/bin/python3
# This script defines a string 'str' and concatenates specific substrings to create a new string
str = "Python is an interpreted, interactive, object-oriented programming\
         language that combines remarkable power with very clear syntax"
str = str[39:67] + str[115:120] + str[0:6]  # Concatenate specific substrings of 'str'
print(str)
