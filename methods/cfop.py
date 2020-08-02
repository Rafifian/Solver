## The steps for solving a cube with CFOP
# Imports
from cube import Cube

class CFOP:
    def __init__(self, cube):
        self.cube = cube
        self.solution = []

        self.solve()

    def solve(self):
        cube = self.cube
        solution = self.solution

        self.cross(cube, solution)
    
    def cross(self, cube, solution):
        pass

    def f2l(self, cube, solution):
        pass

    def oll(self, cube, solution):
        pass

    def pll(self, cube, solution):
        pass

# Debugging
if __name__ == "__main__":
    pass