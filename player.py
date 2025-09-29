class Player:
    def __init__(self, name, symbol):
        self.name = name
        self.symbol = symbol
    def move(self):
        print(self.name, end=" ")
        col = input("Enter Column Number to Drop Your Piece: ")
        while col != '0' and col != '1' and col != '2' and col != '3' and col != '4' and col != '5':
            print("Invalid Choice")
            col = input("Enter Column Number to Drop Your Piece: ")
        return col

