# Given an image represented by an NxN matrix, where each pixel in the image is 4 bytes, write a method to rotate the image by 90 degrees

init_matrix = [['a','a','b','b'],
               ['a','c','d','c'],
               ['b','d','d','b'],
               ['c','a','b','d']]

rotated_matrix = [['c','b','a','a'],
                  ['a','d','c','a'],
                  ['b','d','d','b'],
                  ['d','b','c','b']]

def rotate(matrix):
    
    n = len(matrix)
    newcol = []
    
# create empty matrix NxN
    new_matrix = [[] for i in range(n)]
    print matrix
    
    for j, row in enumerate(matrix):
        for i in range(n):
            new_matrix[i].append(row[i])
       
    print new_matrix
    
# return reverse of each row in the matrix
    return [x[::-1] for x in new_matrix]
    
if __name__ == '__main__':
    result = rotate(init_matrix)
    print result
    if result == rotated_matrix:
        print '90 degree rotated successfully'
    else:
        print 'wrong rotation'