# Name: Liliana Holguin
# Date: April 30, 2024
# Course: ET 362
# Assignment: Project 3: OOP Basics
# Description: An interactive 2 player Connect 4 Game
# Preconditions: User input
# Postcondition: Prints Connect 4 Board

import player
import board2


#GAME BEGINS
print("WELCOME TO 2-PLAYER CONNECT-4!")
want_play = input("Would You Like To Play? Y/N\nChoice: ")
while ((want_play != 'Y') and (want_play !='y') and (want_play != 'N') and (want_play != 'n')):
    print("Invalid input!")
    want_play = input("Would You Like To Play? Y/N\nChoice: ")

while ((want_play == 'Y') or (want_play =='y') or (want_play == 'N') or (want_play == 'n')):
    if ((want_play == 'Y') or (want_play =='y')):
        #INITIALIZES CONNECT 4 GRID
        grid = [[0, 0, 0, 0, 0, 0], 
                [0, 0, 0, 0, 0, 0], 
                [0, 0, 0, 0, 0, 0], 
                [0, 0, 0, 0, 0, 0], 
                [0, 0, 0, 0, 0, 0], 
                [0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0]] 

        #Initialize Columns for Choice Function
        col0 = [6, 5, 4, 3, 2, 1, 0]
        col1 = [6, 5, 4, 3, 2, 1, 0]
        col2 = [6, 5, 4, 3, 2, 1, 0]
        col3 = [6, 5, 4, 3, 2, 1, 0]
        col4 = [6, 5, 4, 3, 2, 1, 0]
        col5 = [6, 5, 4, 3, 2, 1, 0]

        #INITIALIZES PLAYERS
        p1 = player.Player("Player 1", 'X')
        p2 = player.Player("Player 2", 'O')

        #PRINTS BOARD
        board2.printBoard(grid)

        #BEGIN WITH PLAYER 1
        move = 1
        #BEGIN WITH NO WINNER
        winner = False

        while winner == False:
            #player1 turn
            if (move % 2 != 0): 
                play = 1
                col = p1.move()
                grid, col0, col1, col2, col3, col4, col5 = board2.choice(play, col, grid, col0, col1, col2, col3, col4, col5)
                board2.print_game_board(grid)
                winner = board2.win(grid)
            #player2 turn
            elif (move % 2 == 0): 
                play = 2
                col = p2.move()
                grid, col0, col1, col2, col3, col4, col5 = board2.choice(play, col, grid, col0, col1, col2, col3, col4, col5)
                board2.print_game_board(grid)
                winner = board2.win(grid)
            #next player's move
            move += 1
    else:
        print("Ok, Bye!")
        break
    want_play = input("Would You Like To Play Again? Y/N\nChoice: " )


