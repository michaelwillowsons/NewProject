
def multi(a,b):
	ans = a*b
	return ans



# Test case
# 3*9 -> 27
if multi(3,9) == 27:
    print("Test #1 Passed")

# Test case
# three*4 -> nameerror
try:
    multi(three, 4)
except NameError:
    print("Test #2 Passed")