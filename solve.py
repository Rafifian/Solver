### Generates a list of moves to make in order to solve the Rubik's Cube from a given scramble.

## Imports
from methods import CFOP
from cube import Cube
from scramble import ScrambleParse
from copy import copy
from math import inf

## Settings **TO BE IMPLEMENTED**
# Pass this to Solve().
settings = {
    # Solution method (beginner's method, cfop, roux, zz, petrus)
    'METHOD': 1,
    # Number of solutions to output. Defaults to all that are given.
    'NUM_OUT': inf
}

class Solve():
    # Initializes a Solve.
    # @param scrambles The list of scrambles to solve.
    def __init__(self, scrambles):
        # A list of parsed scrambles
        self.scrambles = ScrambleParse(scrambles).scrambles
        self.settings = copy(settings)
        # The solutions for each scramble
        self.results = []

        for i in self.scrambles:
            self.solve(i)
        
        self.print_results()
    
    # Prints the results of a Solve.
    def print_results(self):
        # Prints detailed results
        index = 1
        for i in self.results:
            print(f'{index}: {i}')

    # Scrambles the cube based on the scramble and solves it based on the set method.
    def solve(self, scramble):
        cube = Cube()

        # Scramble
        scr_list = scramble.s.split(' ')
        for i in scr_list:
            val = 1
            n = i[0]
            if len(i) == 2:
                if i[1] == "'":
                    val = 3
                if i[1] == '2':
                    val = 2
            while val > 0:
                if n.islower():
                    if n == 'r':
                        for z in range(3):
                            cube.lTurn()
                        cube.xRot()
                    elif n == 'l':
                        for z in range(3):
                            cube.xRot()
                        cube.rTurn()
                    elif n == 'u':
                        cube.dTurn()
                        cube.yRot()
                    elif n == 'd':
                        for z in range(3):
                            cube.yRot()
                        cube.uTurn()
                    elif n == 'f':
                        cube.zRot()
                        cube.bTurn()
                    elif n == 'b':
                        for z in range(3):
                            cube.zRot()
                        cube.fTurn()
                    elif n == 'x':
                        cube.xRot()
                    elif n == 'y':
                        cube.yRot()
                    elif n == 'z':
                        cube.zRot()
                else:    
                    if n == 'R':
                        cube.rTurn()
                    elif n == 'L':
                        cube.lTurn()
                    elif n == 'U':
                        cube.uTurn()
                    elif n == 'D':
                        cube.dTurn()
                    elif n == 'F':
                        cube.fTurn()
                val -= 1  

        # Solve
        method = self.settings['METHOD']
        if method == 0:
            pass
        elif method == 1:
            CFOP(cube)

# Debugging
if __name__ == "__main__":
    pass