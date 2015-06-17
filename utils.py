'''this is a file'''

import colors as c

def ask (qustion):
    print(c.red + qustion + c.reset)
    answer = input('>' + c.base3).lower().strip()
    print(c.reset)
    return answer

if __name__ == '__main__':
    print(c.clear)
    name = ask("what is your name?")
    color = ask("what is your name color?",c.random_color())
