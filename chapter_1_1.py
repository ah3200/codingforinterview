# Implement an algorithm to determin if a string has all unique characters. What if you cannot use additional data structures
import sys

input = sys.argv[1]

x = 0

for char in input:
    if input.count(char) > 1:
        x = 1
    else:
        x = 0
    
if x == 0:
    print "The input string has all unique characters"
else:
    print "The input string has not all unique characters"