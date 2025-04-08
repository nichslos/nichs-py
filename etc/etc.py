#ETC exercise 1

students = [
{"name": "Nico", "house": "Pasil"},
{"name": "Neo", "house": "Cebu"},
{"name": "Jane", "house": "Leyte"},
]

houses = []
for student in students:
    if student["house"] not in houses:
        houses.append(student["house"])

for house in sorted(houses):
    print(house)

#ETC exercise 2

students = [
{"name": "Nico", "house": "Pasil"},
{"name": "Neo", "house": "Cebu"},
{"name": "Jane", "house": "Leyte"},
]

houses = set()
for student in students:
    house.add(student["house"])

for house in sorted(houses):
    print(house)

#ETC exercise 3
#Banking

balance = 0

def main():
    print("Balance:", balance)
    deposit(100)
    withdraw(50)
    print("Balance:", balance)

#using global variable
def deposit(n):
    global balance
    balance += n

#using global variable
def withdraw(n):
    global balance
    balance -= n

if __name__ == "__main__":
    main()

#ETC exercise 4
#Banking
#Object-oriented

class Account:
    def __init__(self):
        #private
        self._balance = 0

    #using property protect, getter
    @property
    def balance(self):
        return self._balance
    
    def deposit(self, n):
        self._balance += n

    def withdraw(self, n):
        self._balance -= n

def main():
    account = Account()
    print("Balance:", account.balance)
    account.deposit(100)
    account.withdraw(50)
    print("Balance:", account.balance)

if __name__ == "__main__":
    main()


#ETC exercise 5
#constants
for _ in range(3):
    print("meow")

#ETC exercise 6
#constants
MEOWS= 3

for _ in range(MEOWS):
    print("meow")

#ETC exercise 7
#Object-oriented
#constants
class Cat:
    MEOWS = 3
    
    def meow(self):
        for _ in range(Cat.MEOWS):
            print("meow")

cat = Cat()
cat.meow()

#ETC exercise 8
#type hints
def meow(n: int):
    for _ in range(n):
        print("meows")

number: int = int(input("Number: "))
meow()

#ETC exercise 9
#type hints
#define a string value using -> str
def meow(n: int) -> str:
    return "meow\n" * n

number: int = int(input("Number: "))
meows: str = meow(number)
print(meows, end="")


#ETC exercise 9
#docstrings
def meow(n: int) -> str:
    """
    Meow n times.

    :param n: Number of times to meow
    :type n: int
    :raise TypeError: If n is not an int
    :return: A string of n meows, one per line
    :rtype: str
    """
    return "meow\n" * n

number: int = int(input("Number: "))
meows: str = meow(number)
print(meows, end="")


#ETC exercise 9
#Using sys
import sys

if len(sys.argv) == 1:
    print("meow")
else:
    print("usage: etc.py")


#ETC exercise 9
#argparse
#Using sys
#py etc.py -n 2 or more
import sys

if len(sys.argv) == 1:
    print("meow")
elif len(sys.argv) == 3 and sys.argv[1] == "-n":
    n = int(sys.argv[2])
    for _ in range(n):
        print("meow")
else:
    print("usage: etc.py")

#ETC exercise 10
#argparse
#py etc.py -n 2 or more
import argparse

parser = argparse.ArgumentParser(description="Meow like a cat")
parser.add_argument("-n", help="number of times to meow", type=int)
args = parser.parse_args

for _ in range(args.n):
    print("Meow")

#ETC exercise 10
#unpacking
first, _ = input("What's your name? ").split(" ")
print(f"hello, {first}")

#ETC exercise 11
#unpacking
def total(cents, peso, thounsands):
    return (cents * 17 + peso) * 29 + thounsands

print(total(100, 50, 25), "Thousands")

#ETC exercise 12
#unpacking
def total(cents, peso, thounsands):
    return (cents * 17 + peso) * 29 + thounsands

coins = [100, 50, 25]

print(total(*coins), "Thousands")

