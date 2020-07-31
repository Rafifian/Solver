from copy import copy

single_turns = ['R', 'L', 'F', 'B', 'D', 'U']
valid_turns =  single_turns + [i.lower() for i in single_turns]
valid_rot = ['x', 'y', 'z']
valid_mod = ["'", '2', 'w']
valid_chars = valid_turns + valid_rot + valid_mod + [' ']

class Scramble:
    # Initializes a Scramble and its properties. Returns the scramble.
    # @param scramble The given scramble.
    # @param index The scramble number of the given set.
    def __init__(self, scramble, index):
        self.s = scramble
        self.index = index
        self.invalid_chars = []
        self.valid = self.is_valid()

    # Returns a str of this Scramble object.
    def __str__(self):
        return self.s

    # Returns a detailed str of this Scramble object's important features.
    def __repr__(self):
        return f'<Scramble: {self.index} "{self.s}" {self.valid}>'

    # Checks if the scramble is valid. Returns true if it is, and raises errors if not.
    def is_valid(self):
        all_correct = True
        for i in self.s:
            if i not in valid_chars:
                all_correct = False
                self.invalid_chars.append(i)

        if len(self.invalid_chars) == 1:
            raise AssertionError(f'Scramble invalid. "{self.invalid_chars[0]}" is not a valid character.')
        elif len(self.invalid_chars) > 1:
            i = ', '.join(self.s)
            raise AssertionError(f'Scramble invalid. "{i}" are not valid characters.')
        
        return all_correct
    
    # Changes the scramble str in this Scramble object, then checks if it is valid.
    def set_scramble(self, scramble):
        self.s = scramble
        self.is_valid()


# # Debugging
# if __name__ == "__main__":