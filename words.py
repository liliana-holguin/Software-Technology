def getWords (game):
    a = open("animals.txt", "r")
    f = open("foods.txt", "r")
    p = open("plants.txt", "r")
    
    animal = a.readlines()
    food = f.readlines()
    plant = p.readlines()

    

    return [animal[game-1], food[game-1], plant[game-1]]