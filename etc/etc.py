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


# Continue at 54:59