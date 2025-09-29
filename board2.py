def printBoard(grid):
    print("+---+---+---+---+---+---+") 
    for row in range(len(grid)):
        print("|   |   |   |   |   |   |")
        print("+---+---+---+---+---+---+")
    print("  0   1   2   3   4   5  ") 


def print_game_board(grid):
    for row in range(len(grid)):
        print("+---+---+---+---+---+---+")
        print("|", end="")
        for col in range(len(grid[0])):
            if grid[row][col] == 0:
                print("   |", end="")
            elif grid[row][col] == 'X':
                print(" X |", end="")
            elif grid[row][col] == 'O':
                print(" O |", end="")
        print()  
    print("+---+---+---+---+---+---+") 
    print("  0   1   2   3   4   5  ")



def choice(play, col, grid, col0, col1, col2, col3, col4, col5):
    
    col = int(col)
    if col == 0:
        if 6 in col0:
            if play == 1:
                grid[6][0] = 'X'
            elif play == 2:
                grid[6][0] = 'O'
            col0.remove(6)
        elif 5 in col0:
            if play == 1:
                grid[5][0] = 'X'
            elif play == 2:
                grid[5][0] = 'O'
            col0.remove(5)
        elif 4 in col0:
            if play == 1:
                grid[4][0] = 'X'
            elif play == 2:
                grid[4][0] = 'O'
            col0.remove(4)
        elif 3 in col0:
            if play == 1:
                grid[3][0] = 'X'
            elif play == 2:
                grid[3][0] = 'O'
            col0.remove(3)
        elif 2 in col0:
            if play == 1:
                grid[2][0] = 'X'
            elif play == 2:
                grid[2][0] = 'O'
            col0.remove(2)
        elif 1 in col0:
            if play == 1:
                grid[1][0] = 'X'
            elif play == 2:
                grid[1][0] = 'O'
            col0.remove(1)
        elif 0 in col0:
            if play == 1:
                grid[0][0] = 'X'
            elif play == 2:
                grid[0][0] = 'O'
            col0.remove(0)
        else:
            print("Column is Full. Invalid Choice")
        
    elif col == 1:
        if 6 in col1:
            if play == 1:
                grid[6][1] = 'X'
            elif play == 2:
                grid[6][1] = 'O'
            col1.remove(6)
        elif 5 in col1:
            if play == 1:
                grid[5][1] = 'X'
            elif play == 2:
                grid[5][1] = 'O'
            col1.remove(5)
        elif 4 in col1:
            if play == 1:
                grid[4][1] = 'X'
            elif play == 2:
                grid[4][1] = 'O'
            col1.remove(4)
        elif 3 in col1:
            if play == 1:
                grid[3][1] = 'X'
            elif play == 2:
                grid[3][1] = 'O'
            col1.remove(3)
        elif 2 in col1:
            if play == 1:
                grid[2][1] = 'X'
            elif play == 2:
                grid[2][1] = 'O'
            col1.remove(2)
        elif 1 in col1:
            if play == 1:
                grid[1][1] = 'X'
            elif play == 2:
                grid[1][1] = 'O'
            col1.remove(1)
        elif 0 in col1:
            if play == 1:
                grid[0][1] = 'X'
            elif play == 2:
                grid[0][1] = 'O'
            col1.remove(0)
        else:
            print("Column is Full. Invalid Choice")
        
    elif col == 2:
        if 6 in col2:
            if play == 1:
                grid[6][2] = 'X'
            elif play == 2:
                grid[6][2] = 'O'
            col2.remove(6)
        elif 5 in col2:
            if play == 1:
                grid[5][2] = 'X'
            elif play == 2:
                grid[5][2] = 'O'
            col2.remove(5)
        elif 4 in col2:
            if play == 1:
                grid[4][2] = 'X'
            elif play == 2:
                grid[4][2] = 'O'
            col2.remove(4)
        elif 3 in col2:
            if play == 1:
                grid[3][2] = 'X'
            elif play == 2:
                grid[3][2] = 'O'
            col2.remove(3)
        elif 2 in col2:
            if play == 1:
                grid[2][2] = 'X'
            elif play == 2:
                grid[2][2] = 'O'
            col2.remove(2)
        elif 1 in col2:
            if play == 1:
                grid[1][2] = 'X'
            elif play == 2:
                grid[1][2] = 'O'
            col2.remove(1)
        elif 0 in col2:
            if play == 1:
                grid[0][2] = 'X'
            elif play == 2:
                grid[0][2] = 'O'
            col2.remove(0)
        else:
            print("Column is Full. Invalid Choice")
        
    elif col == 3:
        if 6 in col3:
            if play == 1:
                grid[6][3] = 'X'
            elif play == 2:
                grid[6][3] = 'O'
            col3.remove(6)
        elif 5 in col3:
            if play == 1:
                grid[5][3] = 'X'
            elif play == 2:
                grid[5][3] = 'O'
            col3.remove(5)
        elif 4 in col3:
            if play == 1:
                grid[4][3] = 'X'
            elif play == 2:
                grid[4][3] = 'O'
            col3.remove(4)
        elif 3 in col3:
            if play == 1:
                grid[3][3] = 'X'
            elif play == 2:
                grid[3][3] = 'O'
            col3.remove(3)
        elif 2 in col3:
            if play == 1:
                grid[2][3] = 'X'
            elif play == 2:
                grid[2][3] = 'O'
            col3.remove(2)
        elif 1 in col3:
            if play == 1:
                grid[1][3] = 'X'
            elif play == 2:
                grid[1][3] = 'O'
            col3.remove(1)
        elif 0 in col3:
            if play == 1:
                grid[0][3] = 'X'
            elif play == 2:
                grid[0][3] = 'O'
            col3.remove(0)
        else:
            print("Column is Full. Invalid Choice")
       
    elif col == 4:
        if 6 in col4:
            if play == 1:
                grid[6][4] = 'X'
            elif play == 2:
                grid[6][4] = 'O'
            col4.remove(6)
        elif 5 in col4:
            if play == 1:
                grid[5][4] = 'X'
            elif play == 2:
                grid[5][4] = 'O'
            col4.remove(5)
        elif 4 in col4:
            if play == 1:
                grid[4][4] = 'X'
            elif play == 2:
                grid[4][4] = 'O'
            col4.remove(4)
        elif 3 in col4:
            if play == 1:
                grid[3][4] = 'X'
            elif play == 2:
                grid[3][4] = 'O'
            col4.remove(3)
        elif 2 in col4:
            if play == 1:
                grid[2][4] = 'X'
            elif play == 2:
                grid[2][4] = 'O'
            col4.remove(2)
        elif 1 in col4:
            if play == 1:
                grid[1][4] = 'X'
            elif play == 2:
                grid[1][4] = 'O'
            col4.remove(1)
        elif 0 in col4:
            if play == 1:
                grid[0][4] = 'X'
            elif play == 2:
                grid[0][4] = 'O'
            col4.remove(0)
        else:
            print("Column is Full. Invalid Choice")
        
    elif col == 5:
        if 6 in col5:
            if play == 1:
                grid[6][5] = 'X'
            elif play == 2:
                grid[6][5] = 'O'
            col5.remove(6)
        elif 5 in col5:
            if play == 1:
                grid[5][5] = 'X'
            elif play == 2:
                grid[5][5] = 'O'
            col5.remove(5)
        elif 4 in col5:
            if play == 1:
                grid[4][5] = 'X'
            elif play == 2:
                grid[4][5] = 'O'
            col5.remove(4)
        elif 3 in col5:
            if play == 1:
                grid[3][5] = 'X'
            elif play == 2:
                grid[3][5] = 'O'
            col5.remove(3)
        elif 2 in col5:
            if play == 1:
                grid[2][5] = 'X'
            elif play == 2:
                grid[2][5] = 'O'
            col5.remove(2)
        elif 1 in col5:
            if play == 1:
                grid[1][5] = 'X'
            elif play == 2:
                grid[1][5] = 'O'
            col5.remove(1)
        elif 0 in col5:
            if play == 1:
                grid[0][5] = 'X'
            elif play == 2:
                grid[0][5] = 'O'
            col5.remove(0)
        else:
            print("Column is Full. Invalid Choice")
    
    return grid, col0, col1, col2, col3, col4, col5

