test =[[1,2,3,4,5,6,7,8,9],
       [1,2,3,4,5,6,7,8,9],
       [1,2,3,4,5,6,7,8,9],
       [1,2,3,4,5,6,7,8,9],
       [1,2,3,4,5,6,7,8,9],
       [1,2,3,4,5,6,7,8,9],
       [1,2,3,4,5,6,7,8,9],
       [1,2,3,4,5,6,7,8,9],
       [1,2,3,4,5,6,7,8,9]]

def sudoku_solver(sudoku_map: list) -> list:
    rows, cols, secs = [], [[], [], [], [], [], [], [], [], []], [[], [], [], [], [], [], [], [], []]
    
    for row in sudoku_map:
        rows.append(row)
    
        for i in range(0, len(row)):
            cols[i].append(row[i])
        
        print(cols)
        
    
sudoku_solver(test)
    
    
        