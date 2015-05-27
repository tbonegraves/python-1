#!/usr/bin/env python3

import colors as c
print(c.clear +  c.red + "Mmmmmmm, mt aka i dont care")
print("wich number")
number = input('>')
print("table for " + number)

for multiplier in range(12,0,-1):
    product = int(number) * multiplier
    form = '{} x {} = {}'
    print(form.format(number,multiplier,product))
    
