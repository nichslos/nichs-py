#Library Exercise 1
import random

coin = random.choice(["heads", "tails"])
print(coin)

#Library Exercise 2
from random import choice
coin1 = choice(["heads", "tails"])
print(coin1)

#Library Exercise 3
import random

number = random.randint(1, 10)
print(number)

#Library Exercise 4
cards = ["jack", "queen", "king"]
random.shuffle(cards)
for card in cards:
    print(card)

#Library Exercise 5
import statistics
print(statistics.mean([100, 90]))

#Library Exercise 6
import sys
print("Hello, my name is", sys.argv[1])

#Library Exercise 7
import sys

if len(sys.argv) < 2:
    print("Too few arguments")
elif len(sys.argv) > 2:
    print("Too many arguments")
else:
    print("hello, my name is", sys.argv[1])