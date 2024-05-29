import math

stroke = '#'
stroke_ratio = 0.275
inv_stroke_ratio = 1 / stroke_ratio

""" FUNCTIONS:
pyramid(int): triangular pyramid
grid(int, int): open grid
grid_border(int, int): closed grid
window(int): window
hashtag(int): hashtag
diagonals(int, int): diagonals with spacing
squole(int): square hole fractal
square(int): square
coicle(int): circle
doisk(int): filled coicle
realistic_doisk(int): doisk that considers font aspect ratio
checkerboard(int): checkerboard
smog(*args): aversion tactic
"""

## USEFUL FUNCTIONS ##
def line(n):
    return n * stroke

def staggered(distance, length):
    """Outputs * staggered every n units for a string of length k"""
    line = ""
    for i in range(length):
        if i % distance == 0:
            line += stroke
        else:
            line += " "
    return line

def silence(length):
    return length * " "


## SIMPLE STUFF ##
def pyramid(n):
    for i in range(n):
        print(line(i + 1))

def grid(spacing, number):
    """Maks an open grid, without an external border"""
    total = spacing * number
    for i in range(1, total):
        if i % spacing == 0:
            print(line(total - 1))
        else:
            print(staggered(spacing, total)[1:])

def grid_border(spacing, number):
    """Makes a grid with internal spacing and a number of cells"""
    total = spacing * number + 1
    for i in range(total):
        if i % spacing == 0:
            print(line(total))
        else:
            print(staggered(spacing, total))

## WHY NOTS ##

def window(length):
    """Makes a window with panel side length"""
    grid(length, 2)

def hashtag(size):
    """Makes a hashtag of a certain size"""
    grid(size, 3)

def diagonals(spacing, number):
    """a number of diagonals with a certain spacing"""
    length = spacing * number
    total = spacing
    for i in range(total):
        line= ""
        k = i # relabeling
        while k % spacing != 0:
            line += " "
            k -= 1
        print(line + staggered(spacing, length))

## FRACTALS ##
def thrice(s):
    """returns the list representing the image in s three times over"""
    lines = []
    for i in range(len(s)):
        lines.append(3 * s[i])
    return lines

def yes_no_yes(s):
    """thrice without the middle"""
    lines = []
    for i in range(len(s)):
        lines.append(s[i] + silence(len(s)) + s[i])
    return lines

class Squole:
    def __init__(self, size):
        self.size = 3 ^ size

        if size == 1:
            self.lines = [3 * stroke, stroke + ' ' + stroke, 3 * stroke]
        else:
            self.lines = []
            smaller = Squole(size - 1)

            self.lines.extend(thrice(smaller.lines))
            self.lines.extend(yes_no_yes(smaller.lines))
            self.lines.extend(thrice(smaller.lines))
    
    def __str__(self):
        return '\n'.join(self.lines) # trust

def squole(size):
    print(Squole(size))

## SHAPES ##
def round_to_even(num):
    return round(num / 2) * 2

def square(size):
    for _ in range(size):
        print(line(size))

def coicle(diameter):
    def inner_coicle(diameter):
        radius = diameter / 2
        lines, ks = [], []

        for i in range(diameter):
            if i < radius:
                ks.append(round_to_even(inv_stroke_ratio * math.sqrt(radius ** 2 - (radius - i) ** 2)))
            else:
                ks.append(round_to_even(inv_stroke_ratio * math.sqrt(radius ** 2 - ((i - radius) ** 2))))

        # make a centered line of k stars over diameter spaces
        horiz_diameter = round(inv_stroke_ratio * diameter)
        for i in range(diameter):
            number = ks[i]
            side = (horiz_diameter - number) // 2
            side_space = silence(side)
            lines.append(side_space + stroke + silence(number - 2) + stroke)
        
        return '\n'.join(lines) # trust
    print(inner_coicle(diameter))

def doisk(diameter):
    def inner_doisk(diameter):
        radius = diameter / 2
        lines, ks = [], []

        for i in range(diameter):
            if i < radius:
                ks.append(round_to_even(math.sqrt(radius ** 2 - (radius - i) ** 2)))
            else:
                ks.append(round_to_even(math.sqrt(radius ** 2 - ((i - radius) ** 2))))

        # make a centered line of k stars over diameter spaces
        for i in range(diameter):
            number = ks[i]
            side = (diameter - number) // 2
            side_space = silence(side)
            lines.append(side_space + line(number) + side_space)
        
        return '\n'.join(lines) # trust
    print(inner_doisk(diameter))

def realistic_doisk(diameter):
    def inner_doisk(diameter):
        radius = diameter / 2
        lines, ks = [], []

        for i in range(diameter):
            if i < radius:
                ks.append(round_to_even(inv_stroke_ratio * math.sqrt(radius ** 2 - (radius - i) ** 2)))
            else:
                ks.append(round_to_even(inv_stroke_ratio * math.sqrt(radius ** 2 - ((i - radius) ** 2))))

        # make a centered line of k stars over diameter spaces
        horiz_diameter = round(inv_stroke_ratio * diameter)
        for i in range(diameter):
            number = ks[i]
            side = (horiz_diameter - number) // 2
            side_space = silence(side)
            lines.append(side_space + line(number) + side_space)
        
        return '\n'.join(lines) # trust
    print(inner_doisk(diameter))

def checkerboard(size):
    lines = []
    for i in range(size):
        line = ""
        for j in range(size):
            if (i + j) % 2 == 0:
                line += stroke
            else:
                line += ' '
        lines.append(line)
    print('\n'.join(lines))

def smog(*args):
    checkerboard(99)