### Generates a list of moves to make in order to solve the Rubik's Cube from a given scramble.

## Imports
from solve import cfop
from cube import representation, turns
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
    # Initializes a solve.
    # @param scrambles The list of scrambles to solve.
    def __init__(self, scrambles):
        self.scrambles = scrambles
        self.settings = copy(settings)
        self.results = []
    