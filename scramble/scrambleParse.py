from .scramble import Scramble


class ScrambleParse:
    # Initializes a scramble parser, which splits lists of scrambles and returns them as a list of strings.
    # @param unparsed The unparsed list of scrambles.
    def __init__(self, unparsed):
        self.unparsed = unparsed
        self.scrambles = self.parse(unparsed)
        self.numScrambles = self.scrambles.length

    # Returns a string showing the unparsed scramble and number of scrambles given.
    def __str__(self):
        return f'<ScrambleParse: {self.numScrambles} {self.unparsed}>'

    def parse(self, unparsed):
        if not isinstance(unparsed, str):
            raise TypeError(f'unparsed must be a str. Given: {unparsed} of type {type(unparsed)}')
        s = unparsed.split('/')
        for i in s:
            i.strip()
        return s

# Debugging
if __name__ == "__main__":
    ScrambleParse("     R F U' x / R F  ")