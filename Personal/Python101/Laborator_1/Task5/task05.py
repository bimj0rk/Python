def zig_zag(rows, cols):

    zig_zag_matrix = []

    ################### TO DO #########################
    for a in range(rows):
        for b in range(cols):
            zig_zag_matrix[a + 1][b + 1] = 0
    
    j = 0
    
    for i in range(rows):
        zig_zag_matrix[i][j] = 1
        j += 1
        if(j == cols):
            j = 0    
    ###################################################

    return zig_zag_matrix
