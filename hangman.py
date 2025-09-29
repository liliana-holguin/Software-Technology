# Name: Liliana Holguin
# Date: April 16, 2024
# Course: ET 362
# Assignment: Project2: The Hangman
# Description: Creates an interactive Hangman game
# Preconditions: User input
# Postcondition: Prints hangman and game status

import words

# WRITES HANGMAN #
def printHangman(mistake):
    if mistake == 0:
        print(" +--+")
        print(" |  |")
        print("    |")
        print("    |")
        print("    |")
        print("    |")
        print("=====")
    elif mistake == 1:
        print(" +--+")
        print(" |  |")
        print(" O  |")
        print("    |")
        print("    |")
        print("    |")
        print("=====")
    elif mistake == 2:
        print(" +--+")
        print(" |  |")
        print(" O  |")
        print(" |  |")
        print("    |")
        print("    |")
        print("=====")  
    elif mistake == 3:
        print(" +--+")
        print(" |  |")
        print(" O  |")
        print("/|  |")
        print("    |")
        print("    |")
        print("=====") 
    elif mistake == 4:
        print(" +--+")
        print(" |  |")
        print(" O  |")
        print("/|\\ |")
        print("    |")
        print("    |")
        print("=====")
    elif mistake == 5:
        print(" +--+")
        print(" |  |")
        print(" O  |")
        print("/|\\ |")
        print("/   |")
        print("    |")
        print("=====")
    elif mistake == 6:
        print(" +--+")
        print(" |  |")
        print(" O  |")
        print("/|\\ |")
        print("/ \\ |")
        print("    |")
        print("=====")


# WRITES AVAILABLE/GUESSED LETTERS #
def guess (ch):
    row1 = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm']
    row2 = ['n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

    if (ch in row1):
        row1.remove(ch)
    elif (ch in row2):
        row2.remove(ch)
    
    print("Available Letters:")
    for i in row1:
        print(i, end=" ")
    print("\n")
    for j in row2:
        print(j, end=" ")
    print("\n")

#KEEPS TRACK OF MISTAKES MADE
def mistakes(ch, word, mistake):
    if ch in word:
        mistake += 0
    else:
        mistake += 1
    return mistake

#PRINTS WORD
def printWord(ch, word, wrd):
    if ch in word:
        for i, lett in enumerate(word):
            if lett == ch:
                wrd[i] = lett
    for i, lett in enumerate(wrd):
        if i <= len(wrd) - 1:
            print(lett, end=" ")
            i += 1
    print("\n")
    return wrd

#INITIALIZE GAME WITH 1
game = 1

#GAME BEGINS
print("Welcome to Hangman!")
play = input("Would You Like To Play? Y/N\nChoice: ")
while ((play != 'Y') and (play !='y') and (play != 'N') and (play != 'n')):
    print("Invalid input!")
    play = input("Would You Like To Play? Y/N\nChoice: ")

while ((play == 'Y') or (play =='y') or (play == 'N') or (play == 'n')):
    if ((play == 'Y') or (play =='y')):
        # READ WORDS FROM TEXT FILE AND STORE IN SEPERATE LIST #
        if game > 100:
            game = 1
            wordList = words.getWords(game)
        else:
            wordList = words.getWords(game)
        game += 1
        
        # LET PLAYER CHOOSE CATEGORY #
        print("Here are the categories:")
        print("A. Animals\nF. Food\nP. Plants")
        category = input("Choose the Category: ")
        while ((category != 'A') and (category != 'a') and (category != 'F') and (category != 'f') and (category != 'P') and (category != 'p')):
            print("Invalid Choice!")
            print("Here are the categories:")
            print("A. Animals\nF. Food\nP. Plants")
            category = input("Choose the Category: ")
        
        if ((category == 'A') or (category == 'a')):
            word = wordList[0]
        elif ((category == 'F') or (category == 'f')):
            word = wordList[1]
        else:
            word = wordList[2]
        
        #PRINTS STARTING HANGMAN
        mistake = 0
        word = word.lower()
        printHangman(mistake)

        #CREATES UNDERSCORE LIST FOR WORD
        wrd = []
        for lett in word:
            wrd.append("_ ")
        wrd.pop()
        
        #PRINTS UNDERSCORES FOR WORD
        lett = 0
        while lett < len(word) - 1:
            print("_", end=" ")
            lett += 1
        print("\n")
        
        #PRINTS GUESSABLE LETTERS
        ch = '!'
        guess(ch)
        word = word.strip()
        
        #BEGIN GAME WITH NO WIN
        win = False

        #GUESS BEGINS/PLAYER PLAYS GAME HERE
        while win is False and mistake < 6:
            ch = input("Guess a Letter: ").lower()
            guess(ch)
            mistake = mistakes(ch, word, mistake)

            printHangman(mistake)
            wrd = printWord(ch, word, wrd)
            guess(ch)
            
            if list(word) == wrd:
                win = True
            
        #PRINTS WIN STATUS
        if mistake >= 6:
            printHangman(mistake)
            print("You Lose!")
            print("Thanks for Playing!")
        else:
            print("You Win!")
            print("Thanks for Playing!")
            
        
    else:
        print("Ok, Bye!")
        break
    play = input("Would You Like To Play Again? Y/N\nChoice: " )
    while ((play != 'Y') and (play !='y') and (play != 'N') and (play != 'n')):
        print("Invalid input!")
        play = input("Would You Like To Play? Y/N\nChoice: ")
