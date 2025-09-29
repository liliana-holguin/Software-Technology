# Name: Liliana Holguin
# Date: February 26, 2024
# Course: ET 362
# Assignment: Project1: ATM Simulation Program
# Description: ATM Simulation Program is a Python program that stores user information and allows recognized users to view their balance and withdraw if they have sufficient funds after entering their PIN.
# Precondition: User Entry
# Postcondition: Prints blance


#User Database
user1 = [int(1234), "John", float(100.00)]
user2 = [int(1235), "Kate", float(200.00)]
user3 = [int(1236), "Noah", float(300.00)]
user4 = [int(1237), "Ella", float(400.00)]
user5 = [int(1238), "James", float(500.00)]
user6 = [int(1239), "Emma", float(600.00)]
user7 = [int(1240), "Liam", float(700.00)]
user8 = [int(1241), "Mia", float(800.00)]
user9 = [int(1242), "Jacob", float(900.00)]
user10 = [int(1243), "Ava", float(1000.00)]

x = 1
y = 1

print("\n Welcome to the ATM\n---------------------")

#PIN Validation and User Welcome
while x == 1:
    pin = int(input("Enter PIN: "))
    if pin == user1[0]:
        client = user1
        print(f'\nWelcome {client[1]}!\nYour current balance is ${client[2]:.2f}')
        x = 0
    elif pin == user2[0]:
        client = user2
        print(f'\nWelcome {client[1]}!\nYour current balance is ${client[2]:.2f}')
        x = 0
    elif pin == user3[0]:
        client = user3
        print(f'\nWelcome {client[1]}!\nYour current balance is ${client[2]:.2f}')
        x = 0
    elif pin == user4[0]:
        client = user4
        print(f'\nWelcome {client[1]}!\nYour current balance is ${client[2]:.2f}')
        x = 0
    elif pin == user5[0]:
        client = user5
        print(f'\nWelcome {client[1]}!\nYour current balance is ${client[2]:.2f}')
        x = 0
    elif pin == user6[0]:
        client = user6
        print(f'\nWelcome {client[1]}!\nYour current balance is ${client[2]:.2f}')
        x = 0
    elif pin == user7[0]:
        client = user7
        print(f'\nWelcome {client[1]}!\nYour current balance is ${client[2]:.2f}')
        x = 0
    elif pin == user8[0]:
        client = user8
        print(f'\nWelcome {client[1]}!\nYour current balance is ${client[2]:.2f}')
        x = 0
    elif pin == user9[0]:
        client = user9
        print(f'\nWelcome {client[1]}!\nYour current balance is ${client[2]:.2f}')
        x = 0
    elif pin == user10[0]:
        client = user10
        print(f'\nWelcome {client[1]}!\nYour current balance is ${client[2]:.2f}')
        x = 0
    else:
        print("Invalid PIN\n")
        
#Gives Menu
while y == 1:
    print("\n    Menu\n------------")
    print("b. balance\nw. withdraw\ne. exit\n")

    choice = input("Enter option: ")

    #Balance Inquiry
    if choice == 'b' or choice == 'B':
        print(f'\nYour balance is: ${client[2]:.2f}')
    
    #Withdraw
    elif choice == 'w' or choice == 'W':
        print("\nHow much would you like to withdraw?")
        amnt = float(input("Withdraw Amount: $ "))
        #Checks sufficient funds
        if amnt < client[2]:
            client[2] -= amnt
            print(f'\nYour new balance is: ${client[2]:.2f}')
        else:
            print("\nInsufficient Funds")
    
    #Termination
    elif choice == 'e' or choice == 'E':
        print("\nThanks for using the ATM!\n")
        y = 0
    
    #Invalid choice
    else:
        print("\nInvalid Choice. Choose Again\n")