def win(grid):
    #Checks Horizontal
    for row in range(len(grid)):
        for col in range(len(grid[0]) - 3):
            if grid[row][col] == 'X' or grid[row][col] == 'O':
                if grid[row][col] == grid[row][col + 1] == grid[row][col + 2] == grid[row][col + 3]:
                    if grid[row][col] == 'X':
                        print("Player 1 Wins")
                    else:
                        print("Player 2 Wins")
                    return True
    
    #Checks Vertical
    for col in range(len(grid[0])):
        for row in range(len(grid) - 3):
            if grid[row][col] == 'X' or grid[row][col] == 'O':
                if grid[row][col] == grid[row + 1][col] == grid[row + 2][col] == grid[row + 3][col]:
                    if grid[row][col] == 'X':
                        print("Player 1 Wins")
                    else:
                        print("Player 2 Wins")
                    return True
    #Checks Positive Slope Diaganol          
    for row in range(3, len(grid)):
        for col in range(len(grid[0]) - 3):
            if grid[row][col] == 'X' or grid[row][col] == 'O':
                if grid[row][col] == grid[row - 1][col + 1] == grid[row - 2][col + 2] == grid[row - 3][col +3]:
                    if grid[row][col] == 'X':
                        print("Player 1 Wins")
                    else:
                        print("Player 2 Wins")
                    return True
    #Checks Negative Slope Diaganol
    for row in range(len(grid) - 3):
        for col in range(len(grid[0])):
            if grid[row][col] == 'X' or grid[row][col] == 'O':
                if col < 4:
                    if grid[row][col] == grid[row + 1][col + 1] == grid[row + 2][col + 2] == grid[row + 3][col +3]:
                        if grid[row][col] == 'X':
                            print("Player 1 Wins")
                        else:
                            print("Player 2 Wins")
                        return True
    #Checks if There Was a Tie
    for row in range(len(grid)):
        for col in range(len(grid[0])):
            if grid[row][col] == 0:
                return False
    print("Tie!")
            
    return False
    
    