# Implement a method to perform basic string compression using the counts of repeated characters. 
# For example, the string aabcccccaaa would become a2b1c5a3. If the compressed string would not become
# smaller than the original string, your method should return original string

import sys

def count_char(string):
    
    currentchar = string[0]
    res = currentchar
    count = 0
    
    for char in string:
        if char == currentchar:
            count += 1
        else:
            res = res + str(count) + char
            currentchar = char
            count = 1
    
    res = res + str(count)
            
    return res

if __name__ == '__main__':
    print count_char(sys.argv[1])
    
    