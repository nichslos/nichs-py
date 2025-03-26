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

#Library Exercise 8
import sys

if len(sys.argv) < 2:
    sys.exit("Too few arguments")
elif len(sys.argv) > 2:
    sys.exit("Too many arguments")
print("Hello, my name is", sys.argv[1])

#Library Exercise 9 Slices
import sys

if len(sys.argv) < 2:
    sys.exit("Too few arguments")

for arg in sys.argv[1:]:
    print("Hello, my name is", arg)

#Library Exercise 10 with Packages
#pip install cowsay
import cowsay
import sys

if len(sys.argv) == 2:
    cowsay.trex("Hello" + sys.argv[1])

#Library Exercise 11 with API
#pip install requests
import requests
import sys

if len(sys.argv) != 2:
    sys.exit()

response = requests.get("https://itunes.apple.com/search?entity=song&limit=1&term=" + sys.argv[1])
print(response.json())

#Library Exercise 12 with API, json arrange
#pip install requests
import json
import requests
import sys

if len(sys.argv) != 2:
    sys.exit()

response = requests.get("https://itunes.apple.com/search?entity=song&limit=1&term=" + sys.argv[1])
print(json.dumps(response.json(), indent=2))

#Library Exercise 13 with API, calling json specific object
#pip install requests
import json
import requests
import sys

if len(sys.argv) != 2:
    sys.exit()

response = requests.get("https://itunes.apple.com/search?entity=song&limit=50&term=" + sys.argv[1])

o = response.json()
for result in o["results"]:
    print(result["trackName"])

#Library Exercise 13 create own module
#See at say.py
def main():
    hello("world")
    goodbye("world")

def hello(name):
    print(f"Hello, {name}")

def goodbye(name):
    print(f"goodbye, {name}")

if __name__ == "__main__":
    main()