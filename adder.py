# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

# Function to add some numbers
# Better defaults
def add(a=0,b=0,c=0, show = False, user = False):
    if user:
        a = int(input("Enter a: "))
        b = int(input("Enter b: "))
        c = int(input("Enter c: "))
        
    ans = a+b+c
    if show:
        print(f'{a} + {b} + {c} = {ans}')
    return ans

# Print the answer to demonstrate the functionality
print(add(3,7,2, True))

# Test case
# 1,2,3 -> 6
if add(1,2,3) == 6:
    print("Test passed")
else:
    print("Test failed")

add(show = True, user = True)