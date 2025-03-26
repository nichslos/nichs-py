#Loops Exercise 1
i = 3 
while i != 0:
    print("meow")
    i = i - 1

#Loops Exercise 2
j = 0
while j < 0:
    print("Wee")
    j = j + 1

#Loops Exercise 3
for i in range(3):
    print("Hola!")

#Loops Exercise 4
while True:
    x = int(input("What's x? "))
    if x > 0:
        break

for _ in range(x):
    print("Aww!!")

#Loops Exercise 5
def main():
    number = get_number()
    meow(number)

def get_number():
    while True:
        n = int(input("What's n? "))
        if n > 0:
            break
    return n

def meow(n):
    for _ in range(n):
        print("meow")

main()

#Loops Exercise 6
students = ["John", "Noel", "Ron"]
for student in students:
    print(student)

for i in range(len(students)):
    print(i + 1, students[i])
#Loops Exercise 7
people = {
    "Noel",
    "John",
    "Emily"
}
for name in people:
    print(name)

#Loops Exercise 8
person = [
    {"name": "Noel", "location": "USA"},
    {"name": "Angel", "location": "PARIS"},
    {"name": "John", "location": "EUROPE"},
]

for people in person:
    print(people["name"], people["location"], sep=", ")

#Loops Exercise 9
def prints():
    print_column(3)

def print_column(height):
    for _ in range(height):
        print("#")

prints()

#Loops Exercise 10
def brick():
    print_square(3)

def print_square(size):
    for i in range(size):
        print_row(size)

def print_row(width):
    print("#" * width)
brick()