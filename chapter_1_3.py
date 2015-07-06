# Given two strings, write a method to decide if one is permutation of the other
import sys

def compare_permutation(str1, str2):
    words1 = [c for c in str1]
    words2 = [c for c in str2]
    words1.sort()
    words2.sort()
    
#   words1 = sorted(str1) 
#   words2 = sorted(str2)
 
    if words1 == words2:
        return True

if __name__ == '__main__':
    if compare_permutation(sys.argv[1],sys.argv[2]) == True:
        print "One string is permutation of the another"
    else:
        print "Not permutation"