# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

# Function to add some numbers
# Better defaults
def add(a=0,b=0,c=0):
    ans = a+b+c
    return ans

# Print the answer to demonstrate the functionality
print(add(3,7,2))

# Test case
# 1,2,3 -> 6
if add(1,2,3) == 6:
    print("Test passed")
else:
    print("Test failed")