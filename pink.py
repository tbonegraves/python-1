"pink killer"

import colors as c
from utils import ask

intro =  c.magenta + '''welcome
to the pink fluffy unicorns quiz.

let's test your knowlege...'''

def q1():
    answer = ask("what color are the unicorns?")
    if answer == 'pink':
        return True
    return False

def q2():
    answer = ask("what are the uncorns danceing on?")
    if answer == 'rainbow':
        return True
    return False

def q3():    
    answer = ask("what are ther fur made of?")
    if answer == 'smile':
        return True
    return False

questions = [q1,q2,q3]


