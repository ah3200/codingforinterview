# Implement a function void reverse(char* str) in C or C++ which reverses a null-terminated string
import sys

def reverse(str):
    if str != "":
        return str[-1:] + reverse(str[:-1])
    else:
        return ""
    
if __name__ == '__main__':
    x = reverse(sys.argv[1])
    print x
    