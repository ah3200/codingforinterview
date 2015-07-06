# Write an algorithm such that if an element in an MxN matrix is 0, its entire row and column are set to 0

init_matrix = [[2,4,0,5,1],
               [1,3,4,5,6],
               [4,4,0,6,7],
               [2,3,3,7,7]]

def zerolize(matrix):
    
    index = []
    
    result = [x for x in matrix]

    for n, row in enumerate(matrix):
        print row
        for m, col in enumerate(row):
            print col
            if col == 0:
                for i in range(len(result)):
#                    result[i][m] = 0
                    index.append([i,m])
                for j in range(len(result[n])):
#                    result[n][j] = 0
                    index.append([n,j])
            print result    
        
    for loc in index:
        x = loc[0]
        y = loc[1]
        
        result[x][y] = 0
        
    return result

if __name__ == '__main__':
    result = zerolize(init_matrix)
    print result
    
    