# Write a method to replace all spaces in a string with '%20'. You may assume that the string has sufficient space
# at the end of the string to hold the additional characters, and that you are given the "true" length of the string.
# EXAMPLE: 
# input: "Mr John Smith   "
# output: "Mr%20John%20Smith"

import sys

def replace(str):
    print str
    w = '%20'
    ns = str.rstrip()
    print ns
    return ns.replace(" ",w)

if __name__ == '__main__':
    print replace(sys.argv[1])