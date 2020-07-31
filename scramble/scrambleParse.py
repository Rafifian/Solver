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
        list_out = []
        for i in s:
            list_out.append(Scramble(i.strip(), index))
            index += 1
        return list_out

    # Uses the parsed scramble to
    def parse_to_turns(self):
        pass

    def get_scramble(self, index):
        return self.scrambles[index]

# Debugging
if __name__ == "__main__":
    x = ScrambleParse("     R F U' x / R F  ")
    print(x)
    print(x.get_scramble(0))