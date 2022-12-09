# oponent = {'A': 'Rock', 'B'}
#    X . Y . Z . 
# A  3 . 6 . 0
# B  0 . 3 . 6
# C  6 . 0 . 3

import numpy as np

game = np.array([[3,6,0], [0,3,6], [6,0,3]])


def convert(letter):
    if letter == 'A' or letter == 'X':
        return 0
    elif letter == 'B' or letter == 'Y':
        return 1
    else:
        return 2

def win(letter):
    pass

def lose(letter):
    pass

def draw(letter):
    


sum = 0
with open("./long.txt", "r") as f:
    for line in f:
        them,me = line.rstrip().split(' ')
        #print(them, me)
        print(game[convert(them),convert(me)] + convert(me) + 1)
        sum += game[convert(them),convert(me)] + convert(me) + 1
        print(sum)
