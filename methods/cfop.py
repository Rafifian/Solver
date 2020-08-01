## The steps for solving a cube with CFOP

class CFOP:
    def __init__(self, cube):
        self.cube = cube
        self.solution = []

        self.solve()

    def solve(self):
        cube = self.cube
        solution = self.solution

# Debugging
if __name__ == "__main__":
    pass