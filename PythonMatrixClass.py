#Chance Young
#last edited: 9/30/2020
#Project Goal: Create a hug server with functionality for a board game, 
#with the option of calculating for isometric coordinates or cartesian coordinates of a player and the enemies. 


import numpy as np
import hug 
#map: map the matrix(x,y) to all points in the generated array e.g. (transform(),[pointlist])
#function decorators: @hug is a function decorator

#hug functionality
#3 dunder: __init__ __call__ __name/main__
#dictionary: keeps track of enemy and player positions in both the cart and iso forms. e.g. (0,1): (player, iso(0,.5))
#generator: generating the board of m x n points and yielding an np.array
#numpy: creating points and matrices
#string interpolation: printing to the web server the position using  %d stuff

#possible hug functions: 
#/position (cart x, cart y) (prints position in both cartesian and isometric)
#/move (cart x, cart y) (will move your "player" to the specified coordinate)

#Generator function that yields x y points
#nums_squared_lc = [num**2 for num in range(5)] <<<< try this
def boardGenerator():
    yield (x, y) for x in range(3) for y in range(3)
 

for value in boardGenerator():
    board.append(value)




# create web server hug to call functions, this also counts as a function decorator 
@hug.cli()
@hug.get('/position') 
def position():
    pass





class TransMatrix():
    def __init__(self,matrix = np.matrix('0 0; 0 0')):
        self.matrix = np.matrix('1 1; .5 -.5')
    
    def __call__(self, cartpoint):
        #take in a point, dot product function on that point with the transformation matrix
        print(self.matrix)





if __name__ == "__main__":
    position.interface.cli()


# Tests here
def test_transformpoint():
    
    #testpoint = np.array([[0],[1]])
    #out = matrix(testpoint)
    #assert (out == matrix.) 
    pass
