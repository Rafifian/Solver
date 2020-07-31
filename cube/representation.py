## Python representation of the current state of a Rubik's Cube, and methods to turn it.
# Imports
from copy import copy

# cube is a 3-dimensional array to represent the cube.
#
# This is the solved state:
#                ----------------
#                | 0  | 1  | 2  |
#                ----------------
#                | 3  | 4  | 5  |
#                ----------------
#                | 6  | 7  | 8  |
#                ----------------
# -------------------------------------------------------------
# | 9  | 10 | 11 | 18 | 19 | 20 | 27 | 28 | 29 | 36 | 37 | 38 |
# -------------------------------------------------------------
# | 12 | 13 | 14 | 21 | 22 | 23 | 30 | 31 | 32 | 39 | 40 | 41 |
# -------------------------------------------------------------
# | 15 | 16 | 17 | 24 | 25 | 26 | 33 | 34 | 35 | 42 | 43 | 44 |
# -------------------------------------------------------------
#                ----------------
#                | 45 | 46 | 47 |
#                ----------------
#                | 48 | 49 | 50 |
#                ----------------
#                | 51 | 52 | 53 |
#                ----------------
# 
# Here is the solved state, as it is stored internally:
solved_state = [
    # U face
    [
        [0, 1, 2], 
        [3, 4, 5], 
        [6, 7, 8]
    ],
    # L face
    [
        [9, 10, 11], 
        [12, 13, 14], 
        [15, 16, 17]
    ],
    # F face
    [
        [18, 19, 20], 
        [21, 22, 23], 
        [24, 25, 26]
    ],
    # R face
    [
        [27, 28, 29], 
        [30, 31, 32], 
        [33, 34, 35]
    ],
    # B face
    [
        [36, 37, 38], 
        [39, 40, 41], 
        [42, 43, 44]
    ],
    # D face
    [
        [45, 46, 47], 
        [48, 49, 50], 
        [51, 52, 53]
    ],
]
# A scrambled state will have numbers in different places, according to the turn methods that can be found below.
# 
# Importantly, numbers 4, 13, 22, 31, 40, and 49 will never move, as the centers of each face stay the same in relation to each other.
#
# cube, in __init__, is how this information is stored internally. It starts in the solved state, is turned according to the Scramble fed 
# to it, and then is solved according to a method from the methods folder. After, it is compared to solved_state to ensure it is solved.

class Cube:
    ## Representation of a Rubik's cube
    def __init__(self):
        self.cube = copy(solved_state)

    # Checks whether or not the cube is solved.
    def is_solved(self):
        return self.cube == solved_state
    
    ## Turns
    def rTurn(self):
        pass

    def lTurn(self):
        pass

    def uTurn(self):
        pass

    def dTurn(self):
        pass

    def fTurn(self):
        pass

    def bTurn(self):
        pass

    def xRot(self):
        pass

    def yRot(self):
        pass

    def zRot(self):
        pass