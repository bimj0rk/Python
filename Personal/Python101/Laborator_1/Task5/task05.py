def zig_zag(rows, cols):

    zig_zag_matrix = []

    ################### TO DO #########################
    for i in range(rows):
        row = [0] * cols  
        
        col_index = i % (2 * (cols - 1))
         
        if col_index >= cols:
            col_index = 2 * (cols - 1) - col_index  
            
        row[col_index] = 1  
        zig_zag_matrix.append(row)
    ##################################

    return zig_zag_matrix