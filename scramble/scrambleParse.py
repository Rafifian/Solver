from scramble import Scramble


class ScrambleParse:
    # Initializes a scramble parser, which splits lists of scrambles and returns them as a list of strings.
    # @param unparsed The unparsed list of scrambles.
    def __init__(self, unparsed):
        self.unparsed = unparsed
        self.scrambles = self.parse(unparsed)
        self.numScrambles = len(self.scrambles)

    # Returns a string showing the unparsed scramble and number of scrambles given.
    def __str__(self):
        return f'<ScrambleParse: {self.numScrambles} "{self.unparsed}" {self.scrambles}>'

    # Parses the unparsed string of scrambles and returns a list of Scramble objects.
    def parse(self, unparsed):
        if not isinstance(unparsed, str):
            raise TypeError(f'unparsed must be a str. Given: {unparsed} of type {type(unparsed)}')
        s = unparsed.split('/')
        index = 0
        for i in s:
            i = Scramble(i.strip(), index)
            print(i)
            index += 1
        return s

    def get_unparsed(self):
        return self.unparsed

    def get_scrambles(self):
        return self.scrambles
    
    def get_numScrambles(self):
        return self.numScrambles

# Debugging
if __name__ == "__main__":
    x = ScrambleParse("     R F U' x / R F  ")
    print(x.get_scrambles())