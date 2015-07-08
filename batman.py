"akrham seris recap"

import colors as c
from utils import ask

intro =  c.magenta + '''welcome
to the pink fluffy unicorns quiz.

let's test your knowlege...'''

def q1():
    answer = ask("who was the failed robin")
    if answer == "jason tood":
        return True
    return False

def q2():
    answer = ask("who is the arkham knight")
    if answer == 'jason tood':
        return True
    return False

def q3():    
    answer = ask("the joker is iconic what game did he die in")
    if answer == 'arkham city':
        return True
    return False

questions = [q1,q2,q3]


