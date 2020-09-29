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


@hug.cli()
@hug.get('/{x}/{y}') # create web server hug to call functions, this also counts as a function decorator 
def transform(x: int,y: int):
    return x + y

class TransMatrix():
    def __init__(self,matrix = np.matrix('0 0; 0 0')):
        self.matrix = np.matrix('1 1; .5 -.5')
    
    def __call__(self, cartpoint):
        #take in a point, dot product function on that point with the transformation matrix
        print(self.matrix)





if __name__ == "__main__":
    transform.interface.cli()



# Tests here
def test_transformpoint():
    
    testpoint = np.array([[0],[1]])
    out = matrix(testpoint)
    assert (out == matrix.) 
    pass
