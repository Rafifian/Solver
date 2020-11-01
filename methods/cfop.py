## The steps for solving a cube with CFOP
# Imports
from cube import Cube

class CFOP:
    def __init__(self, cube):
        self.cube = cube
        self.solution = []

        self.solve()
        print(self.solution)

    def solve(self):
        cube = self.cube
        solution = self.solution

        return(self.cross(cube, solution))
    
    def cross(self, cube, solution):
        cube = self.cube
        solution = self.solution
        cube_array = cube.cube

        # orient yellow on bottom, green on front
        # assume orientation for now

        # check y/g edge
        if cube_array[5][0][1] == 46:
            pass
        else:
            pass

        # check y/o edge
        if cube_array[5][1][0] == 48:
            pass
        else:
            pass

        # check y/r edge
        if cube_array[5][1][2] == 50:
            pass
        else:
            pass

        # check y/b edge
        if cube_array[5][2][1] == 52:
            pass
        else:
            pass

        return(self.f2l(cube, solution))

    def f2l(self, cube, solution):
        cube = self.cube
        solution = self.solution

        return(self.oll(cube, solution))

    def oll(self, cube, solution):
        cube = self.cube
        solution = self.solution

        return(self.pll(cube, solution))

    def pll(self, cube, solution):
        cube = self.cube
        solution = self.solution

        return(cube, solution)

# Debugging
if __name__ == "__main__":
    pass