#Chance Young
#last edited: 9/30/2020
#Project Goal: Create a hug API with functionality for a board game, 
#with the option of translating the entire board to the isometric coordinate system. 

#Requriments Done:
#my own class implmented: TransformMatrix, which is used to turn the board into isometric coordinates
#Pytest used on at least one function: Position, which passes
#Wrote 

#Upper 5:
#map: map the matrix(x,y) to all points in the generated array e.g. (transform(),[pointlist])
#list comprehension: Used to create the points on the "board"
#function decorators: @hug is a function decorator
#spread operator: used in the getDiagonals
#lambda function: used to create the (x,y) diagonal points.

#Lower 5:
#hug server exposed
#3 dunder functions: __init__ __call__ __name/main__
#dictionary: keeps track of enemy and player positions
#string interpolation: printing information to the server console about the current and updated position of the player
#numpy: various matrices and arrays

import numpy as np
import hug 
import random

class TransMatrix():
    def __init__(self,matrix = [0]):
        self.matrix = np.array([[1, 1], [-.5, .5]])
    def __call__(self, cartpoint):
         temppoint = np.array(cartpoint)
         temppoint.reshape(2,1)
         return np.dot(self.matrix,temppoint)


Masterboard= [(x, y) for x in range(3) for y in range(3)] 

CharacterDict = {
    "Player": Masterboard[0],
    "EnemOne": Masterboard[2],
}

def enemyMove():
    randX = random.randrange(0,3)
    randY = random.randrange(0,3)
    tuppoint = (randX,randY) 
    point = [tuppoint]
    i = 0
    while i < 9:
        if point[0] == Masterboard[i]:
            print(f'EnemyOne position changed to {point}')
            CharacterDict['EnemOne'] = Masterboard[i]
            break
        i = i+1
    enemyOne = CharacterDict['EnemOne']
    player = CharacterDict['Player']
    if player != enemyOne:
        print('The player moved successfully')
        return 1
    else: 
        print(f'The player has died at {player}')
        return 0


#Display the "Board",which is a list of points, to the player
@hug.cli()
@hug.get('/board') 
def board():
    return Masterboard

#get the position of the player
@hug.cli()
@hug.get('/position') 
def position():
    p = CharacterDict['Player']
    print(f'The current player position is {p}')
    return p

#update the player position inside the dictonary for the player and randomly for the enemies. 
#note: If the player and the enemy are on the same square, the game is over. 
@hug.cli()
@hug.get('/move/{x}/{y}') 
def move(x,y):
    err_string = "This point invalid, player not moved."
    
    if x > "2" or x < "0":
        print(err_string)
        return 0
    elif y > "2" or y < "0":
        print(err_string)
        return 0
    else:
        x= int(x)
        y= int(y)
        tuppoint = (x,y) 
        point = [tuppoint]
        i = 0
        while i < 9:
            if point[0] == Masterboard[i]:
                print(f'Player position changed to {point}')
                CharacterDict['Player'] = Masterboard[i]
                return enemyMove()
                break
            i= 1 + i

@hug.cli()
@hug.get('/getDiagonals')
def getDiagonals():
    boardX= [x for x in range(3)]
    boardY= [y for y in range(3)]
    boardtemp = [*boardX,*boardY] #spread operator
    x = lambda x,y : (x,y) # lambda function
    Diagonals = []
    for i in boardtemp:
        Diagonals.append(x(boardtemp[i],boardtemp[i+3]))
    return Diagonals

@hug.cli()
@hug.get('/isometric')
def isometric():
    transmatrix = TransMatrix()
    trans = map(transmatrix,Masterboard)
    trans = list(trans)
    return trans


# Tests here
def test_position():
    assert position() == (0,0)
    pass

if __name__ == "__main__":
    board.interface.cli()
    pass
