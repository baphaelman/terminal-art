from math import pi

stroke = '#'

## USEFUL FUNCTIONS ##
def line(n):
    line = ""
    for _ in range(n):
        line += stroke
    return line

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
    line = ""
    for _ in range(length):
        line += " "
    return line


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

## WHY NOTS

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

