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

blank_state = [[[-1 for y in range(3)]
                for x in range(3)]
                for z in range(6)]

faces = {
    'u': 0,
    'l': 1,
    'f': 2,
    'r': 3,
    'b': 4,
    'd': 5
}

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
        self.blank_state = copy(blank_state)

    # Checks whether or not the cube is solved.
    def is_solved(self):
        return self.cube == solved_state

    # Rotates a 2d array clockwise
    def rotate(self, array):
        a = array
        # transpose
        for i in range(len(a)):
            for j in range(i, len(a)):
                a[i][j], a[j][i] = a[j][i], a[i][j]

        # reverse rows
        for i in range(len(a)):
            k = len(a) - 1
            for j in range(k):
                a[i][j], a[i][k] = a[i][k], a[i][j]
                k = k - 1
        
        return(a)
    
    ## Turns
    def rTurn(self):
        cube = self.cube
        temp = self.blank_state

        # indicies for face, row, and piece
        i = 0
        j = 0
        k = 0

        # for face in cube
        for a in cube:
            j = 0
            # check face
            if i == faces['u']:
                # for row in face
                for b in a:
                    k = 0
                    # for "sticker" in row
                    for c in b:
                        if k <= 1:
                            temp[i][j][k] = c
                        else: 
                            temp[faces['b']][2-j][2-k] = c
                        k += 1
                    j += 1
            elif i == faces['l']:
                # this face isn't affected, so just copy elements from cube to temp
                for b in a:
                    k = 0
                    for c in b:
                        temp[i][j][k] = c
                        k += 1
                    j += 1
            elif i == faces['f']:
                for b in a:
                    k = 0
                    for c in b:
                        if k <= 1:
                            temp[i][j][k] = c
                        else:
                            temp[faces['u']][j][k] = c
                        k += 1
                    j += 1
            elif i == faces['r']:
                # rotate face
                temp[i] = self.rotate(cube[i])
            elif i == faces['b']:
                for b in a:
                    k = 0
                    for c in b:
                        if k >= 1:
                            temp[i][j][k] = c
                        else:
                            temp[faces['d']][2-j][2-k] = c
                        k += 1
                    j += 1
            elif i == faces['d']:
                for b in a:
                    k = 0
                    for c in b:
                        if k <= 1:
                            temp[i][j][k] = c
                        else:
                            temp[faces['f']][j][k] = c
                        k += 1
                    j += 1
            else:
                raise AssertionError(f"{i} is not a valid face value")
            i += 1

        # set self to the temp cube we filled
        self.cube = temp

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

# Debugging
if __name__ == "__main__":
    x = Cube()
    x.rTurn()
    print(x.cube)