#ETC exercise 13
#unpacking
def total(cents, peso, thounsands):
    return (cents * 17 + peso) * 29 + thounsands

print(total(cents=100, peso=50, thounsands=25), "Thousands")

#ETC exercise 14
#unpacking
def total(cents, peso, thounsands):
    return (cents * 17 + peso) * 29 + thounsands

coins = {"cents": 100, "peso": 50, "thousands":25}

print(total(**coins), "Thousands")


#ETC exercise 14
#unpacking
#*args, **kwargs
def f(*args, **kwargs):
    print("Positional:", args)

f(100, 50, 25)

#ETC exercise 15
#unpacking
#*args, **kwargs
def f(*args, **kwargs):
    print("Named:", args)

f(cents=100, peso=50, thousands=25)

#ETC exercise 16
#map
def main():
    yell(["This" "is", "CS50"])

def yell(phrase):
    uppercased = []
    for word in words:
        uppercased.append(word.upper())
    print(uppercased)

if __name__ == "__main__":
    main()

#ETC exercise 17
#map
#map(function, iterable, ...)
def main():
    yell(["This" "is", "CS50"])

def yell(phrase):
    uppercased = map(str.upper)
    print(*uppercased)

if __name__ == "__main__":
    main()

#ETC exercise 18
#list comprehensions
def main():
    yell(["This" "is", "CS50"])

def yell(*words):
    uppercased = [word.upper() for word in words]
    print(*uppercased)

if __name__ == "__main__":
    main()

#ETC exercise 19
#list comprehensions

students = [
{"name": "Nico", "house": "Cebu"},
{"name": "Neo", "house": "Cebu"},
{"name": "Jane", "house": "Cebu"},
]

peoples = [
    student["name"] for student in students["house"] == "Cebu"
]

for people in sorted(peoples):
    print(people)

#ETC exercise 19
#filter
students = [
{"name": "Nico", "house": "Cebu"},
{"name": "Neo", "house": "Cebu"},
{"name": "Jane", "house": "Pasil"},
]

def is_people(s):
    if s["house"] == "Cebu":
        return s["house"] == "Cebu"
    
peoples = filter(is_people, students)

for people in sorted(peoples, key=lambda s: s["name"]):
    print(people["name"])

#ETC exercise 20
#dictionary comprehensions
students = ["Nico", "Jane", "Ron"]

people = []

for student in students:
    people.append({"name": student, "house": "Cebu"})

print(people)


#ETC exercise 21
#dictionary comprehensions
students = ["Nico", "Jane", "Ron"]

people = [{"name": student, "house": "Cebu"} for student in students]

print(people)

#ETC exercise 22
#dictionary comprehensions
students = ["Nico", "Jane", "Ron"]

people = {student: "Cebu" for student in students}

print(people)

#ETC exercise 23
#dictionary comprehensions
students = ["Nico", "Jane", "Ron"]

for i in range(len(students)):
    print(i + 1, students[i])

#ETC exercise 24
#enumerate
students = ["Nico", "Jane", "Ron"]

for i, student in enumerate(students):
    print(i + 1, student)

#ETC exercise 25
#generators
n = int("What's n? ")
for i in range(n):
    print("test" * i)

#ETC exercise 26
#generators
def main():
    n = int("What's n? ")
    for i in range(n):
        print(sheep(i))

def sheep(n):
    return "TEST"

if __name__ == "__main__":
    main()

#ETC exercise 27
#generators
def main():
    n = int("What's n? ")
    for s in sheep(n):
        print(s)

def sheep(n):
    flock = []
    for i in range(n):
        flock.append("TEST" * i)
    return flock

if __name__ == "__main__":
    main()

#ETC exercise 28
#generators, yield
#millions of data
def main():
    n = int("What's n? ")
    for s in sheep(n):
        print(s)

def sheep(n):
    for i in range(n):
        yield "Test" * i

if __name__ == "__main__":
    main()

#ETC exercise 28
#generators, yield, iterators
