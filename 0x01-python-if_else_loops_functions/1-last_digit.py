#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number >= 0:
    last_num = number % 10

else:
    last_num = number % -10

if number > 5:
    print("Last digit of {: d} is {: d} and is greater than 5".format
    (number, last_num))
elif number == 0:
    print("Last digit of {:d} is {:d} and is 0".format(number, last_num))
else:
    print("Last digit of {: d} is {: d} and is less than 6 and not 0".format(number, last_num))
