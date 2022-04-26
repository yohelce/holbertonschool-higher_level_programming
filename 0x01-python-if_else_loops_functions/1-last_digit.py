#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
s = ['Last digit of', 'is', 'and is 0', 'and is greater than 5',
     'and is less than 6 and not 0']
last = number % 10 if number >= 0 else ((number * -1) % 10) * -1
print(s[0], number, s[1], last, s[2] if last == 0 else s[3] \
        if last > 5 else s[4])
